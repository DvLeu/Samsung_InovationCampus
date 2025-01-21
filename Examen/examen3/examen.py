import numpy as np 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics, preprocessing

#? Cargamos los datos del dataset de cancer
data = load_breast_cancer()
x = data['data']
y = 1 - data['target']

#? Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(x, y, 
                                                    test_size=0.4, 
                                                    random_state=1234)

#? KNN con k = 5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)

#? Realizar predicciones en el conjunto de prueba
Y_pred = knn.predict(X_test)

#? Calcular métricas de evaluación
accuracy = metrics.accuracy_score(Y_test, Y_pred)
precision = metrics.precision_score(Y_test, Y_pred)
recall = metrics.recall_score(Y_test, Y_pred)

#? Mostrar resultados
print("Exactitud (Accuracy):", accuracy)
print("Precisión (Precision):", precision)
print("Llamada (Recall):", recall)