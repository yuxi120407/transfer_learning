# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:43:16 2018

@author: yuxi
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt  
import math 
from mpl_toolkits.mplot3d import Axes3D
import textwrap
import glob
from skimage.io import imread  
#%%
def get_labeled_data(txtName,imageName):
    txt_name = glob.glob(str('./')+txtName+str('/*.txt'))
    data = np.zeros([1,3])
    for name in txt_name: 
        image_name = name.split("\\")[1]
        image_name = image_name.split(".")[0]
        path_txt = str('./')+txtName+str('/')+image_name+str('.txt')
        path_image =  str('./')+imageName+str('/')+image_name+str('.jpg')
    
        txtfile = open(path_txt)
        firstline = txtfile.readlines()[2:] 
        txtfile.close()
        image = imread(path_image)
        all_data = np.zeros([50,3])
        for i in range(50):
            
            test_file = firstline[i].split(",")
            point_x = int(test_file[0])
            point_y = int(test_file[1])
            label = int(test_file[2])
            all_data[i,:]=image[point_y,point_x]
        data = np.vstack((data,all_data))
    real_data = data[1:]
    return real_data,label
#%%
data_2015,_ = get_labeled_data('2015new - Copy','2015image')
data_2014,_ = get_labeled_data('2014_new - Copy','2014image')
data_2013,_ = get_labeled_data('2013new - Copy','2013image')
data_2012,_ = get_labeled_data('2012_new','2012image')
data_2017,_ = get_labeled_data('2017new','2017image')
#%%
#plot results
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(*[1,1,1], projection= '3d')
#ax.scatter(data_2017[:,0],data_2017[:,1],data_2017[:,2],color = 'blue')
#ax.scatter(x_src_tca[:,0],x_src_tca[:,1],x_src_tca[:,2],color = 'blue')
#ax.scatter(real_data_2013[:,0],real_data_2013[:,1],real_data_2013[:,2],color = 'red')
#ax.scatter(data_2014[:,0],data_2014[:,1],data_2014[:,2],color = 'yellow')
#ax.scatter(data_2015[:,0],data_2015[:,1],data_2015[:,2],color = 'green')
#ax.scatter(real_data_2017[:,0],real_data_2017[:,1],real_data_2017[:,2],color = 'blue')
#ax.scatter(image_test[:,0],image_test[:,1],image_test[:,2],color = 'green')
#ax.scatter(0,0,255,color='red')
myTitle = 'Pulley ridge IV'
ax.set_title("\n".join(textwrap.wrap(myTitle, 20)))
#%%

