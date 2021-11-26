import math as m
import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plot 

def get_angles():

    # Define parameters:
    # This is the dimensions of my dynamics textbook

    mass = 1.36
    I2 = mass/12*(0.254**2+0.204**2)
    I3 = mass/12*(0.204**2+0.026**2)
    I1 = mass/12*(0.254**2+0.026**2)

    Itensor = np.array([[I1,0, 0], [0, I2, 0] , [0, 0, I3]])

    # The magic is changing these entries!
    omegavec = np.array([10,0.01,0.01])

    Hvec = np.inner(Itensor,omegavec)
    H0 = np.linalg.norm(Hvec)
    T0 = 0.5*np.inner(omegavec,Hvec)
    
    lambda1 = (I2-I3)/I1
    lambda2 = (I3-I1)/I2
    lambda3 = (I1-I2)/I3

    a = m.sqrt((H0**2-2*T0*I3)/(-I1*I2*lambda2))
    b = m.sqrt((H0**2-2*T0*I2)/(I1*I3*lambda3))
    L = m.sqrt(lambda2*lambda3)
    t = np.linspace(0,10,300)

    sn = 0
    cn = 0
    dn = 0

    if a < b:
        k = a/b
        ellipjs = sp.ellipj(b*L*t,k)
        sn = ellipjs[0]
        cn = ellipjs[1]
        dn = ellipjs[2]
        wx = a*sn
        wy = a*m.sqrt(-lambda2/lambda1)*cn
        wz = b*m.sqrt(-lambda3/lambda1)*dn

    elif a > b:
        k = b/a
        ellipjs = sp.ellipj(a*L*t,k)
        sn = ellipjs[0]
        cn = ellipjs[1]
        dn = ellipjs[2]
        wx = b*sn
        wy = a*m.sqrt(-lambda2/lambda1)*dn
        wz = b*m.sqrt(-lambda3/lambda1)*cn
    else:
        wx = a*np.tanh(a*L*t)
        wy = a*m.sqrt(-lambda2/lambda1)/np.cosh(a*L*t)
        wz = a*m.sqrt(-lambda3/lambda1)/np.cosh(a*L*t)


    #plot.plot(t,wx,t,wy,t,wz)
    #plot.show()

    deltat = 10.0/300.0

    return np.array([deltat*wx,deltat*wy,deltat*wz])
    
