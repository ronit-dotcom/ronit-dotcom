import numpy as np
from sklearn import preprocessing

input_data=np.array([[2.9 , 0.4 , -0.7],
                     [6.3 , 4.2 , 0.6],
                     [-5.8 , 5.2 , -3.7],
                     [-9.1 , 1.3 , 2.3]])
data_binarized=preprocessing.Binarizer(threshold=0.25).transform(input_data)
print('\n Binarized Data:\n',data_binarized)

print('mean=',input_data.mean(axis=0))
print('std deviation=',input_data.std(axis=0))

data_scaled=preprocessing.scale(input_data)
print('mean=',data_scaled.mean(axis=0))
print('std deviation=',data_scaled.std(axis=0))

data_scaler_minmax=preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax=data_scaler_minmax.fit_transform(input_data)
print('\n MinMax scaled data:\n',data_scaled_minmax)

data_normalize_L1=preprocessing.normalize(input_data, norm='l1')
print('L1 normalzed data:\n',data_normalize_L1)

data_normalize_L2=preprocessing.normalize(input_data, norm='l2')
print('L2 normalized data:\n',data_normalize_L2)