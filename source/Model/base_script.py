import sys
import numpy as np
import joblib
import scipy
import json
import re

memory={} #keep the model in memory between mutiple uses of the python nodes

def init_model(name,imp,params):
    modules = ['svm', 'gaussian_process', 'neighbors', 'cluster', 'manifold', 'ensemble', 'tree', 'decomposition', 'naive_bayes', 'isotonic', 'linear_model', 'neural_network', 'mixture', 'kernel_ridge', 'discriminant_analysis']
    found = False
    if imp=='':
        for m in modules:
            try: 
                exec('from sklearn.'+m+' import '+name)
                found = True
                break
            except: pass
        if not found: raise ('Please give the import parameter. ex: from sklearn.linear_model import LinearRegression')
    else: exec(imp)
    memory['name'] = name
    if params == '':
        memory[name] = eval(name)()
    else:
        kwp = params_from_json(params)
        memory[name] = eval(name)(**kwp) #Definition du modele

"""
Certains parametres des objets sklearn peuvent avoir plusieurs types
mais les clusters LabView ne permettent pas cela.
Pour resoudre le probleme, on cree un cluster LabView du nom du parametre
qui contient les differentes possibilite.
On reconstruit ensuite le bon dictionnaire dans Python.
Ex: recu {"param":{"param_type":"int","param_int":3,"param_list":[1,2,3]}}
    reconstruit {"param":3}
Ex:
    recu {"param":{"param_type":"list","param_int":3,"param_list":[1,2,3]}}
    reconstruit {"param":[1,2,3]}
"""

def params_from_json(params):
    params = json.loads(params)
    rd = {}
    for k,v in params.items():
        if type(v)==dict:
            key_needed  = k+'_'+v[k+'_type']
            if key_needed in v: 
                if v[k+'_type']=='float': rd[k] = float(v[key_needed]) #force the type
                elif v[k+'_type']=='dict': rd[k] = eval(v[key_needed]) #force the type
                else: rd[k] = v[key_needed]
            else: rd[k] = v[k+'_type']
        elif k=='estimators':
            rd[k] = [(est,memory[est]) for est in v]
        elif type(v)==list:
            a = np.array(v)
            if np.all(a.shape): rd[k] = a
        elif k=='base_estimator':
            rd[k] = memory[v] if v != 'None' else None
        else: rd[k] = v
    for k,v in rd.items():
        if v=='None': rd[k]=None
    return rd

def set_params(name,params):
    rd = params_from_json(params)
    memory[name].set_params(**rd)

"""
Certains parametres des objets sklearn peuvent avoir plusieurs types
mais les clusters LabView ne permettent pas cela.
Pour resoudre le probleme, on cree un cluster LabView du nom du parametre
qui contient les differentes possibilite.
On reconstruit ensuite le bon dictionnaire dans Python.
Ex: recu {"param":{"param_type":"None","param_int":0,"param_list":[]}}
    parametres du modele {"param":3}
    reconstruit {"param":{"param_type":"int","param_int":3,"param_list":[]}}
Ex:
    recu {"param":{"param_type":"None","param_int":0,"param_list":[]}}
    parametres du modele {"param":[1,2,3]}
    reconstruit {"param":{"param_type":"list","param_int":0,"param_list":[1,2,3]}}
"""
def get_params(requested,name):
    params = memory[name].get_params()
    params = special_case(params) #transforms ndarray to list
    requested = json.loads(requested) #format of the LV cluster
    sd = requested.copy()
    for k,v in sd.items():
        if type(v)==dict: #the parameter k can be of multiple types
            type_needed = type(params[k]).__name__ #ex: 'int'
            key_needed  = k+'_'+type_needed        #ex: 'param_int'
            if type(params[k])==dict: params[k] = dict_to_string(params[k])
            if params[k] is None: pass             #this parameter is not set
            elif key_needed in v:
                sd[k][k+'_type'] = type_needed
                sd[k][key_needed] = params[k]
            else: sd[k][k+'_type'] = params[k]     #param_type can be 'None', 'int', 'list', ... or a string parameter like 'euclidian'
        elif params[k] is None: pass
        elif k=='estimators': sd[k] = [tp[0] for tp in params[k]]
        elif k=='base_estimator': pass
        else: sd[k] = params[k]
    return json.dumps(sd)
    

