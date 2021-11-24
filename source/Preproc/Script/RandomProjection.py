# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:42:27 2020

@author: cipop
"""


import sys
from sklearn import random_projection
import numpy


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
# GaussianRandomProjection
# =============================================================================
    
def GaussianRandomProjectionFit(n_components, eps_donne, random_state_donne, X, Y): 
    if n_components != 'auto':
        n_components = eval(n_components)
    if eps_donne == -1:
        eps_donne = None
    if random_state_donne == -1:
        random_state_donne = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        GaussianRandomProjection = random_projection.GaussianRandomProjection(n_components, eps = eps_donne, random_state = random_state_donne).fit(X, Y)
        mem['FitGaussianRandomProjection'] = GaussianRandomProjection
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def GaussianRandomProjectionFitTransform(n_components, eps_donne, random_state_donne, X, Y):
    if n_components != 'auto':
        n_components = eval(n_components)
    if eps_donne == -1:
        eps_donne = None
    if random_state_donne == -1:
        random_state_donne = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        GaussianRandomProjection = random_projection.GaussianRandomProjection(n_components, eps = eps_donne, random_state = random_state_donne).fit_transform(X, Y)
        dtype = type(GaussianRandomProjection)
        if dtype == numpy.ndarray:
            GaussianRandomProjection = GaussianRandomProjection.tolist()
            return str(GaussianRandomProjection)
        else:
            Mat = GaussianRandomProjection.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    

def GaussianRandomProjectionTransform(n_components, eps_donne, random_state_donne, X, Y):
    if n_components != 'auto':
        n_components = eval(n_components)
    if eps_donne == -1:
        eps_donne = None
    if random_state_donne == -1:
        random_state_donne = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        GaussianRandomProjection = mem['FitGaussianRandomProjection'].transform(X, Y)
        dtype = type(GaussianRandomProjection)
        if dtype == numpy.ndarray:
            GaussianRandomProjection = GaussianRandomProjection.tolist()
            return str(GaussianRandomProjection)
        else:
            Mat = GaussianRandomProjection.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# SparseRandomProjection
# =============================================================================

def SparseRandomProjectionFit(n_components, density_donne, eps_donne, dense_output_donne, random_state_donne, X, Y): 
    if n_components != 'auto':
        n_components = eval(n_components)
    if density_donne != 'auto':
        density_donne = eval(density_donne)
    if eps_donne == -1:
        eps_donne = None    
    if random_state_donne == -1:
        random_state_donne = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        SparseRandomProjection = random_projection.SparseRandomProjection(n_components, density = density_donne, eps = eps_donne , dense_output = dense_output_donne, random_state = random_state_donne).fit(X, Y)
        mem['FitSparseRandomProjection'] = SparseRandomProjection
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def SparseRandomProjectionFitTransform(n_components, density_donne, eps_donne, dense_output_donne, random_state_donne, X, Y):
    if n_components != 'auto':
        n_components = eval(n_components)
    if density_donne != 'auto':
        density_donne = eval(density_donne)
    if eps_donne == -1:
        eps_donne = None    
    if random_state_donne == -1:
        random_state_donne = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        SparseRandomProjection = random_projection.SparseRandomProjection(n_components, density = density_donne, eps = eps_donne , dense_output = dense_output_donne, random_state = random_state_donne).fit_transform(X, Y)
        dtype = type(SparseRandomProjection)
        if dtype == numpy.ndarray:
            SparseRandomProjection = SparseRandomProjection.tolist()
            return str(SparseRandomProjection)
        else:
            Mat = SparseRandomProjection.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    

def SparseRandomProjectionTransform(n_components, density_donne, eps_donne, dense_output_donne, random_state_donne, X, Y):
    if n_components != 'auto':
        n_components = eval(n_components)
    if density_donne != 'auto':
        density_donne = eval(density_donne)
    if eps_donne == -1:
        eps_donne = None    
    if random_state_donne == -1:
        random_state_donne = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        SparseRandomProjection = mem['FitSparseRandomProjection'].transform(X, Y)
        dtype = type(SparseRandomProjection)
        if dtype == numpy.ndarray:
            SparseRandomProjection = SparseRandomProjection.tolist()
            return str(SparseRandomProjection)
        else:
            Mat = SparseRandomProjection.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# johnson_lindenstrauss_min_dim
# =============================================================================

def JohnsonProjection(n_samples, eps): 
    try:
        Johnson = random_projection.johnson_lindenstrauss_min_dim(n_samples, eps)
        Johnson = Johnson.tolist()
        return str(Johnson)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

