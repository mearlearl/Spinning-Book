%%%%  JACOBI FUNCTION PART 2 %%%%

clear;
clc;

% Define parameters:
I1 = 0.0164;
I2 = 0.0185;
I3 = 0.00121;

Itensor = [I1 0 0; 0 I2 0 ; 0 0 I3];
omegavec = [15 0.01 0.01 ]';
Hvec = Itensor*omegavec;
H0 = norm(Hvec);
T0 = 0.5*dot(omegavec,Hvec);

lambda1 = (I2-I3)/I1;
lambda2 = (I3-I1)/I2;
lambda3 = (I1-I2)/I3;

a = sqrt((H0^2-2*T0*I3)/(-I1*I2*lambda2));
b = sqrt((H0^2-2*T0*I2)/(I1*I3*lambda3));
L = sqrt(lambda2*lambda3);

t = linspace(0,10,1000);

if a < b
    k = a/b;
    wx = a*jacobiSN(b*L*t,k);
    wy = a*sqrt(-lambda2/lambda1)*jacobiCN(b*L*t,k);
    wz = b*sqrt(-lambda3/lambda1)*jacobiDN(b*L*t,k);
elseif a > b
    k = b/a;
    wx = b*jacobiSN(a*L*t,k);
    wy = a*sqrt(-lambda2/lambda1)*jacobiDN(a*L*t,k);
    wz = b*sqrt(-lambda3/lambda1)*jacobiCN(a*L*t,k); 
else
    wx = a*tanh(a*L*t);
    wy = a*sqrt(-lambda2/lambda1)*sech(a*L*t);
    wz = a*sqrt(-lambda3/lambda1)*sech(a*L*t);
end

plot(t,wx,t,wy,t,wz)
