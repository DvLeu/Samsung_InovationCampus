import numpy as np  
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics, preprocessing

#? Cargamos los datos del dataset de cáncer
data = load_breast_cancer()
x = data['data']
y = 1 - data['target']

#? Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(x, y, 
                                                    test_size=0.4, 
                                                    random_state=1234)

#? Preprocesamos los datos: normalizamos (hacemos que todos los valores estén en la misma escala)
scaler = preprocessing.StandardScaler().fit(X_train)  # Creamos el objeto para normalizar los datos
X_train_scaled = scaler.transform(X_train)  # Aplicamos la normalización a los datos de entrenamiento
X_test_scaled = scaler.transform(X_test)    # Aplicamos la misma normalización a los datos de prueba

#? KNN con k = 5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, Y_train)  # Entrenamos con los datos normalizados

#? Realizar predicciones en el conjunto de prueba
Y_pred = knn.predict(X_test_scaled)  # Usamos los datos normalizados para las predicciones

#? Calcular métricas de evaluación
accuracy = metrics.accuracy_score(Y_test, Y_pred)
precision = metrics.precision_score(Y_test, Y_pred)
recall = metrics.recall_score(Y_test, Y_pred)
f1 = metrics.f1_score(Y_test, Y_pred) 

#? Mostrar resultados
print("PREPROCESADO : ")
print("Exactitud (Accuracy):", accuracy)
print("Precisión (Precision):", precision)
print("Llamada (Recall):", recall)
print("Puntaje F1 (F1-Score):", f1)