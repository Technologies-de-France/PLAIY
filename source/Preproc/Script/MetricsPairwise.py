# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:10:53 2020

@author: cipop
"""


import sys
from sklearn import metrics
import numpy as np
import numpy

# =============================================================================
# additive_chi2_kernel
# =============================================================================

def additive_chi2_kernel(X, Y):
    try:
        X = eval(X)
        if Y == '':
           Y = None
        else:
           Y = eval(Y)
        additive_chi2_kernel = metrics.pairwise.additive_chi2_kernel(X, Y)
        additive_chi2_kernel = additive_chi2_kernel.tolist()
        return str(additive_chi2_kernel)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# chi2_kernel
# =============================================================================

def chi2_kernel(X, Y, gamma):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        chi2_kernel = metrics.pairwise.chi2_kernel(X, Y, gamma)
        chi2_kernel = chi2_kernel.tolist()
        return str(chi2_kernel)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# cosine_similarity
# =============================================================================

def cosine_similarity(X, Y, dense_output):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        cosine_similarity = metrics.pairwise.cosine_similarity(X, Y, dense_output)
        cosine_similarity = cosine_similarity.tolist()
        return str(cosine_similarity)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# cosine_distances
# =============================================================================

def cosine_distances(X, Y):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        cosine_distances = metrics.pairwise.cosine_distances(X, Y)
        cosine_distances = cosine_distances.tolist()
        return str(cosine_distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

# =============================================================================
# euclidean_distances
# =============================================================================

def euclidean_distances(X, Y, Y_norm_squared, squared, X_norm_squared):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        if Y_norm_squared == '':
            Y_norm_squared = None
        else:
            Y_norm_squared = eval(Y_norm_squared)
        if X_norm_squared == '':
            X_norm_squared = None
        else:
            X_norm_squared = eval(X_norm_squared)
        euclidean_distances = metrics.pairwise.euclidean_distances(X, Y)
        euclidean_distances = euclidean_distances.tolist()
        return str(euclidean_distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# haversine_distances
# =============================================================================

def haversine_distances(X, Y):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        haversine_distances = metrics.pairwise.haversine_distances(X, Y)
        haversine_distances = haversine_distances.tolist()
        return str(haversine_distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# laplacian_kernel
# =============================================================================

def laplacian_kernel(X, Y, gamma):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        if gamma == 'None' or gamma == '':
            gamma = None
        else:
            gamma = eval(gamma)
        laplacian_kernel = metrics.pairwise.laplacian_kernel(X, Y, gamma)
        laplacian_kernel = laplacian_kernel.tolist()
        return str(laplacian_kernel)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# linear_kernel
# =============================================================================

def linear_kernel(X, Y, dense_output):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        linear_kernel = metrics.pairwise.linear_kernel(X, Y, dense_output)
        linear_kernel = linear_kernel.tolist()
        return str(linear_kernel)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# manhattan_distances
# =============================================================================

def manhattan_distances(X, Y, dense_output):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        manhattan_distances = metrics.pairwise.manhattan_distances(X, Y, dense_output)
        manhattan_distances = manhattan_distances.tolist()
        return str(manhattan_distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# nan_euclidean_distances
# =============================================================================

def nan_euclidean_distances(X, Y, squared, missing_values, copy):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        if missing_values == 'nan':
            missing_values = np.nan
        else:
            missing_values = eval(missing_values)
        nan_euclidean_distances = metrics.pairwise.nan_euclidean_distances(X, Y, squared, missing_values, copy)
        nan_euclidean_distances = nan_euclidean_distances.tolist()
        return str(nan_euclidean_distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# pairwise_kernels
# =============================================================================

def pairwise_kernels(X, Y, metric, filter_params, n_jobs):
    try:
        values_metric = ['additive_chi2', 'chi2', 'linear', 'poly', 'polynomial', 'rbf', 'laplacian', 'sigmoid', 'cosine']
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        if metric not in values_metric:
            metric = eval(metric)
        if n_jobs == 'None' or n_jobs == '':
            n_jobs = None
        else:
            n_jobs = eval(n_jobs)
        pairwise_kernels = metrics.pairwise.pairwise_kernels(X, Y, metric, filter_params, n_jobs)
        pairwise_kernels = pairwise_kernels.tolist()
        return str(pairwise_kernels)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# polynomial_kernel
# =============================================================================

def polynomial_kernel(X, Y, degree, gamma, coef0):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        if gamma == 'None' or gamma == '':
            gamma = None
        else:
            gamma = eval(gamma)
        polynomial_kernel = metrics.pairwise.polynomial_kernel(X, Y, degree, gamma, coef0)
        polynomial_kernel = polynomial_kernel.tolist()
        return str(polynomial_kernel)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# rbf_kernel
# =============================================================================

def rbf_kernel(X, Y, gamma):
    try:
        X = eval(X)
        if Y == '':
             Y = None
        else:
             Y = eval(Y)
        if gamma == 'None' or gamma == '':
             gamma = None
        else:
             gamma = eval(gamma)
        rbf_kernel = metrics.pairwise.rbf_kernel(X, Y, gamma)
        rbf_kernel = rbf_kernel.tolist()
        return str(rbf_kernel)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# sigmoid_kernel
# =============================================================================

def sigmoid_kernel(X, Y, gamma, coef0):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        if gamma == 'None' or gamma == '':
            gamma = None
        else:
            gamma = eval(gamma)
        sigmoid_kernel = metrics.pairwise.sigmoid_kernel(X, Y, gamma, coef0)
        sigmoid_kernel = sigmoid_kernel.tolist()
        return str(sigmoid_kernel)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# paired_euclidean_distances
# =============================================================================

def paired_euclidean_distances(X, Y):
    try:
        X = eval(X)
        Y = eval(Y)
        paired_euclidean_distances = metrics.pairwise.paired_euclidean_distances(X, Y)
        paired_euclidean_distances = paired_euclidean_distances.tolist()
        return str(paired_euclidean_distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# paired_manhattan_distances
# =============================================================================

def paired_manhattan_distances(X, Y):
    try:
        X = eval(X)
        Y = eval(Y)
        paired_manhattan_distances = metrics.pairwise.paired_manhattan_distances(X, Y)
        paired_manhattan_distances = paired_manhattan_distances.tolist()
        return str(paired_manhattan_distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# paired_cosine_distances
# =============================================================================

def paired_cosine_distances(X, Y):
    try:
        X = eval(X)
        Y = eval(Y)
        paired_cosine_distances = metrics.pairwise.paired_cosine_distances(X, Y)
        paired_cosine_distances = paired_cosine_distances.tolist()
        return str(paired_cosine_distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# paired_distances
# =============================================================================

def paired_distances(X, Y, metric):
    try:
        X = eval(X)
        Y = eval(Y)
        values_metric = ['euclidean', 'manhattan', 'cosine']
        if metric not in values_metric:
            metric = eval(metric)
        paired_distances = metrics.pairwise.paired_distances(X, Y, metric)
        paired_distances = paired_distances.tolist()
        return str(paired_distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# pairwise_distances
# =============================================================================

def pairwise_distances(X, Y, metric, n_jobs, force_all_finite):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        values_metric = ['cityblock', 'cosine', 'euclidean', 'l1', 'l2', 'manhattan', 'nan_euclidean', 'braycurtis', 'canberra', 'chebyshev', 'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski', 'mahalanobis', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule' ]
        if metric not in values_metric:
            metric = eval(metric)
        if n_jobs == 'None' or n_jobs == '':
            n_jobs = None
        else:
            n_jobs = eval(n_jobs)
        if force_all_finite == 'True':
            force_all_finite = True
        elif force_all_finite == 'False':
            force_all_finite = False
        else:
            pass
        pairwise_distances = metrics.pairwise.pairwise_distances(X, Y, metric, n_jobs, force_all_finite)
        pairwise_distances = pairwise_distances.tolist()
        return str(pairwise_distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# pairwise_distances_argmin
# =============================================================================

def pairwise_distances_argmin(X, Y, axis, metric, metric_kwargs):
    try:
        X = eval(X)
        Y = eval(Y)
        values_metric = ['cityblock', 'cosine', 'euclidean', 'l1', 'l2', 'manhattan', 'braycurtis', 'canberra', 'chebyshev', 'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski', 'mahalanobis', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule' ]
        if metric not in values_metric:
            metric = eval(metric)
        if metric_kwargs == '':
            metric_kwargs = None
        else:
            metric_kwargs= eval(metric_kwargs) 
        pairwise_distances_argmin = metrics.pairwise_distances_argmin(X, Y, axis, metric, metric_kwargs)
        pairwise_distances_argmin = pairwise_distances_argmin.tolist()
        return str(pairwise_distances_argmin)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# pairwise_distances_argmin_min
# =============================================================================

def pairwise_distances_argmin_min(X, Y, axis, metric, metric_kwargs, returns): 
    try:
        X = eval(X)
        Y = eval(Y)
        values_metric = ['cityblock', 'cosine', 'euclidean', 'l1', 'l2', 'manhattan', 'braycurtis', 'canberra', 'chebyshev', 'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski', 'mahalanobis', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule' ]
        if metric not in values_metric:
            metric = eval(metric)
        if metric_kwargs == '':
            metric_kwargs = None
        else:
            metric_kwargs= eval(metric_kwargs) 
        argmin, distances = metrics.pairwise_distances_argmin_min(X, Y, axis, metric, metric_kwargs)
        if returns == 'argmin':
            argmin = argmin.tolist()
            return str(argmin)
        else: 
            distances = distances.tolist()
            return str(distances)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# pairwise_distances_chunked
# =============================================================================

def pairwise_distances_chunked(X, Y, reduce_func, metric, n_jobs, working_memory):
    try:
        X = eval(X)
        if Y == '':
            Y = None
        else:
            Y = eval(Y)
        if reduce_func == 'None' or reduce_func == '':
            reduce_func = None
        else:
            reduce_func = eval(reduce_func)
        values_metric = ['cityblock', 'cosine', 'euclidean', 'l1', 'l2', 'manhattan', 'braycurtis', 'canberra', 'chebyshev', 'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski', 'mahalanobis', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule' ]
        if metric not in values_metric:
            metric = eval(metric)
        if n_jobs == 'None' or n_jobs == '':
            n_jobs = None
        else:
            n_jobs = eval(n_jobs)
        if working_memory == 'None' or working_memory == '':
            working_memory = None
        else:
            working_memory = eval(working_memory)
        pairwise_distances_chunked = metrics.pairwise_distances_chunked(X, Y, reduce_func, metric, n_jobs, working_memory)
        pairwise_distances_chunked = next(pairwise_distances_chunked)
        dtype = type(pairwise_distances_chunked)
        if dtype == numpy.ndarray:
            D_chunk = pairwise_distances_chunked.tolist()
            return str(D_chunk)
        else:
            Mat = pairwise_distances_chunked.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message