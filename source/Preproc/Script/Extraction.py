# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:09:21 2020

@author: cipop
"""

import sys
from sklearn import feature_extraction
import numpy
import numpy as np
from scipy import sparse


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
# DictVectorizer
# =============================================================================

def DictVectorizerFit(dtype, separator, sparse_bool, sort, X):
    dtype = TypeVar(dtype) 
    X = eval(X)
    try:
        DictVectorizer = feature_extraction.DictVectorizer(dtype, separator, sparse_bool, sort).fit(X)
        mem['FitDictVectorizer'] = DictVectorizer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def DictVectorizerFitTransform(dtype, separator, sparse_bool, sort, X):
    dtype = TypeVar(dtype)   
    X = eval(X)
    try:
        DictVectorizer = feature_extraction.DictVectorizer(dtype, separator, sparse_bool, sort).fit_transform(X)
        dtype = type(DictVectorizer)
        if dtype == numpy.ndarray:
            DictVectorizer = DictVectorizer.tolist()
            return str(DictVectorizer)
        else:
            Mat = DictVectorizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def DictVectorizerGetFeatureNames(dtype, separator, sparse_bool, sort, X):
    dtype = TypeVar(dtype)    
    try:
        DictVectorizer = feature_extraction.DictVectorizer(dtype, separator, sparse_bool, sort).get_feature_names()
        return str(DictVectorizer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def DictVectorizerTransform(dtype, separator, sparse_bool, sort, X):
    dtype = TypeVar(dtype)    
    X = eval(X)
    try:
        DictVectorizerTransform = mem['FitDictVectorizer'].transform(X)
        dtype = type(DictVectorizerTransform)
        if dtype == numpy.ndarray:
            DictVectorizerTransform = DictVectorizerTransform.tolist()
            return str(DictVectorizerTransform)
        else:
            Mat = DictVectorizerTransform.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    

# =============================================================================
# FeatureHasher
# =============================================================================

def FeatureHasherFit(n_features, input_type, dtype, alternate_sign, X, Y):
    dtype = TypeVar(dtype) 
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        FeatureHasher = feature_extraction.FeatureHasher(n_features, input_type, dtype, alternate_sign).fit(X, Y)
        mem['FitFeatureHasher'] = FeatureHasher
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def FeatureHasherFitTransform(n_features, input_type, dtype, alternate_sign, X, Y):
    dtype = TypeVar(dtype)   
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        FeatureHasher = feature_extraction.FeatureHasher(n_features, input_type, dtype, alternate_sign).fit_transform(X, Y)
        dtype = type(FeatureHasher)
        if dtype == numpy.ndarray:
            FeatureHasher = FeatureHasher.tolist()
            return str(FeatureHasher)
        else:
            Mat = FeatureHasher.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def FeatureHasherTransform(n_features, input_type, dtype, alternate_sign, X, Y):
    dtype = TypeVar(dtype)    
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        FeatureHasher = mem['FitFeatureHasher'].transform(X, Y)
        dtype = type(FeatureHasher)
        if dtype == numpy.ndarray:
            FeatureHasher = FeatureHasher.tolist()
            return str(FeatureHasher)
        else:
            Mat = FeatureHasher.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# Extract_Patches_2D
# =============================================================================

def Patches2D( image, patch_height, patch_width, max_patches, random_state):
    if max_patches == '' or max_patches == 'None':
        max_patches = None
    else:
        max_patches = eval(max_patches)
    if random_state == -1:
        random_state = None   
    image = eval(image)
    imagearray = np.array(image)
    try:
        Patches2D = feature_extraction.image.extract_patches_2d(imagearray, (patch_height, patch_width), max_patches, random_state)
        Patches2Dlist = Patches2D.tolist()
        return str(Patches2Dlist)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message


# =============================================================================
# Reconstruct_from_patches_2d
# =============================================================================
        
def ReconstructFromPatches2D(patches, image_height, image_width):  
    try:
        Patches2D = feature_extraction.image.reconstruct_from_patches_2d(patches, (image_height, image_width))
        return str(Patches2D)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# PatchExtractor
# =============================================================================

def PatchExtractorFit(patch_height, patch_width, max_patches, random_state, image):  
    if max_patches == '' or max_patches == 'None':
        max_patches = None
    else:
        max_patches = eval(max_patches)
    if random_state == -1:
        random_state = None 
    image = np.array(image)
    try:
        PatchExtractor = feature_extraction.image.PatchExtractor((patch_height, patch_width), max_patches, random_state).fit(image)
        mem['FitPatchExtractor'] = PatchExtractor
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def PatchExtractorTransform(patch_height, patch_width, max_patches, random_state, image):  
    if max_patches == '' or max_patches == 'None':
        max_patches = None
    else:
        max_patches = eval(max_patches)
    if random_state == -1:
        random_state = None 
    image = np.array(image)
    try:
        Patches2D = mem['FitPatchExtractor'].transform(image)
        Patches2Dlist = Patches2D.tolist()
        return str(Patches2Dlist)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# CountVectorizer
# =============================================================================

def CountVectorizerFit(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, list_stop_words, token_pattern, min_n, max_n, analyzer, max_df, min_df, max_features, vocabulary, binary, dtype, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype)
    list_analyzer = ['word', 'char', 'char_wb']
    if vocabulary == 'None':
        vocabulary = None
    else:
        vocabulary = eval(vocabulary)
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if max_features == -1:
        max_features = None
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer)  
    try:
        CountVectorizer = feature_extraction.text.CountVectorizer(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, token_pattern, (min_n, max_n), analyzer, max_df, min_df, max_features, vocabulary, binary, dtype).fit(X)
        mem['FitCountVectorizer'] = CountVectorizer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def CountVectorizerFitTransform(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, list_stop_words, token_pattern, min_n, max_n, analyzer, max_df, min_df, max_features, vocabulary, binary, dtype, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype)
    list_analyzer = ['word', 'char', 'char_wb']
    if vocabulary == 'None':
        vocabulary = None
    else:
        vocabulary = eval(vocabulary)
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if max_features == -1:
        max_features = None
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer)  
    try:
        CountVectorizer = feature_extraction.text.CountVectorizer(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, token_pattern, (min_n, max_n), analyzer, max_df, min_df, max_features, vocabulary, binary, dtype).fit_transform(X)
        dtype = type(CountVectorizer)
        if dtype == numpy.ndarray:
            CountVectorizer = CountVectorizer.tolist()
            return str(CountVectorizer)
        else:
            Mat = CountVectorizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def CountVectorizerTransform(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, list_stop_words, token_pattern, min_n, max_n, analyzer, max_df, min_df, max_features, vocabulary, binary, dtype, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype)
    list_analyzer = ['word', 'char', 'char_wb']
    if vocabulary == 'None':
        vocabulary = None
    else:
        vocabulary = eval(vocabulary)
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if max_features == -1:
        max_features = None
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer)     
    try:
        CountVectorizer = mem['FitCountVectorizer'].transform(X)
        dtype = type(CountVectorizer)
        if dtype == numpy.ndarray:
            CountVectorizer = CountVectorizer.tolist()
            return str(CountVectorizer)
        else:
            Mat = CountVectorizer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def CountVectorizerGetFeat(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, list_stop_words, token_pattern, min_n, max_n, analyzer, max_df, min_df, max_features, vocabulary, binary, dtype, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype)
    list_analyzer = ['word', 'char', 'char_wb']
    if vocabulary == 'None':
        vocabulary = None
    else:
        vocabulary = eval(vocabulary)
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if max_features == -1:
        max_features = None
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer)    
    try:
        CountVectorizer = feature_extraction.text.CountVectorizer(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, token_pattern, (min_n, max_n), analyzer, max_df, min_df, max_features, vocabulary, binary, dtype).get_feature_names()
        return str(CountVectorizer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def CountVectorizerDecode(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, list_stop_words, token_pattern, min_n, max_n, analyzer, max_df, min_df, max_features, vocabulary, binary, dtype, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype)
    list_analyzer = ['word', 'char', 'char_wb']
    if vocabulary == 'None':
        vocabulary = None
    else:
        vocabulary = eval(vocabulary)
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if max_features == -1:
        max_features = None
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer)   
    try:
        CountVectorizer = feature_extraction.text.CountVectorizer(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, token_pattern, (min_n, max_n), analyzer, max_df, min_df, max_features, vocabulary, binary, dtype).decode(doc)
        return str(CountVectorizer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# HashingVectorizer
# =============================================================================

def HashingVectorizerFit(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, list_stop_words, token_pattern, min_n, max_n, analyzer, n_features, binary, norm, alternate_sign, dtype, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype)
    list_analyzer = ['word', 'char', 'char_wb']
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer) 
    try:
        HashingVectorizer = feature_extraction.text.HashingVectorizer(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, token_pattern, (min_n, max_n), analyzer, n_features, binary, norm, alternate_sign, dtype).fit(X)
        mem['FitHashingVectorizer'] = HashingVectorizer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def HashingVectorizerFitTransform(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, list_stop_words, token_pattern, min_n, max_n, analyzer, n_features, binary, norm, alternate_sign, dtype, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype)
    list_analyzer = ['word', 'char', 'char_wb']
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer) 
    try:
        HashingVectorizer = feature_extraction.text.HashingVectorizer(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, token_pattern, (min_n, max_n), analyzer, n_features, binary, norm, alternate_sign, dtype).fit_transform(X)
        Mat = HashingVectorizer.tocoo()
        return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def HashingVectorizerTransform(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, list_stop_words, token_pattern, min_n, max_n, analyzer, n_features, binary, norm, alternate_sign, dtype, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype)
    list_analyzer = ['word', 'char', 'char_wb']
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer) 
    try:
        HashingVectorizer = mem['FitHashingVectorizer'].transform(X)
        Mat = HashingVectorizer.tocoo()
        return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def HashingVectorizerDecode(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, list_stop_words, token_pattern, min_n, max_n, analyzer, n_features, binary, norm, alternate_sign, dtype, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype)
    list_analyzer = ['word', 'char', 'char_wb']
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer) 
    try:
        HashingVectorizer = feature_extraction.text.HashingVectorizer(input_, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, stop_words, token_pattern, (min_n, max_n), analyzer, n_features, binary, norm, alternate_sign, dtype).decode(doc)
        return str(HashingVectorizer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# TfidfTransformer
# =============================================================================

def TfidfTransformerFit(norm, use_idf, smooth_idf, sublinear_tf, X, Y):
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        TfidfTransformer = feature_extraction.text.TfidfTransformer(norm, use_idf, smooth_idf, sublinear_tf).fit(X, Y)
        mem['FitTfidfTransformer'] = TfidfTransformer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def TfidfTransformerFitTransform(norm, use_idf, smooth_idf, sublinear_tf, X, Y):
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        TfidfTransformer = feature_extraction.text.TfidfTransformer(norm, use_idf, smooth_idf, sublinear_tf).fit_transform(X, Y)
        dtype = type(TfidfTransformer)
        if dtype == numpy.ndarray:
            TfidfTransformer = TfidfTransformer.tolist()
            return str(TfidfTransformer)
        else:
            Mat = TfidfTransformer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def TfidfTransformerTransform(norm, use_idf, smooth_idf, sublinear_tf, X, Y):
    X = eval(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
    try:
        TfidfTransformer = mem['FitTfidfTransformer'].transform(X, Y)
        dtype = type(TfidfTransformer)
        if dtype == numpy.ndarray:
            TfidfTransformer = TfidfTransformer.tolist()
            return str(TfidfTransformer)
        else:
            Mat = TfidfTransformer.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

# =============================================================================
# TfidfVectorizer
# =============================================================================

def TfidfVectorizerFit(input, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, analyzer, stop_words, list_stop_words, token_pattern, min_n, max_n, max_df, min_df, max_features, vocabulary, binary, dtype, norm, use_idf, smooth_idf, sublinear_tf, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype) 
    list_analyzer = ['word', 'char', 'char_wb']
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if norm == 'None':
        norm = None
    if max_features == -1:
        max_features = None
    if vocabulary == 'None':
        vocabulary = None
    else:
        vocabulary = eval(vocabulary)
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer) 
    try:
        TfidfVectorizer = feature_extraction.text.TfidfVectorizer(input, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, analyzer, stop_words, token_pattern, (min_n, max_n), max_df, min_df, max_features, vocabulary, binary, dtype, norm, use_idf, smooth_idf, sublinear_tf).fit(X)
        mem['FitTfidfVectorizer'] = TfidfVectorizer
        return str('OK')
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def TfidfVectorizerFitTransform(input, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, analyzer, stop_words, list_stop_words, token_pattern, min_n, max_n, max_df, min_df, max_features, vocabulary, binary, dtype, norm, use_idf, smooth_idf, sublinear_tf, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype) 
    list_analyzer = ['word', 'char', 'char_wb']
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if norm == 'None':
        norm = None
    if max_features == -1:
        max_features = None
    if vocabulary == 'None':
        vocabulary = None
    else:
        vocabulary = eval(vocabulary)
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer) 
    try:
        TfidfVectorizer = feature_extraction.text.TfidfVectorizer(input, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, analyzer, stop_words, token_pattern, (min_n, max_n), max_df, min_df, max_features, vocabulary, binary, dtype, norm, use_idf, smooth_idf, sublinear_tf).fit_transform(X)
        Mat = TfidfVectorizer.tocoo()
        return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 
    
def TfidfVectorizerTransform(input, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, analyzer, stop_words, list_stop_words, token_pattern, min_n, max_n, max_df, min_df, max_features, vocabulary, binary, dtype, norm, use_idf, smooth_idf, sublinear_tf, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype) 
    list_analyzer = ['word', 'char', 'char_wb']
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if norm == 'None':
        norm = None
    if max_features == -1:
        max_features = None
    if vocabulary == 'None':
        vocabulary = None
    else:
        vocabulary = eval(vocabulary)
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer) 
    try:
        TfidfVectorizer = mem['FitTfidfVectorizer'].transform(X)
        Mat = TfidfVectorizer.tocoo()
        return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def TfidfVectorizerDecode(input, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, analyzer, stop_words, list_stop_words, token_pattern, min_n, max_n, max_df, min_df, max_features, vocabulary, binary, dtype, norm, use_idf, smooth_idf, sublinear_tf, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype) 
    list_analyzer = ['word', 'char', 'char_wb']
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if norm == 'None':
        norm = None
    if max_features == -1:
        max_features = None
    if vocabulary == 'None':
        vocabulary = None
    else:
        vocabulary = eval(vocabulary)
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer) 
    try:
        TfidfVectorizer = feature_extraction.text.TfidfVectorizer(input, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, analyzer, stop_words, token_pattern, (min_n, max_n), max_df, min_df, max_features, vocabulary, binary, dtype, norm, use_idf, smooth_idf, sublinear_tf).decode(doc)
        return str(TfidfVectorizer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def TfidfVectorizerFeatNames(input, encoding, decode_error, strip_accents, lowercase, preprocessor, tokenizer, analyzer, stop_words, list_stop_words, token_pattern, min_n, max_n, max_df, min_df, max_features, vocabulary, binary, dtype, norm, use_idf, smooth_idf, sublinear_tf, X, doc):
    X = eval(X)
    dtype = TypeVar(dtype) 
    list_analyzer = ['word', 'char', 'char_wb']
    if tokenizer == 'None' or tokenizer == '':
        tokenizer = None
    else:
        tokenizer = eval(tokenizer)
    if preprocessor == 'None' or preprocessor == '':
        preprocessor = None
    else:
        preprocessor = eval(preprocessor)
    if strip_accents == 'None':
        strip_accents = None
    if stop_words == 'None':
        stop_words = None
    elif stop_words == 'list':
        stop_words = list_stop_words
    else: 
        pass
    if norm == 'None':
        norm = None
    if max_features == -1:
        max_features = None
    if vocabulary == 'None':
        vocabulary = None
    else:
        vocabulary = eval(vocabulary)
    if analyzer not in list_analyzer:
        analyzer = eval(analyzer) 
    try:
        TfidfVectorizer = mem['FitTfidfVectorizer'].get_feature_names()
        return str(TfidfVectorizer)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message