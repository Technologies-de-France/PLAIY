# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:20:26 2020

@author: cipop
"""


import sys
from sklearn import kernel_approximation
import numpy

mem = {}

# =============================================================================
# AdditiveChi2Sampler
# =============================================================================

def AdditiveChiFit(sample_steps, sample_interval, X, Y): 
    if sample_steps == -1:
        sample_steps = None
    if sample_interval == -1:
        sample_interval = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        AdditiveChi = kernel_approximation.AdditiveChi2Sampler(sample_steps, sample_interval).fit(X, Y)
        mem['FitAdditiveChi'] = AdditiveChi
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def AdditiveChiFitTransform(sample_steps, sample_interval, X, Y):
    if sample_steps == -1:
        sample_steps = None
    if sample_interval == -1:
        sample_interval = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        AdditiveChi = kernel_approximation.AdditiveChi2Sampler(sample_steps, sample_interval).fit_transform(X, Y)
        dtype = type(AdditiveChi)
        if dtype == numpy.ndarray:
            AdditiveChi = AdditiveChi.tolist()
            return str(AdditiveChi)
        else:
            Mat = AdditiveChi.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    

def AdditiveChiTransform(sample_steps, sample_interval, X, Y):
    if sample_steps == -1:
        sample_steps = None
    if sample_interval == -1:
        sample_interval = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        AdditiveChi = mem['FitAdditiveChi'].transform(X, Y)
        dtype = type(AdditiveChi)
        if dtype == numpy.ndarray:
            AdditiveChi = AdditiveChi.tolist()
            return str(AdditiveChi)
        else:
            Mat = AdditiveChi.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# Nystroem
# =============================================================================

def NystroemFit(kernel, gamma, coef0, degree, kernel_params, n_components, random_state, X, Y): 
    if gamma == 'None' or gamma == '':
        gamma = None
    else: 
        gamma = eval(gamma)
    if coef0 == 'None' or coef0 == '':
        coef0 = None
    else: 
       coef0 = eval(coef0)
    if degree == 'None' or degree == '':
        degree = None
    else: 
        degree = eval(gamma)
    if kernel_params == 'None' or kernel_params == '':
        kernel_params = None
    else: 
        kernel_params = eval(kernel_params)
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        Nystroem = kernel_approximation.Nystroem(kernel, gamma, coef0, degree, kernel_params, n_components, random_state).fit(X, Y)
        mem['FitNystroem'] = Nystroem
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def NystroemFitTransform(kernel, gamma, coef0, degree, kernel_params, n_components, random_state, X, Y):
    if gamma == 'None' or gamma == '':
        gamma = None
    else: 
        gamma = eval(gamma)
    if coef0 == 'None' or coef0 == '':
        coef0 = None
    else: 
       coef0 = eval(coef0)
    if degree == 'None' or degree == '':
        degree = None
    else: 
        degree = eval(gamma)
    if kernel_params == 'None' or kernel_params == '':
        kernel_params = None
    else: 
        kernel_params = eval(kernel_params)
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        Nystroem = kernel_approximation.Nystroem(kernel, gamma, coef0, degree, kernel_params, n_components, random_state).fit_transform(X, Y)
        Nystroem = Nystroem.tolist()
        return str(Nystroem)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    

def NystroemTransform(kernel, gamma, coef0, degree, kernel_params, n_components, random_state, X, Y):
    if gamma == 'None' or gamma == '':
        gamma = None
    else: 
        gamma = eval(gamma)
    if coef0 == 'None' or coef0 == '':
        coef0 = None
    else: 
       coef0 = eval(coef0)
    if degree == 'None' or degree == '':
        degree = None
    else: 
        degree = eval(gamma)
    if kernel_params == 'None' or kernel_params == '':
        kernel_params = None
    else: 
        kernel_params = eval(kernel_params)
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        Nystroem = mem['FitNystroem'].transform(X, Y)
        Nystroem = Nystroem.tolist()
        return str(Nystroem)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# RBFSampler
# =============================================================================

def RBFSamplerFit(gamma, n_components, random_state, X, Y): 
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        RBFSampler = kernel_approximation.RBFSampler(gamma, n_components, random_state).fit(X, Y)
        mem['FitRBFSampler'] = RBFSampler
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def RBFSamplerFitTransform(gamma, n_components, random_state, X, Y):
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        RBFSampler = kernel_approximation.RBFSampler(gamma, n_components, random_state).fit_transform(X, Y)
        RBFSampler = RBFSampler.tolist()
        return str(RBFSampler)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    

def RBFSamplerTransform(gamma, n_components, random_state, X, Y):
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        RBFSampler = mem['FitRBFSampler'].transform(X, Y)
        RBFSampler = RBFSampler.tolist()
        return str(RBFSampler)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# SkewedChi2Sampler
# =============================================================================
        
def SkewedChi2SamplerFit(skewedness, n_components, random_state, X, Y): 
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        SkewedChi2Sampler = kernel_approximation.SkewedChi2Sampler(skewedness, n_components, random_state).fit(X, Y)
        mem['FitSkewedChi2Sampler'] = SkewedChi2Sampler
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def SkewedChi2SamplerFitTransform(skewedness, n_components, random_state, X, Y):
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        SkewedChi2Sampler = kernel_approximation.SkewedChi2Sampler(skewedness, n_components, random_state).fit_transform(X, Y)
        SkewedChi2Sampler = SkewedChi2Sampler.tolist()
        return str(SkewedChi2Sampler)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    

def SkewedChi2SamplerTransform(skewedness, n_components, random_state, X, Y) :
    if random_state == -1:
        random_state = None
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        SkewedChi2Sampler = mem['FitSkewedChi2Sampler'].transform(X, Y)
        SkewedChi2Sampler = SkewedChi2Sampler.tolist()
        return str(SkewedChi2Sampler)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
