# import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Charger les donnees du fichier
data = pd.read_csv("database/ex1data1.csv")
# data.plot()

# Visualiser les donnees
# plt.show()

# Decoupez vos donnees en deux vecteurs X et y et transformerz-les en array numpy
X = np.array(data['population'])
Y = np.array(data['profit'])

#Calcul d'une premiere predictio

# Initialisez theta en un vecteur de deux valeurs a zero
theta = np.zeros(2)

# ecrivez une fonction predict qui prend en argument une population (x)
# ainsi que les parametres theta et predit le profit (y) associe
# Donc X('population') est un predicteur
# Y (a savoir le profit dans l'exemple est une variable explique)
# pour savoir si un modele est utilisable par la regression simple,
# on peut calculer son coefficient de correlation
# yi = a + b * xi + epsi
# yi => la variable explique
# a => const qui est l'augementation de la variable yi en l'absence de xi
# b => coeff d'augmentation de la variable yi quand xi augmente de 1
# xi => valeur de la variable predicteur
# epsi => residu aleatoire, les epsi de deux xi different n'ont aucun lien!
print("Ca des parametre : ")
covxy = np.cov(X, Y, None, True)[0][1]
b = (covxy) / np.var(X);
a = np.average(Y) - np.average(X) * b
print("La fonction exacte : " + str(a) + " * x + " + str(b))
# print("Determination de la variance de b")
# print("V[b] = Variance du residu epsilon / Nombre d'entre dans la database * Variance X")
# print("Plus la variance de X est grande et plus la variance de b diminue,")
# print("donc l'intervalle de confiance est plus grand.")
# print("V[a] = (Variance du residu epsilon / Nombre d'entre dans la database) \
#  * ( 1 + (Moyenne X) * (Moyenne X) / Variance X)")
# print("Si ma moyenne est trop grande, j'aurais donc des difficultees a savoir \
# ce qu'il se passe lorsque X est a 0");

M = len(X)

def cost():
	print("cost")

def partial_d(otheta, alpha):
	dteta = 0
	dalpha = 0
	for i in range(0, M):
		estimate = otheta[0] + (otheta[1] * X[i])
		dalpha += (estimate - Y[i])
		dteta += ((estimate - Y[i]) * X[i])
	dalpha = otheta[0] - (1/M) * dalpha * alpha
	dteta = otheta[1] - (1/M) * dteta * alpha
	return [dalpha, dteta]

def fit(X, y, theta, alpha = 0.01, num_iters = 1500):
	for i in range(0, num_iters):
		theta = partial_d(theta, alpha)
	return theta

theta = fit(X, Y, theta)

print("Par approximation:")
print(theta[1])
print(theta[0])

def predict(X, theta):
	y = theta[0] * X + theta[1]
	return (y)
value = 500
print("Prediction sur une population de " + str(value) + " : " + str(predict(value, theta)))
