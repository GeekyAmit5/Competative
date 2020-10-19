import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from sklearn import tree


# reading data from csv
# df = pd.read_csv('steam.csv')
# print(df.shape)
# print(df.describe())
# print(df.values)

# loading csv file and diving input and output
# music_data = pd.read_csv('music.csv')
# x = music_data.drop(columns=['genre'])
# y = music_data['genre']

# making model and predicting
# model = DecisionTreeClassifier()
# model.fit(x,y)
# predictions = model.predict([[21, 1], [22, 0]])
# print(predictions)

# training and testing the model
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# model = DecisionTreeClassifier()
# model.fit(x_train, y_train)
# predictions = model.predict(x_test)
# score = accuracy_score(y_test, predictions)
# print(score)

# saving the trained model so that we do not have to retrain
# model = DecisionTreeClassifier()
# model.fit(x, y)
# joblib.dump(model, 'music_recommender.joblib')

# accessing the trained model
# model = joblib.load('music_recommender.joblib')
# predictions = model.predict([[21, 1], [22, 0]])
# print(predictions)

# see the graph of the model and learn how model decides
# music_data = pd.read_csv('music.csv')
# x = music_data.drop(columns=['genre'])
# y = music_data['genre']
# model = DecisionTreeClassifier()
# model.fit(x, y)
# tree.export_graphviz(model, out_file='music_recommender.dot', feature_names=[
#                      'age', 'gender'], class_names=sorted(y.unique()), label='all', rounded=True, filled=True)
