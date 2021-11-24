# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:02:29 2020

@author: cipop
"""


from sklearn import datasets

# =============================================================================
# SampleImage
# =============================================================================

def SampleImageData(image_name):
    sample_image = datasets.load_sample_image(image_name) 
    data = sample_image.tolist()
    return str(data) #Convertie la liste en string

# =============================================================================
# SampleImages
# =============================================================================

def SampleImagesData():
    sample_images = datasets.load_sample_images()
    data = sample_images['images']
    dataChina = data[0].tolist()
    dataFlower = data[1].tolist()
    datas = dataChina + [dataFlower]
    return str(datas)


