import numpy as np
from sklearn import preprocessing
input_labels=['yellow','black','blue','purple','red','green']
encoder=preprocessing.LabelEncoder()
encoder.fit(input_labels)

test_labels=['green','black','blue']
encoded_values=encoder.transform(test_labels)
print('Labels:',test_labels)
print('encoded labeles:',encoded_values)

encoded_values=[4,5,2]
decoded_list=encoder.inverse_transform(encoded_values)
print('encoded values:',encoded_values)
print('decoded values:',decoded_list)