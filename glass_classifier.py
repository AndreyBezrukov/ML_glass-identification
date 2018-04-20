import numpy as np
import sklearn

#importing the data

x_data = np.loadtxt('glass.data', delimiter=",", usecols=(1,2,3,4,5,6,7,8,9)) # RI, Na, Mg, Al, Si, K, Ca, Ba, Fe
y_data_raw = np.loadtxt('glass.data', delimiter=",", usecols=(10))            # 7 types of glass

#re-grouping glass types in 3 categories: float processed, non-float processed, Non-window glass

for i in range(0, len(y_data)):
    if y_data_raw[i]==1:  # float processed 
        y_data[i] = 1
    if y_data_raw[i]==2:  # float processed 
        y_data[i] = 1
    if y_data_raw[i]==3:  # non-float processed
        y_data[i] = 2
    if y_data_raw[i]==4:  # non-float processed
        y_data[i] = 2
    if y_data_raw[i]==5:  # Non-window glass
        y_data[i] = 3
    if y_data_raw[i]==6:  # Non-window glass
        y_data[i] = 3
    if y_data_raw[i]==7:  # Non-window glass
        y_data[i] = 3

#sptit the dataset to train and test parts

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.5)

#first classifier option

from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

# second classifier option

#from sklearn.neighbors import KNeighborsClassifier
#my_classifier = KNeighborsClassifier()

my_classifier.fit(x_train, y_train)

predictions = my_classifier.predict(x_test)

print "output test data:"
print y_test
print "output prediction:"
print predictions

from sklearn.metrics import accuracy_score

print "accuracy of prediction:"
print accuracy_score(y_test, predictions)

print "accuracy of random prediction:"
import random
y_randomtest = []
for i in range(0, len(y_test)):
    y_randomtest.append(random.randint(1, 3))
print accuracy_score(y_test, y_randomtest)

print "accuracy of prediction that all glass samples are float processed (type 1):"
y_only1test = []
for i in range(0, len(y_test)):
    y_only1test.append(1)
print accuracy_score(y_test, y_only1test)