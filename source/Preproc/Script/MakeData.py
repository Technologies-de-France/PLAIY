# -*- coding: utf-8 -*-
import sys
from sklearn import datasets
import numpy 
from pylab import shape


def biclusters(n_rows, n_cols, n_clusters, noise, minval, maxval, shuffle, random_state, returns):
    try:
        if random_state == -1:
            random_state = None
        X, rows, columns = datasets.make_biclusters((n_rows, n_cols), n_clusters, noise, minval, maxval, shuffle, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        elif returns == 'rows' :
            data_rows = rows.tolist()
            return str(data_rows)
        else:
            data_columns = columns.tolist()
            return str(data_columns)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def blobs(n_samples,  n_features, centers, cluster_std, centermin, centermax, shuffle, random_state, return_centers, returns):
    try:
        if len(n_samples) == 1:
            n_samples = n_samples[0]
        if centers == []:
            centers = None
        if centers == [[]]:
            centers = None
        size_centers = shape(centers)
        if size_centers == (1,):
            centers = centers[0]
        if size_centers == (1, 1):
            centers = centers[0][0]
        if len(cluster_std) == 1:
           cluster_std = cluster_std[0]
        if random_state == -1:
            random_state = None
        X, y, centers = datasets.make_blobs(n_samples,  n_features, centers, cluster_std, (centermin, centermax), shuffle, random_state, return_centers)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        elif returns == 'Y' :
            data_y = y.tolist()
            return str(data_y)
        else:
            data_centers = centers.tolist()
            return str(data_centers)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def checkerboard(n_rows, n_cols, n_clusters, noise, minval, maxval, shuffle, random_state, returns):
    try:
        n_clusters = eval(n_clusters)
        if random_state == -1:
            random_state = None
        X, rows, columns = datasets.make_checkerboard((n_rows, n_cols), n_clusters, noise, minval, maxval, shuffle, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        elif returns == 'rows' :
            data_rows = rows.tolist()
            return str(data_rows)
        else:
            data_columns = columns.tolist()
            return str(data_columns)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def circles(n_samples, shuffle, noise, random_state, factor, returns):
    try:
        n_samples = eval(n_samples)
        if noise == -1:
            noise = None
        if random_state == -1:
            random_state = None
        X, y = datasets.make_circles(n_samples, shuffle, noise, random_state, factor)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        else :
            datay = y.tolist()
            return str(datay)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def classification(n_samples,  n_features, n_informative, n_redundant, n_repeated, n_classes, n_clusters_per_class, weights, flip_y, class_sep, 
          hypercube,  shift,  scale, shuffle, random_state, returns):
    try: 
        if weights == []:
            weights = None
        if random_state == -1:
            random_state = None
        if shift == []:
            shift = None
        if scale == []:
            scale = None
        X, y = datasets.make_classification(n_samples,  n_features, n_informative, n_redundant, n_repeated, n_classes, n_clusters_per_class, weights, flip_y, class_sep, hypercube,  shift,  scale, shuffle, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        else :
            datay = y.tolist()
            return str(datay)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def friedman1(n_samples, n_features, noise, random_state, returns):
    try: 
        if random_state == -1:
            random_state = None
        X, y = datasets.make_friedman1(n_samples, n_features, noise, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        else :
            datay = y.tolist()
            return str(datay)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def friedman2(n_samples, noise, random_state, returns):
    try:
        if random_state == -1:
            random_state = None
        X, y = datasets.make_friedman2(n_samples, noise, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        else :
            datay = y.tolist()
            return str(datay)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def friedman3(n_samples, noise, random_state, returns):
    try: 
        if random_state == -1:
            random_state = None
        X, y = datasets.make_friedman3(n_samples, noise, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        else :
            datay = y.tolist()
            return str(datay)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def gaussian_quantiles(mean, cov, n_samples, n_features, n_classes, shuffle, random_state, returns):
    try: 
        if mean[0] == -1:
            mean = None 
        if random_state == -1 :
            random_state = None
        X, y = datasets.make_gaussian_quantiles(mean, cov, n_samples, n_features, n_classes, shuffle, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        else :
            datay = y.tolist()
            return str(datay)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def hastie_10_2(n_samples, random_state, returns):
    try: 
        if random_state == -1:
            random_state = None
        X, y = datasets.make_hastie_10_2(n_samples, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        else :
            datay = y.tolist()
            return str(datay)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def low_rank_matrix(n_samples, n_features, effective_rank, tail_strength, random_state):
    try:
        if random_state == -1:
            random_state = None
        X = datasets.make_low_rank_matrix(n_samples, n_features, effective_rank, tail_strength, random_state)
        data = X.tolist()
        return str(data)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def moons(n_samples, shuffle, noise, random_state, returns):
    try:
        n_samples = eval(n_samples)
        if random_state == -1:
            random_state = None
        if noise == -1:
            noise = None
        X, y = datasets.make_moons(n_samples, shuffle, noise, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        else:
            datay = y.tolist()
            return str(datay)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def multilabel_classification(n_samples, n_features, n_classes, n_labels, length, allow_unlabeled, sparse, return_indicator, return_distributions, random_state, returns):
    try:
        if random_state == -1:
            random_state = None
        if return_indicator == 'False':
            return_indicator = False
        X, y, p_c, p_w_c = datasets.make_multilabel_classification(n_samples, n_features, n_classes, n_labels, length, allow_unlabeled, sparse, return_indicator, return_distributions, random_state)
        dtype = type(y) 
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        elif returns == 'Y':
            if dtype == numpy.ndarray:
                datay = y.tolist()
                return str(datay)
            else:
                Mat = y.tocoo()
                return str(list(zip(Mat.row, Mat.col, Mat.data)))
        elif returns == 'p_c':
            data_p_c = p_c.tolist()
            return str(data_p_c)
        else:
            data_p_w_c = p_w_c.tolist()
            return str(data_p_w_c)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def regression(n_samples, n_features, n_informative, n_targets, bias, effective_rank, tail_strength, noise, shuffle, coef, random_state, returns):
    try:
        if random_state == -1:
            random_state = None
        if effective_rank == 'None':
            effective_rank = None
        else: 
            effective_rank = eval(effective_rank)
        X, y, coef = datasets.make_regression(n_samples, n_features, n_informative, n_targets, bias, effective_rank, tail_strength, noise, shuffle, coef, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX) 
        elif returns == 'Y':
            datay = y.tolist()
            return str(datay)
        else:
            data_coef = coef.tolist()
            return str(data_coef)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

    
def s_curve(n_samples, noise, random_state, returns):
    try:
        if random_state == -1:
            random_state = None
        X, t = datasets.make_s_curve(n_samples, noise, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        else: 
            data_t = t.tolist()
            return str(data_t)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def sparse_coded_signal(n_samples, n_components, n_features, n_nonzero_coefs, random_state, returns):
    try : 
        if random_state == -1:
            random_state = None
        data, dictionary, code = datasets.make_sparse_coded_signal(n_samples, n_components, n_features, n_nonzero_coefs, random_state)
        if returns == 'data':
            datalist = data.tolist()
            return str(datalist)
        elif returns == 'dictionary':
            datalist = dictionary.tolist()
            return str(datalist)
        else:
            datalist = code.tolist()
            return str(datalist)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
        

def sparse_spd_matrix(dim, alpha, norm_diag, smallest_coef, largest_coef, random_state):
    try : 
        if random_state == -1:
            random_state = None
        data = datasets.make_sparse_spd_matrix(dim, alpha, norm_diag, smallest_coef, largest_coef, random_state)
        datas = data.tolist()
        return str(datas)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def sparse_uncorrelated(n_samples, n_features, random_state, returns):
    try :
        if random_state == -1:
            random_state = None
        X, y = datasets.make_sparse_uncorrelated(n_samples, n_features, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)
        else:
            datay = y.tolist()
            return str(datay)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    

def spd_matrix(n_dim, random_state):
    try: 
        if random_state == -1:
            random_state = None
        data = datasets.make_spd_matrix(n_dim, random_state)
        datalist = data.tolist()
        return str(datalist)   
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def swiss_roll(n_samples, noise, random_state, returns):
    try: 
        if random_state == -1:
            random_state = None
        X, t = datasets.make_swiss_roll(n_samples, noise, random_state)
        if returns == 'X':
            dataX = X.tolist()
            return str(dataX)   
        else: 
            data_t = t.tolist()
            return str(data_t)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    



    
    