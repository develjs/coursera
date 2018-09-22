# pandas
# https://pandas.pydata.org/pandas-docs/stable/api.html#attributes-and-underlying-data
# http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
import numpy as np
import pandas
from sklearn.tree import DecisionTreeClassifier

# 1. 
data = pandas.read_csv('../titanic.csv',index_col='PassengerId') # 891
# print (data.columns)
count = data.shape[0]

# 2. select only Survived,Pclass,Fare,Age,Sex
data = data.filter(items=['Survived','Pclass','Fare','Age','Sex']) 

# 5. remove NaN
data = data.dropna(0)

# 4.
survived = np.array(data.filter(items=['Survived'])).T[0]
names = ['Pclass','Fare','Age','Sex']
data = data.filter(items=names)

# 6. 
def trans(item):
    return [
        int(item['Pclass']),
        int(100*item['Fare']),
        int(item['Age']),
        int(1 if item['Sex']=='male' else 0) 
    ]
data = data.apply(trans, axis=1).get_values()# np.array(, np.int)

def getLen(array):
    length = 0
    if type(array) is list:
        length = len(array)
    if type(array) is np.ndarray:
        length = array.shape[0]
    return length

def make_array(array): # [rows, cols]
    rows = getLen(array)
    cols = getLen(array[0])
    result = np.empty([0, cols], np.int)
    for i in range(rows):
        result = np.append(result, [array[i]], axis=0)
    return result

data = make_array(data)

#data = np.array(data.apply(trans, axis=1).get_values())

clf = DecisionTreeClassifier(random_state=241)
clf.fit(data, survived)

print names
print clf.feature_importances_
# importances.predict()

#print (data)
