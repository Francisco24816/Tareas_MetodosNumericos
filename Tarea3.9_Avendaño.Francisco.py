import numpy as np

# Generar datos de la distribución
np.random.seed(20)
mu = 0     # Media
sigma = 1   # Desviación estándar
n_samples = 2000000 #Cantidad de sampleos

# Generar los datos de la distribución normal la cual cumple la condición señalada
data = np.random.normal(mu, sigma, n_samples)

mean = np.mean(data) #Promedio
var = np.var(data, ddof=1) #Varianza

cumulante_3 = np.mean((data-mean)**3) #Calculamos el cumulante l=3
cumulante_4 = np.mean((data-mean)**4) - 3 * var**2 #Calculamos el cumulante l=4

#Imprimimos los resultados
print(f"Cumulante de tercer orden: {cumulante_3:.6f}")  
print(f"Cumulante de cuarto orden: {cumulante_4:.6f}") 

# Por lo visto en clases, el cumulante 3 deberían de tender a 0. 
# Mientras que para este caso especifico,
# al ser una distribución normal, la kurtosis tiende a 0, 
# esto quiere decir, que cumulante 4 tiende a 0 too.
