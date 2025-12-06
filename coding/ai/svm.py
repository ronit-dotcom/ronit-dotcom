import pandas as pd
import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt

iris= datasets.load_iris()
x=iris.data[:, :2]
y=iris.target
C=1.0
x_min, x_max=x[:, 0].min()-1, x[:, 0].max()+1
y_min, x_max=x[:, 1].min()-1, x[:, 1].max()+1
h=(x_max/x_min)/100
xx, yy=np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, x_max, h))
x_plot=np.c_[xx.ravel(),yy.ravel()]

svc_classifier=svm.SVC(kernel='linear',C=C, decision_function_shape='ovr').fit(x, y)
z=svc_classifier.predict(x_plot)
z=z.reshape(xx.shape)

plt.figure(figsize=(15, 15))
plt.subplot(121)
plt.contourf(xx,yy,z,cmap=plt.cm.tab10, alpha=0.3)
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Set1)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernal')