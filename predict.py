# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:24:19 2021

@author: vinic_000
"""

from models import Yolov4

model = Yolov4(weight_path='yolov4.weights', 
               class_name_path='class_names/coco_classes.txt')

model.predict('img/pessoas.png')
model.predict('img/vaca.png')
model.predict('img/cavalo.png')
model.predict('img/escola.jpg')
model.predict('img/kite.jpg')
