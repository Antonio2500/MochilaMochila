import cvxpy as cvx

w= [5,6,8,4,2,3,9,8] #peso
b= [3,4,5,2,1,2,6,5] #beneficio
q= 25 #capacidad
n= len(w) #numero de objetos

x= cvx.Variable(n, boolean = True) #variables de decision (binarias)

#restricciones
wacum=0
for i in range(n):
    wacum= wacum+w[i]*x[i]

cst=[]
cst.append(wacum<=q) #construccion de la lista de restricciones

z=0
for j in range(n):
    z= z+b[j]*x[j] #contruccion de la funcion objetivo
    
mochila= cvx.Problem(cvx.Maximize(z), cst) #definicion del problema
zopt= mochila.solve(solver=cvx.GLPK_MI) #resolucion del problema

print("estatus de la mochila: ", mochila.status)
print("valor optimo de la mochila: ", mochila.value)
xr=[]
for i in range(0,n,1):
    if (x.value[i]>0.5):
        xr.append(1)
    else:
        xr.append(0)
print("Mejor decision: ", xr)