"""
Certains attributs peuvent avoir des dimensions 1 ou 2 selon les cas.
Pour resoudre ce probleme, on definit dans LabView les attributs avec la dimensions
max et on ajoute dans pythons une dimensions si necessaire.
Ex: array(1), shape=() -> array([1]), shape=(1,)
    array([1,2,3]), shape=(3,) -> array([[1, 2, 3]]), shape=(1,3)
    array([[1, 2, 3],[3,4,5]]), shape=(2,3) -> array([[[1, 2, 3],[3, 4, 5]]]), shape=(1,2,3)
"""

def get_attributes(attributes_requested,name):
    attributes_requested = json.loads(attributes_requested)
    names = attributes_requested.keys() #Tous les attributs ne sont pas definies sous LabView car certains vont disparaître prochainements de sklearn
    attributes = {key:value for key,value in memory[name].__dict__.items() if key in names}
    sa = attributes_requested.copy()
    for k,v in attributes.items():
        if (type(attributes_requested[k])==list):
            v = np.array(v)
            if None in v or not np.all(v.shape):
                sa[k] = attributes_requested[k]
                continue
            n_dim = len(v.shape)
            n_dim_required = len(np.array(attributes_requested[k]).shape)
            if n_dim_required>n_dim: #we need to add a new dimension
                if n_dim>0: sa[k] = v[np.newaxis,:]
                else: sa[k] = v[np.newaxis]
            else: sa[k] = v
        else: sa[k] = v
    sa = special_case(sa)
    try:
        out = json.dumps(sa)
    except TypeError:
        #Certains attributs sont des fonction que Python ne peut pas mettre en forme dans le JSON,
        #dans ce cas, on va remplacer la fonction par son nom
        out = json.dumps(special_case_plus(sa))
    return out

"""
Retourne seulement les valeurs necessaireset non vides
Ex: data = {"X":[1,2,3],"y":[0,0,0],"sample_weight":[]}
    nd = {"X":array([1,2,3]),"y":array([0,0,0])}
"""
def NotEmptyAndNeeded(data,func):
    import inspect
    needed = [key for key in inspect.signature(func).parameters if key in data.keys()]
    nd = {}
    for key in needed:
        if type(data[key])==list:
            a = np.array(data[key])
            if np.all(a.shape):
                if key in ('y','Xred'):
                    for i in a.shape:
                        if i==1: a = a.ravel()
                nd[key] = a
        else: nd[key] = data[key]
    return nd

def special_case(d):
    for key in d.keys():
        if str(type(d[key]))=="<class 'function'>": d[key] = d[key].__name__
        elif str(type(d[key]))=="<class 'numpy.ndarray'>": d[key] = d[key].tolist()
        elif str(type(d[key]))=="<class 'numpy.intc'>": d[key] = int(d[key])
        elif str(type(d[key]))=="<class 'numpy.int32'>": d[key] = int(d[key])
        elif str(type(d[key]))=="<class 'numpy.int64'>": d[key] = int(d[key])
        elif str(type(d[key]))=="<class 'numpy.float64'>": d[key] = float(d[key])
    return d

def special_case_plus(d):
    for key in d.keys():
        if type(d[key]) not in (str, int, float, bool, list, tuple, dict, None): d[key] = type(d[key]).__name__
    return d

def dict_to_string(d):
    if type(list(d.keys())[0])==int: return str(d)
    else: return json.dumps(d)

def fit(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].fit)
    memory[name].fit(**data)

def fit_predict(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].fit_predict)
    out = memory[name].fit_predict(**data)
    if len(out.shape)<2: out = out[:,np.newaxis]
    return out.astype('float64').tolist()

def fit_transform(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].fit_transform)
    out = memory[name].fit_transform(**data)
    if len(out.shape)<2: out = out[:,np.newaxis]
    return out.astype('float64').tolist()

def transform(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].transform)
    out = memory[name].transform(**data)
    if len(out.shape)<2: out = out[:,np.newaxis]
    return out.astype('float64').tolist()

def inverse_transform(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].transform)
    out = memory[name].transform(**data)
    if len(out.shape)<2: out = out[:,np.newaxis]
    return out.astype('float64').tolist()

def decision_function(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].decision_function)
    out = memory[name].decision_function(**data)
    if len(out.shape)<2: out = out[:,np.newaxis]
    return out.astype('float64')

def partial_fit(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].partial_fit)
    memory[name].partial_fit(**data)

