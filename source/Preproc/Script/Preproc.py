# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:22:37 2020

@author: cipop
"""

import sys
from sklearn import preprocessing
import numpy
import numpy as np

mem = {}

# =============================================================================
# Type
# =============================================================================

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
    return var

#PREPROC

# =============================================================================
# Binarizer
# =============================================================================
def Binarizer_Fit(threshold, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        binarizer_fit = preprocessing.Binarizer(threshold, copy).fit(X, y)
        mem['FitBinarizer'] = binarizer_fit
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def Binarizer_FitTransform(threshold, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        binarizer_fit_transform = preprocessing.Binarizer(threshold, copy).fit_transform(X, y)
        binarizer_fit_transform = binarizer_fit_transform.tolist()
        return str(binarizer_fit_transform)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def Binarizer_Transform(threshold, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        binarizer_transform = mem['FitBinarizer'].transform(X)
        binarizer_transform = binarizer_transform.tolist()
        return str(binarizer_transform)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message  

# =============================================================================
# FunctionTransformer
# =============================================================================

def FunctionTransformer_Fit(func, inverse_func, validate, accept_sparse, check_inverse, kw_args, inv_kw_args, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    if func == 'None' or func == '':
        func = None
    else :
        func = eval(func)
    if inverse_func == 'None' or inverse_func == '':
        inverse_func = None
    else :
        inverse_func = eval(inverse_func)
    if kw_args == 'None' or kw_args == '':
        kw_args = None
    else :
        kw_args = eval(kw_args)
    if inv_kw_args == 'None' or inv_kw_args == '':
        inv_kw_args = None
    else :
        inv_kw_args = eval(inv_kw_args)
    try:
        FunctionTransformer = preprocessing.FunctionTransformer(func, inverse_func, validate, accept_sparse, check_inverse, kw_args, inv_kw_args).fit(X, y)
        mem['FitFunctionTransformer'] = FunctionTransformer
        return str(FunctionTransformer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def FunctionTransformer_FitTransform(func, inverse_func, validate, accept_sparse, check_inverse, kw_args, inv_kw_args, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    if func == 'None' or func == '':
        func = None
    else :
        func = eval(func)
    if inverse_func == 'None' or inverse_func == '':
        inverse_func = None
    else :
        inverse_func = eval(inverse_func)
    if kw_args == 'None' or kw_args == '':
        kw_args = None
    else :
        kw_args = eval(kw_args)
    if inv_kw_args == 'None' or inv_kw_args == '':
        inv_kw_args = None
    else :
        inv_kw_args = eval(inv_kw_args)
    try:
       
        FunctionTransformer = preprocessing.FunctionTransformer(func, inverse_func, validate, accept_sparse, check_inverse, kw_args, inv_kw_args).fit_transform(X, y)
        dtype = type(FunctionTransformer)
        if dtype == numpy.ndarray:
            FunctionTransformer = FunctionTransformer.tolist()
            return str(FunctionTransformer) 
        else:
            Mat = FunctionTransformer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def FunctionTransformer_Transform(func, inverse_func, validate, accept_sparse, check_inverse, kw_args, inv_kw_args, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    if func == 'None' or func == '':
        func = None
    else :
        func = eval(func)
    if inverse_func == 'None' or inverse_func == '':
        inverse_func = None
    else :
        inverse_func = eval(inverse_func)
    if kw_args == 'None' or kw_args == '':
        kw_args = None
    else :
        kw_args = eval(kw_args)
    if inv_kw_args == 'None' or inv_kw_args == '':
        inv_kw_args = None
    else :
        inv_kw_args = eval(inv_kw_args)
    try:
        FunctionTransformer = mem['FitFunctionTransformer'].transform(X)
        dtype = type(FunctionTransformer)
        if dtype == numpy.ndarray:
            FunctionTransformer = FunctionTransformer.tolist()
            return str(FunctionTransformer) 
        else:
            Mat = FunctionTransformer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
# =============================================================================
# KBinsDiscretizer
# =============================================================================

def KBinsDiscretizer_Fit(n_bins, encode, strategy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    if len(n_bins) == 1:
        n_bins = n_bins[0]
    try:
        KBinsDiscretizer= preprocessing.KBinsDiscretizer(n_bins, encode, strategy).fit(X, y)
        mem['FitKBinsDiscretizer'] = KBinsDiscretizer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def KBinsDiscretizer_FitTransform(n_bins, encode, strategy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    if len(n_bins) == 1:
        n_bins = n_bins[0]
    try:
        
        KBinsDiscretizer = preprocessing.KBinsDiscretizer(n_bins, encode, strategy).fit_transform(X, y)
        dtype = type(KBinsDiscretizer)
        if dtype == numpy.ndarray:
            KBinsDiscretizer = KBinsDiscretizer.tolist()
            return str(KBinsDiscretizer) 
        else:
            Mat = KBinsDiscretizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def KBinsDiscretizer_Transform(n_bins, encode, strategy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    if len(n_bins) == 1:
        n_bins = n_bins[0]
    try:
        KBinsDiscretizer= mem['FitKBinsDiscretizer'].transform(X)
        dtype = type(KBinsDiscretizer)
        if dtype == numpy.ndarray:
            KBinsDiscretizer = KBinsDiscretizer.tolist()
            return str(KBinsDiscretizer) 
        else:
            Mat = KBinsDiscretizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

# =============================================================================
# KernelCenterer
# =============================================================================

def KernelCenterer_Fit(X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        KernelCenterer = preprocessing.KernelCenterer().fit(X, y)
        mem['FitKernelCenterer'] = KernelCenterer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def KernelCenterer_FitTransform(X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        KernelCenterer = preprocessing.KernelCenterer().fit_transform(X, y)
        dtype = type(KernelCenterer)
        if dtype == numpy.ndarray:
            KernelCenterer = KernelCenterer.tolist()
            return str(KernelCenterer) 
        else:
            Mat = KernelCenterer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def KernelCenterer_Transform(K, y):
    K = eval(K)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        KernelCenterer = mem['FitKernelCenterer'].transform(K)
        dtype = type(KernelCenterer)
        if dtype == numpy.ndarray:
            KernelCenterer = KernelCenterer.tolist()
            return str(KernelCenterer) 
        else:
            Mat = KernelCenterer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

# =============================================================================
# LabelBinarizer
# =============================================================================

def LabelBinarizer_Fit(neg_label, pos_label, sparse_output, y):
    y = eval(y)
    try:
        LabelBinarizer = preprocessing.LabelBinarizer(neg_label, pos_label, sparse_output).fit(y)
        mem['FitLabelBinarizer'] = LabelBinarizer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def LabelBinarizer_FitTransform(neg_label, pos_label, sparse_output, y):
    y = eval(y)
    try:
        LabelBinarizer = preprocessing.LabelBinarizer(neg_label, pos_label, sparse_output).fit_transform(y)
        dtype = type(LabelBinarizer)
        if dtype == numpy.ndarray:
            LabelBinarizer = LabelBinarizer.tolist()
            return str(LabelBinarizer) 
        else:
            Mat = LabelBinarizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def LabelBinarizer_Transform(neg_label, pos_label, sparse_output, y): #sparse_output renvoie une matrice creuse si Vrai
    y = eval(y)
    try:
        LabelBinarizer = mem['FitLabelBinarizer'].transform(y)
        dtype = type(LabelBinarizer)
        if dtype == numpy.ndarray:
            LabelBinarizer = LabelBinarizer.tolist()
            return str(LabelBinarizer) 
        else:
            Mat = LabelBinarizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

# =============================================================================
# LabelEncoder
# =============================================================================
        
def LabelEncoder_Fit(y):
    y = eval(y)
    try:
        LabelEncoder = preprocessing.LabelEncoder().fit(y)
        mem['FitLabelEncoder'] = LabelEncoder
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def LabelEncoder_FitTransform(y):
    y = eval(y)
    try:
        LabelEncoder = preprocessing.LabelEncoder().fit_transform(y)
        LabelEncoder = LabelEncoder.tolist()
        return str(LabelEncoder)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def LabelEncoder_Transform(y):
    y = eval(y)
    try:
        LabelEncoder = mem['FitLabelEncoder'].transform(y)
        LabelEncoder = LabelEncoder.tolist()
        return str(LabelEncoder)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# MultiLabelBinarizer
# =============================================================================
        
def MultiLabelBinarizer_Fit(classes, sparse_output, y):
    y = eval(y)
    if classes == '' or classes == 'None':
        classes = None
    else:
        classes = eval(classes)
    try:
        MultiLabelBinarizer = preprocessing.MultiLabelBinarizer(classes, sparse_output).fit(y)
        mem['FitMultiLabelBinarizer'] = MultiLabelBinarizer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def MultiLabelBinarizer_FitTransform(classes, sparse_output, y):
    y = eval(y)
    if classes == '' or classes == 'None':
        classes = None
    else:
        classes = eval(classes)
    try:
        MultiLabelBinarizer = preprocessing.MultiLabelBinarizer(classes, sparse_output).fit_transform(y)
        dtype = type(MultiLabelBinarizer)
        if dtype == numpy.ndarray:
            MultiLabelBinarizer = MultiLabelBinarizer.tolist()
            return str(MultiLabelBinarizer) 
        else:
            Mat = MultiLabelBinarizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def MultiLabelBinarizer_Transform(classes, sparse_output, y):
    y = eval(y)
    if classes == '' or classes == 'None':
        classes = None
    else:
        classes = eval(classes)
    try:
        MultiLabelBinarizer = mem['FitMultiLabelBinarizer'].transform(y)
        dtype = type(MultiLabelBinarizer)
        if dtype == numpy.ndarray:
            MultiLabelBinarizer = MultiLabelBinarizer.tolist()
            return str(MultiLabelBinarizer) 
        else:
            Mat = MultiLabelBinarizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

# =============================================================================
# MaxAbsScaler
# =============================================================================
        
def MaxAbsScaler_Fit(copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        MaxAbsScaler_fit = preprocessing.MaxAbsScaler(copy).fit(X, y)
        mem['FitMaxAbsScaler'] = MaxAbsScaler_fit
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def MaxAbsScaler_FitTransform(copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        MaxAbsScaler = preprocessing.MaxAbsScaler(copy).fit_transform(X, y)
        dtype = type(MaxAbsScaler)
        if dtype == numpy.ndarray:
            MaxAbsScaler = MaxAbsScaler.tolist()
            return str(MaxAbsScaler) 
        else:
            Mat = MaxAbsScaler.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def MaxAbsScaler_Transform(copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        MaxAbsScaler = mem['FitMaxAbsScaler'].transform(X)
        dtype = type(MaxAbsScaler)
        if dtype == numpy.ndarray:
            MaxAbsScaler = MaxAbsScaler.tolist()
            return str(MaxAbsScaler) 
        else:
            Mat = MaxAbsScaler.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def MaxAbsScaler_Partial_Fit(copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        MaxAbsScaler = preprocessing.MaxAbsScaler(copy).partial_fit(X, y)
        mem['FitMaxAbsScaler'] = MaxAbsScaler
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# MinMaxScaler
# =============================================================================
        
def MinMaxScaler_Fit(n_min, n_max, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        MinMaxScaler = preprocessing.MinMaxScaler((n_min, n_max), copy).fit(X, y)
        mem['FitMinMaxScaler'] = MinMaxScaler
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def MinMaxScaler_FitTransform(n_min, n_max, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        MinMaxScaler = preprocessing.MinMaxScaler((n_min, n_max), copy).fit_transform(X, y)
        dtype = type(MinMaxScaler)
        if dtype == numpy.ndarray:
            MinMaxScaler = MinMaxScaler.tolist()
            return str(MinMaxScaler) 
        else:
            Mat = MinMaxScaler.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def MinMaxScaler_Transform(n_min, n_max, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        MinMaxScaler = mem['FitMinMaxScaler'].transform(X)
        dtype = type(MinMaxScaler)
        if dtype == numpy.ndarray:
            MinMaxScaler = MinMaxScaler.tolist()
            return str(MinMaxScaler) 
        else:
            Mat = MinMaxScaler.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def MinMaxScaler_Partial_Fit(n_min, n_max, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        MinMaxScaler = preprocessing.MinMaxScaler((n_min, n_max), copy).partial_fit(X, y)
        mem['FitMinMaxScaler'] = MinMaxScaler
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# Normalizer
# =============================================================================
        
def Normalizer_Fit(norm, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        Normalizer = preprocessing.Normalizer(norm, copy).fit(X, y)
        mem['FitNormalizer'] = Normalizer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def Normalizer_FitTransform(norm, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        Normalizer = preprocessing.Normalizer(norm, copy).fit_transform(X, y)
        dtype = type(Normalizer)
        if dtype == numpy.ndarray:
            Normalizer = Normalizer.tolist()
            return str(Normalizer) 
        else:
            Mat = Normalizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def Normalizer_Transform(norm, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        Normalizer = mem['FitNormalizer'].transform(X, y)
        dtype = type(Normalizer)
        if dtype == numpy.ndarray:
            Normalizer = Normalizer.tolist()
            return str(Normalizer) 
        else:
            Mat = Normalizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

# =============================================================================
# OneHotEncoder
# =============================================================================
        
def OneHotEncoder_Fit(categories, drop, sparse, dtype, handle_unknown, X, y):
    X = eval(X)
    dtype = TypeVar(dtype)
    if drop == 'None':
        drop = None
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        OneHotEncoder = preprocessing.OneHotEncoder(categories, drop, sparse, dtype, handle_unknown).fit(X, y)
        mem['FitOneHotEncoder'] = OneHotEncoder
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def OneHotEncoder_FitTransform(categories, drop, sparse, dtype, handle_unknown, X, y):
    X = eval(X)
    dtype = TypeVar(dtype)
    if drop == 'None':
        drop = None
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        OneHotEncoder = preprocessing.OneHotEncoder(categories, drop, sparse, dtype, handle_unknown).fit_transform(X, y)
        dtype_func = type(OneHotEncoder)
        if dtype_func == numpy.ndarray:
            OneHotEncoder = OneHotEncoder.tolist()
            return str(OneHotEncoder) 
        else:
            Mat = OneHotEncoder.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def OneHotEncoder_Transform(categories, drop, sparse, dtype, handle_unknown, X, y):
    X = eval(X)
    dtype = TypeVar(dtype)
    if drop == 'None':
        drop = None
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        OneHotEncoder = mem['FitOneHotEncoder'].transform(X)
        dtype_func = type(OneHotEncoder)
        if dtype_func == numpy.ndarray:
            OneHotEncoder = OneHotEncoder.tolist()
            return str(OneHotEncoder) 
        else:
            Mat = OneHotEncoder.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def OneHotEncoder_Feature_Names(categories, drop, sparse, dtype, handle_unknown, X, y):
    dtype = eval(dtype)
    if drop == 'None':
        drop = None
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        OneHotEncoder_feature_names = mem['FitOneHotEncoder'].get_feature_names()
        return str(OneHotEncoder_feature_names)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# OrdinalEncoder
# =============================================================================
        
def OrdinalEncoder_Fit(categories, dtype, X, y):
    X = eval(X)
    dtype = TypeVar(dtype) 
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        OrdinalEncoder = preprocessing.OrdinalEncoder(categories, dtype).fit(X, y)
        mem['FitOrdinalEncoder'] = OrdinalEncoder
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def OrdinalEncoder_FitTransform(categories, dtype, X, y):
    X = eval(X)
    dtype = TypeVar(dtype)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        OrdinalEncoder = preprocessing.OrdinalEncoder(categories, dtype).fit_transform(X, y)
        dtype_func = type(OrdinalEncoder)
        if dtype_func == numpy.ndarray:
            OrdinalEncoder = OrdinalEncoder.tolist()
            return str(OrdinalEncoder) 
        else:
            Mat = OrdinalEncoder.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def OrdinalEncoder_Transform(categories, dtype, X, y):
    X = eval(X)
    dtype = TypeVar(dtype)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        OrdinalEncoder = mem['FitOrdinalEncoder'].transform(X)
        dtype_func = type(OrdinalEncoder)
        if dtype_func == numpy.ndarray:
            OrdinalEncoder = OrdinalEncoder.tolist()
            return str(OrdinalEncoder) 
        else:
            Mat = OrdinalEncoder.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# PolynomialFeatures
# =============================================================================
        
def PolynomialFeatures_Fit(degree, interaction_only, include_bias, order, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        PolynomialFeatures = preprocessing.PolynomialFeatures(degree, interaction_only, include_bias, order).fit(X, y)
        mem['FitPolynomialFeatures'] = PolynomialFeatures
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def PolynomialFeatures_FitTransform(degree, interaction_only, include_bias, order, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        PolynomialFeatures = preprocessing.PolynomialFeatures(degree, interaction_only, include_bias, order).fit_transform(X, y)
        dtype = type(PolynomialFeatures)
        if dtype == numpy.ndarray:
            PolynomialFeatures = PolynomialFeatures.tolist()
            return str(PolynomialFeatures) 
        else:
            Mat = PolynomialFeatures.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def PolynomialFeatures_Transform(degree, interaction_only, include_bias, order, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        PolynomialFeatures = mem['FitPolynomialFeatures'].transform(X)
        dtype = type(PolynomialFeatures)
        if dtype == numpy.ndarray:
            PolynomialFeatures = PolynomialFeatures.tolist()
            return str(PolynomialFeatures) 
        else:
            Mat = PolynomialFeatures.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def PolynomialFeatures_Feature_Names(degree, interaction_only, include_bias, order, X):
    try:
        PolynomialFeatures = mem['FitPolynomialFeatures'].get_feature_names()
        return str(PolynomialFeatures)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# PowerTransformer
# =============================================================================
        
def PowerTransformer_Fit(method, standardize, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        PowerTransformer = preprocessing.PowerTransformer(method, standardize, copy).fit(X, y)
        mem['FitPowerTransformer'] = PowerTransformer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def PowerTransformer_FitTransform(method, standardize, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        PowerTransformer = preprocessing.PowerTransformer(method, standardize, copy).fit_transform(X, y)
        dtype = type(PowerTransformer)
        if dtype == numpy.ndarray:
            PowerTransformer = PowerTransformer.tolist()
            return str(PowerTransformer) 
        else:
            Mat = PowerTransformer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def PowerTransformer_Transform(method, standardize, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        PowerTransformer = mem['FitPowerTransformer'].transform(X)
        dtype = type(PowerTransformer)
        if dtype == numpy.ndarray:
            PowerTransformer = PowerTransformer.tolist()
            return str(PowerTransformer) 
        else:
            Mat = PowerTransformer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# QuantileTransformer
# =============================================================================
        
def QuantileTransformer_Fit(n_quantiles, output_distribution, ignore_implicit_zeros, subsample, random_state, copy, X, y):
    X = eval(X)
    if random_state == -1 :
        random_state = None
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        QuantileTransformer = preprocessing.QuantileTransformer(n_quantiles, output_distribution, ignore_implicit_zeros, subsample, random_state, copy).fit(X, y)
        mem['FitQuantileTransformer'] = QuantileTransformer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def QuantileTransformer_FitTransform(n_quantiles, output_distribution, ignore_implicit_zeros, subsample, random_state, copy, X, y):
    X = eval(X)
    if random_state == -1 :
        random_state = None
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        QuantileTransformer = preprocessing.QuantileTransformer(n_quantiles, output_distribution, ignore_implicit_zeros, subsample, random_state, copy).fit_transform(X, y)
        dtype = type(QuantileTransformer)
        if dtype == numpy.ndarray:
            QuantileTransformer = QuantileTransformer.tolist()
            return str(QuantileTransformer) 
        else:
            Mat = QuantileTransformer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def QuantileTransformer_Transform(n_quantiles, output_distribution, ignore_implicit_zeros, subsample, random_state, copy, X, y):
    X = eval(X)
    if random_state == -1 :
        random_state = None
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        QuantileTransformer = mem['FitQuantileTransformer'].transform(X)
        dtype = type(QuantileTransformer)
        if dtype == numpy.ndarray:
            QuantileTransformer = QuantileTransformer.tolist()
            return str(QuantileTransformer) 
        else:
            Mat = QuantileTransformer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

# =============================================================================
# RobustScaler
# =============================================================================
        
def RobustScaler_Fit(with_centering, with_scaling, q_min, q_max, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        RobustScaler = preprocessing.RobustScaler(with_centering, with_scaling, (q_min, q_max), copy).fit(X, y)
        mem['FitRobustScaler'] = RobustScaler
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def RobustScaler_FitTransform(with_centering, with_scaling, q_min, q_max, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        RobustScaler = preprocessing.RobustScaler(with_centering, with_scaling, (q_min, q_max), copy).fit_transform(X, y)
        dtype = type(RobustScaler)
        if dtype == numpy.ndarray:
            RobustScaler = RobustScaler.tolist()
            return str(RobustScaler) 
        else:
            Mat = RobustScaler.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def RobustScaler_Transform(with_centering, with_scaling, q_min, q_max, copy, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        RobustScaler = mem['FitRobustScaler'].transform(X)
        dtype = type(RobustScaler)
        if dtype == numpy.ndarray:
            RobustScaler = RobustScaler.tolist()
            return str(RobustScaler) 
        else:
            Mat = RobustScaler.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

# =============================================================================
# StandardScaler
# =============================================================================
        
def StandardScaler_Fit(copy, with_mean, with_std, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        StandardScaler= preprocessing.StandardScaler(copy, with_mean, with_std).fit(X, y)
        mem['FitStandardScaler'] = StandardScaler
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def StandardScaler_FitTransform(copy, with_mean, with_std, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        StandardScaler = preprocessing.StandardScaler(copy, with_mean, with_std).fit_transform(X, y)
        dtype = type(StandardScaler)
        if dtype == numpy.ndarray:
            StandardScaler = StandardScaler.tolist()
            return str(StandardScaler) 
        else:
            Mat = StandardScaler.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def StandardScaler_Transform(copy, with_mean, with_std, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        StandardScaler = mem['FitStandardScaler'].transform(X)
        dtype = type(StandardScaler)
        if dtype == numpy.ndarray:
            StandardScaler = StandardScaler.tolist()
            return str(StandardScaler) 
        else:
            Mat = StandardScaler.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def StandardScaler_Partial_Fit(copy, with_mean, with_std, X, y):
    X = eval(X)
    if y == 'None' or y == '':
        y = None
    else:
        y = eval(y)
    try:
        StandardScaler = preprocessing.StandardScaler(copy, with_mean, with_std).partial_fit(X, y)
        mem['FitStandardScaler'] = StandardScaler
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# add_dummy_feature
# =============================================================================
        
def add_dummy_feature(X, value):
    X = eval(X)
    try:
        add_dummy_feature = preprocessing.add_dummy_feature(X, value)
        dtype = type(add_dummy_feature)
        if dtype == numpy.ndarray:
            add_dummy_feature = add_dummy_feature.tolist()
            return str(add_dummy_feature)
        else:
            Mat = add_dummy_feature.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
# =============================================================================
# binarize
# =============================================================================
        
def binarize(X, threshold, copy):
    X = eval(X)
    try:
        binarize = preprocessing.binarize(X, threshold, copy)
        dtype = type(binarize)
        if dtype == numpy.ndarray:
            binarize = binarize.tolist()
            return str(binarize)
        else:
            Mat = binarize.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

# =============================================================================
# label_binarize
# =============================================================================
        
def label_binarize(y, classes, neg_label, pos_label, sparse_output):
    y = eval(y)
    classes = eval(classes)
    try:
        label_binarize = preprocessing.label_binarize(y, classes, neg_label, pos_label, sparse_output)
        dtype = type(label_binarize)
        if dtype == numpy.ndarray:
            label_binarize = label_binarize.tolist()
            return str(label_binarize)
        else:
            Mat = label_binarize.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# maxabs_scale
# =============================================================================
        
def maxabs_scale(X, axis, copy):
    X = eval(X)
    try:
        maxabs_scale = preprocessing.maxabs_scale(X, axis, copy)
        dtype = type(maxabs_scale)
        if dtype == numpy.ndarray:
            maxabs_scale = maxabs_scale.tolist()
            return str(maxabs_scale)
        else:
            Mat = maxabs_scale.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# minmax_scale
# =============================================================================
        
def minmax_scale(X, n_min, n_max, axis_donne, copy_donne):
    X = eval(X)
    try:
        minmax_scale = preprocessing.minmax_scale(X, (n_min, n_max), axis = axis_donne, copy = copy_donne)
        minmax_scale  = minmax_scale.tolist()
        return str(minmax_scale)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# normalize
# =============================================================================
        
def normalize(X, norm, axis, copy, return_norm, returns):
    X = eval(X)
    try:
        normalize, norms = preprocessing.normalize(X, norm, axis, copy, return_norm)
        if returns == 'norms':
            norms  = norms.tolist()
            return str(normalize)
        else: 
            dtype = type(normalize)
            if dtype == numpy.ndarray:
                normalize = normalize.tolist()
                return str(normalize) 
            else:
                Mat = normalize.tocoo()
                return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# quantile_transform
# =============================================================================
        
def quantile_transform(X, axis, n_quantiles, output_distribution, ignore_implicit_zeros, subsample, random_state, copy):
    X = eval(X)
    if random_state == -1:
        random_state = None
    try:
        quantile_transform = preprocessing.quantile_transform(X, axis, n_quantiles, output_distribution, ignore_implicit_zeros, subsample, random_state, copy)
        dtype = type(quantile_transform)
        if dtype == numpy.ndarray:
            quantile_transform = quantile_transform.tolist()
            return str(quantile_transform) 
        else:
            Mat = quantile_transform.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# robust_scale
# =============================================================================
        
def robust_scale(X, axis, with_centering, with_scaling, q_min, q_max, copy):
    X = eval(X)
    try:
        robust_scale = preprocessing.robust_scale(X, axis, with_centering, with_scaling, (q_min, q_max), copy)
        dtype = type(robust_scale)
        if dtype == numpy.ndarray:
            robust_scale = robust_scale.tolist()
            return str(robust_scale) 
        else:
            Mat = robust_scale.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# scale
# =============================================================================
        
def scale(X, axis, with_mean, with_std, copy):
    X = eval(X)
    try:
        scale = preprocessing.scale(X, axis, with_mean, with_std, copy)
        dtype = type(scale)
        if dtype == numpy.ndarray:
            scale = scale.tolist()
            return str(scale) 
        else:
            Mat = scale.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# power_transform
# =============================================================================
        
def power_transform(X, method, standardize, copy):
    X = eval(X)
    try:
        power_transform = preprocessing.power_transform(X, method, standardize, copy)
        power_transform  = power_transform.tolist()
        return str(power_transform)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message