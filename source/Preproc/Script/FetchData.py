# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:07:09 2020

@author: cipop
"""
import sys
from sklearn import datasets

def OlivettiFaces(data_home, shuffle, random_state, download_if_missing, return_X_y, returns):
    try:
        if data_home == 'None':
            data_home = None
        if random_state == -1:
            random_state = None
        olivetti_faces = datasets.fetch_olivetti_faces(data_home, shuffle, random_state, download_if_missing, return_X_y)
        if returns == 'Data':
            data = olivetti_faces['images'].tolist()
            return str(data)
        else :
            data = olivetti_faces['target'].tolist()
            return str(data)  
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

    
def NewsGroups(data_home, subset, categories, shuffle, random_state, remove, download_if_missing, return_X_y, returns):
    try:
        if data_home == 'None':
            data_home = None
        if categories[0] == 'None' or categories[0] == '':
            categories = None
        if random_state == -1:
            random_state = None
        remove = tuple(remove)
        NewsGroups = datasets.fetch_20newsgroups(data_home, subset, categories, shuffle, random_state, remove, download_if_missing, return_X_y)
        if returns == 'Data':
            data = NewsGroups['data']
            return str(data)
        else :
            data = NewsGroups['target'].tolist()
            return str(data)  
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('//!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def NewsGroupsVect(subset, remove, data_home, download_if_missing, return_X_y, normalize, returns):
    if data_home == 'None':
        data_home = None
    remove = tuple(remove)
    NewsGroups = datasets.fetch_20newsgroups_vectorized(subset, remove, data_home, download_if_missing, return_X_y, normalize)
    try:
        if returns == 'Data' :
            data = NewsGroups['data']
            Mat = data.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
        else :
            data = NewsGroups['target'].tolist()
            return str(data)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def LfwPeople(data_home, funneled, resize, min_faces_per_person, color, height1, width1, val1, height2, width2, val2, download_if_missing, return_X_y, returns):
    if data_home == 'None':
        data_home = None
    if val1 == 'None':
        val1 = None
    if val2 == 'None':
        val2 = None
    try:
        LfwPeople = datasets.fetch_lfw_people(data_home, funneled, resize, min_faces_per_person, color, (slice(height1, width1, val1), slice(height2, width2, val2)), download_if_missing, return_X_y)
        if returns == 'Data': 
            data = LfwPeople['images'].tolist()
            return str(data)
        else :
            data = LfwPeople['target'].tolist()
            return str(data)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    

def LfwPairs(subset, data_home, funneled, resize, color, height1, width1, val1, height2, width2, val2, download_if_missing, returns):
    if data_home == 'None':
        data_home = None
    if val1 == 'None':
        val1 = None
    if val2 == 'None':
        val2 = None
    try:
        LfwPairs = datasets.fetch_lfw_pairs(subset, data_home, funneled, resize, color, (slice(height1, width1, val1), slice(height2, width2, val2)), download_if_missing)
        if returns == 'Data': 
            data = LfwPairs['pairs'].tolist()
            return str(data)
        else :
            data = LfwPairs['target'].tolist()
            return str(data)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def Covtype(data_home, download_if_missing, random_state, shuffle, return_X_y, returns):
    if data_home == 'None':
        data_home = None
    if random_state == -1:
        random_state = None
    try:
        Covtype = datasets.fetch_covtype(data_home, download_if_missing, random_state, shuffle, return_X_y)
        if returns == 'Data' : 
            data = Covtype['data'].tolist()
            return str(data)
        else :
            data = Covtype['target'].tolist()
            return str(data)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

def Rcv1(data_home, subset, download_if_missing, random_state, shuffle, return_X_y, returns):
    if data_home == 'None':
        data_home = None
    if random_state == -1:
        random_state = None
    try:
        Rcv1 = datasets.fetch_rcv1(data_home, subset, download_if_missing, random_state, shuffle, return_X_y)
        if returns == 'Data': 
            data = Rcv1['data']
            Mat = data.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
        else :
            data = Rcv1['target']
            Mat = data.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
def Kddcup99(subset, data_home, shuffle, random_state, percent10, download_if_missing, return_X_y, returns):
    if subset == 'None':
        subset = None
    if data_home == 'None':
        data_home = None
    if random_state == -1:
        random_state = None
    try:
        Kddcup99 = datasets.fetch_kddcup99(subset, data_home, shuffle, random_state, percent10, download_if_missing, return_X_y)
        if returns == 'Data': 
            data = Kddcup99['data'].tolist()
            return str(data)
        else :
            data = Kddcup99['target'].tolist()
            return str(data)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

    
def CaliforniaHouse(data_home, download_if_missing, return_X_y, returns):
    if data_home == 'None':
        data_home = None
    try:
        CaliforniaHouse = datasets.fetch_california_housing(data_home, download_if_missing, return_X_y)
        if returns == 'Data' :
            data = CaliforniaHouse['data'].tolist()
            return str(data)
        else :
            data = CaliforniaHouse['target'].tolist()
            return str(data)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

    
