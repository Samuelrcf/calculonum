import numpy as np

from scipy import optimize

 

def g(x):  

    # return np.log(10/x)

    # return -np.sqrt((12-x**3)/5), #ponto fixo para a função f(x)=x^3+5x^2-12

    # return -np.sqrt((12-x**3)/5)

    # return np.cos(x)

    return 2-x**3-x**2

 

 #est. da solucao  

xe = optimize.fixed_point(g, 0.5, xtol=1e-08, maxiter=500, method='del2')  

 

  #aprox. inicial  

x0 = 0.5 

eps = np.fabs(x0-xe)  

print("x1 =  %.5f, eps =~ %.1e" % (x0, eps))  

 

for i in np.arange(30):  

    x = g(x0);  

    eps = np.fabs(x-xe);  

    print('%s =~ %.5f, eps =~ %.1e' % (('x'+str(i+2)), x, eps))  

    x0 = x