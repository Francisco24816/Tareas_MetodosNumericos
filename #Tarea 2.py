#Tarea 2
#Francisco Avendaño

#Definimos las variables
p_sick=0.2 #Prob. que la persona este enferma
p_healthy=0.8 #Prob. que este sana
p_truesick=0.9 #Prob. real positivo
p_falsesick=0.3 #Prob. falso positivo
p_rash=0.2 #Prob. manchas despues de la droga

p_sick_true_rash=p_sick*p_truesick*p_rash #Prob. que este enfermo sea verdad y tenga manchas

p_rash_total= p_sick_true_rash + p_healthy*p_falsesick*p_rash #Prob. manchas total

p_total = p_sick_true_rash/p_rash_total 

print('La probabilidad que haya tenido la enfermedad si tiene manchas rojas es de', p_total)







