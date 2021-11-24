# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:09:21 2020

@author: cipop
"""

import sys
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn import impute
import numpy as np


mem = {}

def TypeVar(var):
    if var == 'float':
        var = float
    if var == 'dict':
        var = dict
    if var == 'list':
        var = list
    if var == 'object':
        var = object
    if var == 'bool':
        var = bool
    if var == 'str':
        var = str
    if var == 'int':
        var = int
    if var == 'None':
        var = None
    return var

# =============================================================================
# SimpleImputer
# =============================================================================


def SimpleImputerFit(missing_values, strategy, dtype_fill_value, str_, int_, verbose, copy, add_indicator, X, Y): 
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    if missing_values == 'nan':
        missing_values = np.nan
    elif missing_values == '' or missing_values == 'None':
        missing_values = None
    else:
        missing_values = eval(missing_values)
    if dtype_fill_value == 'None':
        fill_value = None
    elif dtype_fill_value == 'int' :
        fill_value = int_
    else:
        fill_value = str_  
    try:
        SimpleImputer = impute.SimpleImputer(missing_values, strategy, fill_value, verbose, copy, add_indicator).fit(X, Y)
        mem['FitSimpleImputer'] = SimpleImputer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def SimpleImputerFitTransform(missing_values, strategy, dtype_fill_value, str_, int_, verbose, copy, add_indicator, X, Y):
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    if missing_values == 'nan':
        missing_values = np.nan
    elif missing_values == '' or missing_values == 'None':
        missing_values = None
    else:
        missing_values = eval(missing_values)
    if dtype_fill_value == 'None':
        fill_value = None
    elif dtype_fill_value == 'int' :
        fill_value = int_
    else:
        fill_value = str_  
    try:
        SimpleImputer = impute.SimpleImputer(missing_values, strategy, fill_value, verbose, copy, add_indicator).fit_transform(X, Y)
        SimpleImputer = SimpleImputer.tolist()
        return str(SimpleImputer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    

def SimpleImputerTransform(missing_values, strategy, dtype_fill_value, str_, int_, verbose, copy, add_indicator, X, Y): 
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    if missing_values == 'nan':
        missing_values = np.nan
    elif missing_values == '' or missing_values == 'None':
        missing_values = None
    else:
        missing_values = eval(missing_values)
    if dtype_fill_value == 'None':
        fill_value = None
    elif dtype_fill_value == 'int' :
        fill_value = int_
    else:
        fill_value = str_  
    try:
        SimpleImputer = mem['FitSimpleImputer'].transform(X, Y)
        SimpleImputer = SimpleImputer.tolist()
        return str(SimpleImputer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# MissingIndicator
# =============================================================================

def MissingIndicatorFit(missing_values, features, sparses, error_on_new, X):
    X = eval(X)
    if missing_values == 'nan':
        missing_values = np.nan
    elif missing_values == '' or missing_values == 'None':
        missing_values = None
    else:
        missing_values = eval(missing_values)
    if features == 'None':
        features = None
    if sparses == 'True':
        sparses = True
    elif sparses == 'False':
        sparses = False
    elif sparses == 'None':
        sparses = None
    else:
        sparses = 'auto'
    try:
        MissingIndicator = impute.MissingIndicator(missing_values, features, sparses, error_on_new).fit(X)
        mem['FitMissingIndicator'] = MissingIndicator
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def MissingIndicatorFitTransform(missing_values, features, sparses, error_on_new, X):
    X = eval(X)
    if missing_values == 'nan':
        missing_values = np.nan
    elif missing_values == '' or missing_values == 'None':
        missing_values = None
    else:
        missing_values = eval(missing_values)
    if features == 'None':
        features = None
    if sparses == 'True':
        sparses = True
    elif sparses == 'False':
        sparses = False
    elif sparses == 'None':
        sparses = None
    else:
        sparses = 'auto'
    try:
        MissingIndicator = impute.MissingIndicator(missing_values, features, sparses, error_on_new).fit_transform(X)
        MissingIndicator = MissingIndicator.tolist()
        return str(MissingIndicator)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    

def MissingIndicatorTransform(missing_values, features, sparses, error_on_new, X):  
    X = eval(X)
    if missing_values == 'nan':
        missing_values = np.nan
    elif missing_values == '' or missing_values == 'None':
        missing_values = None
    else:
        missing_values = eval(missing_values)
    if features == 'None':
        features = None
    if sparses == 'True':
        sparses = True
    elif sparses == 'False':
        sparses = False
    elif sparses == 'None':
        sparses = None
    else:
        sparses = 'auto'
    try:
        MissingIndicator = mem['FitMissingIndicator'].transform(X)
        MissingIndicator = MissingIndicator.tolist()
        return str(MissingIndicator)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# KNNImputer
# =============================================================================

def KNNImputerFit(missing_values, n_neighbors, weights, metric, copy, add_indicator, X, Y):
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    if weights != 'uniform' and weights != 'distance':
        weights = eval(weights)
    if metric != 'nan_euclidean':
        metric = eval(metric)
    if missing_values == 'nan':
        missing_values = np.nan
    elif missing_values == '' or missing_values == 'None':
        missing_values = None
    else:
        missing_values = eval(missing_values)
    try:
        KNNImputer = impute.KNNImputer(missing_values, n_neighbors, weights, metric, copy, add_indicator).fit(X, Y)
        mem['FitKNNImputer'] = KNNImputer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def KNNImputerFitTransform(missing_values, n_neighbors, weights, metric, copy, add_indicator, X, Y):
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    if weights != 'uniform' and weights != 'distance':
        weights = eval(weights)
    if metric != 'nan_euclidean':
        metric = eval(metric)
    if missing_values == 'nan':
        missing_values = np.nan
    elif missing_values == '' or missing_values == 'None':
        missing_values = None
    else:
        missing_values = eval(missing_values)
    try:
        KNNImputer = impute.KNNImputer(missing_values, n_neighbors, weights, metric, copy, add_indicator).fit_transform(X, Y)
        KNNImputer = KNNImputer.tolist()
        return str(KNNImputer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    

def KNNImputerTransform(missing_values, n_neighbors, weights, metric, copy, add_indicator, X, Y):  
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    if weights != 'uniform' and weights != 'distance':
        weights = eval(weights)
    if metric != 'nan_euclidean':
        metric = eval(metric)
    if missing_values == 'nan':
        missing_values = np.nan
    elif missing_values == '' or missing_values == 'None':
        missing_values = None
    else:
        missing_values = eval(missing_values)
    try:
        KNNImputer = mem['FitKNNImputer'].transform(X, Y)
        KNNImputer = KNNImputer.tolist()
        return str(KNNImputer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# IterativeImputer
# =============================================================================

def IterativeImputerFit(estimator, missing_values, sample_posterior, max_iter, tol, n_nearest_features, initial_strategy, imputation_order, skip_complete, min_value, max_value, verbose, random_state, add_indicator, X, Y):
    if estimator == 'None' or estimator == '':
        estimator = None
    else:
        estimator = eval(estimator)
    if missing_values == 'nan':
        missing_values = np.nan
    else:
        missing_values = eval(missing_values)
    if n_nearest_features == -1:
        n_nearest_features = None
    if min_value == [] or min_value[0] == 'None':
        min_value = None
    else:
        min_value = eval(min_value)
    if max_value == [] or max_value[0] == 'None':
        max_value = None
    else:
        max_value = eval(max_value)
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        IterativeImputers = IterativeImputer(estimator, missing_values, sample_posterior, max_iter, tol, n_nearest_features, initial_strategy, imputation_order, skip_complete, min_value, max_value, verbose, random_state, add_indicator).fit(X, Y)
        mem['FitIterativeImputer'] = IterativeImputers
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def IterativeImputerFitTransform(estimator, missing_values, sample_posterior, max_iter, tol, n_nearest_features, initial_strategy, imputation_order, skip_complete, min_value, max_value, verbose, random_state, add_indicator, X, Y):
    if estimator == 'None' or estimator == '':
        estimator = None
    else:
        estimator = eval(estimator)
    if missing_values == 'nan':
        missing_values = np.nan
    else:
        missing_values = eval(missing_values)
    if n_nearest_features == -1:
        n_nearest_features = None
    if min_value == [] or min_value[0] == 'None':
        min_value = None
    else:
        min_value = eval(min_value)
    if max_value == [] or max_value[0] == 'None':
        max_value = None
    else:
        max_value = eval(max_value)
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        IterativeImputers = IterativeImputer(estimator, missing_values, sample_posterior, max_iter, tol, n_nearest_features, initial_strategy, imputation_order, skip_complete, min_value, max_value, verbose, random_state, add_indicator).fit_transform(X, Y)
        IterativeImputers = IterativeImputers.tolist()
        return str(IterativeImputers)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    

def IterativeImputerTransform(estimator, missing_values, sample_posterior, max_iter, tol, n_nearest_features, initial_strategy, imputation_order, skip_complete, min_value, max_value, verbose, random_state, add_indicator, X, Y):  
    if estimator == 'None' or estimator == '':
        estimator = None
    else:
        estimator = eval(estimator)
    if missing_values == 'nan':
        missing_values = np.nan
    else:
        missing_values = eval(missing_values)
    if n_nearest_features == -1:
        n_nearest_features = None
    if min_value == [] or min_value[0] == 'None':
        min_value = None
    else:
        min_value = eval(min_value)
    if max_value == [] or max_value[0] == 'None':
        max_value = None
    else:
        max_value = eval(max_value)
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        IterativeImputer = mem['FitIterativeImputer'].transform(X, Y)
        IterativeImputer = IterativeImputer.tolist()
        return str(IterativeImputer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message