def score(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].score)
    return memory[name].score(**data)

def predict(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].predict)
    out = memory[name].predict(**data)
    if len(out.shape)<2: out = out[:,np.newaxis]
    return out.astype('float64')

def predict_ARD(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].predict)
    for k,v in data.items():
        if type(v)==list: data[k] = np.array(v)
    if data['return_std']: out1,out2 = memory[name].predict(**data)
    else: out1,out2 = memory[name].predict(**data),np.array([])
    return out1.tolist(),out2.tolist()

def log_marginal_likelihood(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].log_marginal_likelihood)
    if 'eval_gradient' in data.keys() and data['eval_gradient']: out1,out2 = memory[name].log_marginal_likelihood(**data)
    else: out1,out2 = memory[name].log_marginal_likelihood(**data),np.array([])
    return out1,out2.tolist()

def kneighbors(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].kneighbors)
    for k,v in data.items():
        if type(v)==list: data[k] = np.array(v)
    if data['return_distance']: out1,out2 = memory[name].kneighbors(**data)
    else: 
        out2 = memory[name].kneighbors(**data)
        out1 = np.array([])
    return out1.tolist(),out2.tolist()

def kneighbors_graph(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].kneighbors_graph)
    return memory[name].kneighbors_graph(**data).todense().tolist()

def radius_neighbors_graph(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].radius_neighbors_graph)
    return memory[name].radius_neighbors_graph(**data).todense().tolist()

def radius_neighbors(data):

    def to_list(arrays):
        for i,a in enumerate(arrays):
            for j,aa in enumerate(a):
                a[j] = aa.tolist()
            arrays[i] = a.tolist()
        return arrays

    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].radius_neighbors)
    for k,v in data.items():
        if type(v)==list: data[k] = np.array(v)
    if data['return_distance']: 
        out1,out2 = memory[name].radius_neighbors(**data)
        out1,out2 = to_list([out1,out2])
    else: 
        out2 = memory[name].radius_neighbors(**data)
        out2 = to_list([out2])[0]
        out1 = []
    return out1,out2


def cost_complexity_pruning_path(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].cost_complexity_pruning_path)
    out = memory[name].cost_complexity_pruning_path(**data)
    return out['ccp_alphas'].tolist(),out['impurities'].tolist()

def decision_path(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].decision_path)
    return memory[name].decision_path(**data).todense().tolist(),[]

def decision_path_etc(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].decision_path)
    out = memory[name].decision_path(**data)
    return out[0].todense().tolist(),out[1].tolist()

def sample(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].sample)
    out = memory[name].sample(**data)
    return out[0].tolist(),out[1].tolist()

def get_covariance():
    return memory[memory['name']].get_covariance().tolist()

def get_precision():
    return memory[memory['name']].get_precision().tolist()

def get_depth():
    return memory[memory['name']].get_depth()

def get_n_leaves():
    return memory[memory['name']].get_n_leaves()

def reconstruction_error():
    return memory[memory['name']].reconstruction_error()

def get_indices(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].get_indices)
    row_ind,col_ind = memory[name].get_shape(**data)
    return int(row_ind),int(col_ind)

def get_shape(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].get_shape)
    return memory[name].get_shape(**data)

def get_submatrix(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].get_submatrix)
    return memory[name].get_submatrix(**data).tolist()

def perplexity(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].perplexity)
    return memory[name].perplexity(**data)

def aic(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].aic)
    return memory[name].aic(**data)

def bic(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].bic)
    return memory[name].bic(**data)


def debug(function,data):
    try:
        return str(eval(function)(data))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message


def save_model(UserModelName=str,path=str):
    try:
        filename=path+'.gz'
        joblib.dump(memory[UserModelName],filename=filename)
        return filename
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 



def load_model(UserModelName=str,file=str):

    try:
        memory[UserModelName]=joblib.load(filename=file) 
        return str(memory[UserModelName])
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def get_help(UserModelName=str):
    try:
        return str(memory[UserModelName].__doc__)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 


func_names = ['apply','predict_proba','predict_log_proba','score_samples']
code = """
def {f_name}(data):
    data = json.loads(data)
    name=data['name']
    memory['name'] = name
    data = NotEmptyAndNeeded(data,memory[name].{f_name})
    return memory[name].{f_name}(**data).tolist()
"""
for f_name in func_names:
    exec(code.format(f_name=f_name))
