import tensorflow as tf
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.applications.densenet import preprocess_input

dir_p = "dataset/"
def dataset_yuklash(path):
    rasmlar = []
    holat = ["with_mask","without_mask"]
    for i in holat:
        for rasm_path in glob.glob(os.path.join(path,i,'*')):
            try:
                maskali = cv2.imread(rasm_path)
                maskali = cv2.cvtColor(maskali,cv2.COLOR_BGR2RGB)
                rasmlar.append((maskali,i))
            except:
                pass
    return rasmlar

maska = dataset_yuklash(dir_p)
random.shuffle(maska)

y_size = [i[0].shape[0] for i in maska]
x_size = [i[0].shape[1] for i in maska]
plt.plot(np.arange(1839),y_size,"r*")
plt.plot(np.arange(1839),x_size,"g*")

# Rasmlarni bir xil o'lchamga keltirish
def ulcham(maska):
    maska = cv2.resize(maska,(224,224))
    return maska

# Maska bor yoki yo'qligini binaryga o'tkazish
def holat(holatlar):
    if holatlar=="with_mask":
        holatlar=1
    else:
        holatlar = 0
    return holatlar

# Tayyor rasmlar
def tayyor_rasm(rasmlar):
    tayyor_rasmlar = []
    for i in rasmlar:
        tayyor_rasmlar.append((ulcham(i[0]),holat(i[1])))
    return tayyor_rasmlar

tayyor_rasmlar = tayyor_rasm(maska)
x_train = []
y_train = []
x_test = []
y_test = []
for i in range(len(tayyor_rasmlar)):
    if i < int(len(tayyor_rasmlar)*0.8):
        x_train.append(tayyor_rasmlar[i][0])        
        y_train.append(tayyor_rasmlar[i][1])
    else:
        x_test.append(tayyor_rasmlar[i][0])        
        y_test.append(tayyor_rasmlar[i][1])

# CNN

x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

x_train = preprocess_input(x_train)
x_test = preprocess_input(x_test)

bm = DenseNet121(include_top=False,input_shape=(224,224,3))

bm.trainable = False

model = Sequential([
    bm,
    Flatten(),
    Dense(1000,activation="relu"),
    Dense(100,activation="relu"),
    Dense(1,activation="sigmoid")
])

model.compile(optimizer="Adam",loss=tf.keras.losses.BinaryCrossentropy(),metrics=["accuracy"])
model.fit(x_train,y_train,batch_size=4,epochs=5)

model.evaluate(x_test,y_test)