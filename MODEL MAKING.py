import pandas as pd
import numpy as np
import pickle
data_train = pd.read_csv('dataset.csv')
data_test = [['3','0','0']]
# print(data_train)
# print(data_test)
label_train = data_train['total'].to_numpy()
fitur_train = data_train[['jumlah kedip', 'jumlah kepala miring', 'jumlah menguap']].to_numpy()
# print(fitur_train)
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(fitur_train, label_train, random_state=0)
from sklearn.svm import LinearSVC
svc = LinearSVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
accuracy = (tn + tp) / (tn + fp + fn + tp)
recall = tp / (tp+fn)
precission = tp / (tp+fp)
print("Akurasi :",accuracy)
print("Presisi :",precission)
print("Recall  :",recall)
fitur_test = data_test['jumlah kedip','jumlah kepala miring','jumlah menguap']

y_pred_test = svc.predict(fitur_test)


import pickle
filename = 'ngantuk_modelup'
pickle.dump(svc,open(filename,'wb'))
loaded_model = pickle.load(open(filename,'rb'))
