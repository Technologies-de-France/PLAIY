# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:54:55 2020

@author: cipop
"""


from sklearn import datasets

def BostonFeatureNames():
    boston = datasets.load_boston() 
    feature_names = boston['feature_names'].tolist() # converti les datas en une liste
    feature_names.append('MEDV') # ajoute la feature name target a la liste
    return str(feature_names) #Convertie la liste en string

def BostonData():
    boston = datasets.load_boston() 
    data = boston['data'].tolist() # converti les datas en une liste
    return str(data) #Convertie la liste en string

def BostonTarget():
    boston = datasets.load_boston() 
    data_target = boston['target'].tolist() # converti les datas en une liste
    return str(data_target) #Convertie la liste en string

def IrisFeatureNames():
    iris = datasets.load_iris()
    feature_names = iris['feature_names'] + ['Setosa/Versicolore/Virginica']
    return str(feature_names)

def IrisData():
    iris = datasets.load_iris()
    data = iris['data'].tolist()
    return str(data)

def IrisTarget():
    iris = datasets.load_iris()
    data_target = iris['target'].tolist()
    return str(data_target)

def DiabetesFeatureNames():
    diabetes = datasets.load_diabetes() 
    feature_names = diabetes['feature_names'] + ['progression']
    return str(feature_names) #Convertie la liste en string

def DiabetesData():
    diabetes = datasets.load_diabetes() 
    data = diabetes['data'].tolist() # converti les datas en une liste
    return str(data) #Convertie la liste en string

def DiabetesTarget():
    diabetes = datasets.load_diabetes() 
    data_target = diabetes['target'].tolist() # converti les datas en une liste
    return str(data_target) #Convertie la liste en string

def LinnerudFeatureNames():
    linnerud = datasets.load_linnerud() 
    feature_names = linnerud['feature_names'] + linnerud['target_names']
    return str(feature_names) #Convertie la liste en string
    
def LinnerudData():
    linnerud = datasets.load_linnerud() 
    data = linnerud['data'].tolist() # converti les datas en une liste
    return str(data) #Convertie la liste en string

def LinnerudTarget():
    linnerud = datasets.load_linnerud() 
    data_target = linnerud['target'].tolist() # converti les datas en une liste
    return str(data_target) #Convertie la liste en string

def WineFeatureNames():
    wine = datasets.load_wine() 
    feature_names = wine['feature_names'] + ['Vin1/Vin2/Vin3']
    return str(feature_names) #Convertie la liste en string

def WineData():
    wine = datasets.load_wine() 
    data = wine['data'].tolist() # converti les datas en une liste
    return str(data) #Convertie la liste en string

def WineTarget():
    wine = datasets.load_wine() 
    data_target = wine['target'].tolist() # converti les datas en une liste
    return str(data_target) #Convertie la liste en string

def BreastCancerFeatureNames():
    breast_cancer = datasets.load_breast_cancer() 
    feature_names = breast_cancer['feature_names'].tolist() # converti les datas en une liste
    feature_names = feature_names + ['Malin/Bénin'] # ajoute la feature name target a la liste
    return str(feature_names) #Convertie la liste en string

def BreastCancerData():
    breast_cancer = datasets.load_breast_cancer() 
    data = breast_cancer['data'].tolist() # converti les datas en une liste
    return str(data) #Convertie la liste en string

def BreastCancerTarget():
    breast_cancer = datasets.load_breast_cancer() 
    data_target = breast_cancer['target'].tolist() # converti les datas en une liste
    return str(data_target) #Convertie la liste en string

def DigitsData():
    digits = datasets.load_digits() 
    data = digits['images'].tolist() # converti les datas en une liste
    return str(data) #Convertie la liste en string

