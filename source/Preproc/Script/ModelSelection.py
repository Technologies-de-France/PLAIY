# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:55:03 2020

@author: cipop
"""



import sys
from sklearn import model_selection
import numpy as np
import numpy

mem = {}

# =============================================================================
# train_test_split
# =============================================================================

def X_TRAIN(X, y, val_test_size, val_train_size, val_random_state, val_shuffle, val_stratify):
    if len(val_stratify) == 0:
        val_stratify = None
    X = eval(X)
    y = eval(y)
    if val_test_size == -1:
        val_test_size = None
    if val_train_size == -1:
        val_train_size = None
    if val_random_state == -1:
        val_random_state = None
    try:
        X_train, X_test, y_train, y_test= model_selection.train_test_split(X, y, test_size=val_test_size, train_size=val_train_size, random_state=val_random_state, shuffle=val_shuffle, stratify=val_stratify)
        return str(X_train)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message 

def X_TEST(X, y, val_test_size, val_train_size, val_random_state, val_shuffle, val_stratify):
    if len(val_stratify) == 0:
        val_stratify = None
    X = eval(X)
    y = eval(y)
    if val_test_size == -1:
        val_test_size = None
    if val_train_size == -1:
        val_train_size = None
    if val_random_state == -1:
        val_random_state = None
    try:
        X_train, X_test, y_train, y_test= model_selection.train_test_split(X, y, test_size=val_test_size, train_size=val_train_size, random_state=val_random_state, shuffle=val_shuffle, stratify=val_stratify)
        return str(X_test)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def Y_TRAIN(X, y, val_test_size, val_train_size, val_random_state, val_shuffle, val_stratify):
    if len(val_stratify) == 0:
        val_stratify = None
    X = eval(X)
    y = eval(y)
    if val_test_size == -1:
        val_test_size = None
    if val_train_size == -1:
        val_train_size = None
    if val_random_state == -1:
        val_random_state = None
    try:
        X_train, X_test, y_train, y_test= model_selection.train_test_split(X, y, test_size=val_test_size, train_size=val_train_size, random_state=val_random_state, shuffle=val_shuffle, stratify=val_stratify)
        return str(y_train)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def Y_TEST(X, y, val_test_size, val_train_size, val_random_state, val_shuffle, val_stratify):
    if len(val_stratify) == 0:
        val_stratify = None
    X = eval(X)
    y = eval(y)
    if val_test_size == -1:
        val_test_size = None
    if val_train_size == -1:
        val_train_size = None
    if val_random_state == -1:
        val_random_state = None
    try:
        X_train, X_test, y_train, y_test= model_selection.train_test_split(X, y, test_size=val_test_size, train_size=val_train_size, random_state=val_random_state, shuffle=val_shuffle, stratify=val_stratify)
        return str(y_test)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# GroupKFold
# =============================================================================


def GroupKFold_Split(n_splits, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    list_return = []
    try:
        for train_index, test_index in model_selection.GroupKFold(n_splits).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# GroupShuffleSplit
# =============================================================================


def GroupShuffleSplit_Split(n_splits, test_size, train_size, random_state, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    if test_size == 'None':
        test_size = None
    else:
         test_size = eval(test_size)
    if train_size == 'None':
        train_size = None
    else:
         train_size = eval(train_size)
    if random_state == -1:
        random_state = None
    list_return = []
    try:
        for train_index, test_index in model_selection.GroupShuffleSplit(n_splits, test_size, train_size, random_state).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# KFold
# =============================================================================


def KFold_Split(n_splits, shuffle, random_state, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    if random_state == -1:
        random_state = None
    list_return = []
    try:
        for train_index, test_index in model_selection.KFold(n_splits, shuffle, random_state).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# LeaveOneGroupOut
# =============================================================================


def LeaveOneGroupOut_Split(X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    list_return = []
    try:
        for train_index, test_index in model_selection.LeaveOneGroupOut().split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# LeavePOut
# =============================================================================


def LeavePOut_Split(p, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    list_return = []
    try:
        for train_index, test_index in model_selection.LeavePOut(p).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# LeavePGroupsOut
# =============================================================================


def LeavePGroupsOut_Split(n_groups, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    list_return = []
    try:
        for train_index, test_index in model_selection.LeavePGroupsOut(n_groups).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# LeaveOneOut
# =============================================================================


def LeaveOneOut_Split(X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    list_return = []
    try:
        for train_index, test_index in model_selection.LeaveOneOut().split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# PredefinedSplit
# =============================================================================


def PredefinedSplit_Split(test_fold, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    list_return = []
    try:
        for train_index, test_index in model_selection.PredefinedSplit(test_fold).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# RepeatedKFold
# =============================================================================


def RepeatedKFold_Split(n_splits, n_repeats, random_state, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    if random_state == -1:
        random_state = None
    list_return = []
    try:
        for train_index, test_index in model_selection.RepeatedKFold(n_splits, n_repeats, random_state).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# RepeatedStratifiedKFold
# =============================================================================


def RepeatedStratifiedKFold_Split(n_splits, n_repeats, random_state, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    if random_state == -1:
        random_state = None
    list_return = []
    try:
        for train_index, test_index in model_selection.RepeatedStratifiedKFold(n_splits, n_repeats, random_state).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# ShuffleSplit
# =============================================================================


def ShuffleSplit_Split(n_splits, test_size, train_size, random_state, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    if test_size == 'None':
        test_size = None
    else:
         test_size = eval(test_size)
    if train_size == 'None':
        train_size = None
    else:
         train_size = eval(train_size)
    if random_state == -1:
        random_state = None
    list_return = []
    try:
        for train_index, test_index in model_selection.ShuffleSplit(n_splits, test_size, train_size, random_state).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

# =============================================================================    
# StratifiedKFold
# =============================================================================


def StratifiedKFold_Split(n_splits, shuffle, random_state, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    if random_state == -1:
        random_state = None
    list_return = []
    try:
        for train_index, test_index in model_selection.StratifiedKFold(n_splits, shuffle, random_state).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# StratifiedShuffleSplit
# =============================================================================


def StratifiedShuffleSplit_Split(n_splits, test_size, train_size, random_state, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    if test_size == 'None':
        test_size = None
    else:
         test_size = eval(test_size)
    if train_size == 'None':
        train_size = None
    else:
         train_size = eval(train_size)
    if random_state == -1:
        random_state = None
    list_return = []
    try:
        for train_index, test_index in model_selection.StratifiedShuffleSplit(n_splits, test_size, train_size, random_state).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# TimeSeriesSplit
# =============================================================================


def TimeSeriesSplit_Split(n_splits, max_train_size, X, Y, groups):
    X = eval(X)
    X = np.array(X)
    if Y == '':
        Y = None
    else:
        Y = eval(Y)
        Y = np.array(Y)
    if groups == '':
        groups = None
    else:
        groups = eval(groups)
        groups = np.array(groups)
    if max_train_size == 'None':
        max_train_size = None
    else:
         max_train_size = eval(max_train_size)
    list_return = []
    try:
        for train_index, test_index in model_selection.TimeSeriesSplit(n_splits, max_train_size).split(X, Y, groups):
            list_return = list_return +["TRAIN:", train_index.tolist(), "TEST:", test_index.tolist()]
            X_train, X_test = X[train_index].tolist(), X[test_index].tolist()
            y_train, y_test = Y[train_index].tolist(), Y[test_index].tolist()
            list_return = list_return +["X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test]
        return str(list_return)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# ParameterGrid
# =============================================================================

def ParameterGrid(param_grid):
    param_grid = eval(param_grid)
    try:
        ParameterGrid = model_selection.ParameterGrid(param_grid)
        ParameterGrid = list(ParameterGrid)
        return str(ParameterGrid)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# ParameterSampler
# =============================================================================  

def ParameterSampler(param_distributions, n_iter, random_state):
    param_distributions = eval(param_distributions)
    if random_state == -1:
        random_state = None
    try:
        ParameterSampler = model_selection.ParameterSampler(param_distributions, n_iter, random_state)
        ParameterSampler = list(ParameterSampler)
        return str(ParameterSampler)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message