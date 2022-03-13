import sklearn
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

sklearn.datasets.load_iris  # Загружаем датасет Ирис
data = pd.read_csv('Iris.csv')  # Помещаем датасет в перемнную
data.drop('Id', axis=1, inplace=True)  # убираем ненужный столб ID
print(data.head(5))
X = data.iloc[:, :-1].values  # ".iloc" принимает row_indexer, column_indexer
y = data['Species']  # Теперь выделим нужный столбец
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,
                                                    random_state=27)  # Этот параметр можно использовать для воссоздания определённого результата:
# test_size показывает, какой объем данных нужно выделить для тестового набора
# Random_state — просто сид для случайной генерации
print('x_train :\n', X_train)
print('y_train :\n', y_train)
SVC_model = svm.SVC()
KNN_model = KNeighborsClassifier(n_neighbors=10)
SVC_model.fit(X_train, y_train)
KNN_model.fit(X_train, y_train)
SVC_prediction = SVC_model.predict(X_test)
KNN_prediction = KNN_model.predict(X_test)
print('SVC:', accuracy_score(SVC_prediction, y_test))  # Оценка точности
print('KNN:', accuracy_score(KNN_prediction, y_test))
print(confusion_matrix(SVC_prediction, y_test))  # Матрица неточности
print(classification_report(KNN_prediction, y_test))
