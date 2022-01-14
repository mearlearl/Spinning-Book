%%% Adv. Dyn Project %%%

%%% Define system parameters

height = 0.254;    %[m]  Height of Book
width = 0.204;     %[m]  Width of Book
thickness = 0.026; %[m]  Thickness of Book
mass = 1.36;       %[kg] Mass of Book

% Calculate moments of inertia
% Note ranking I1 > I2 > I3

I1 = 1/12*mass*((height)^2+(width)^2);
I2 = 1/12*mass*((height)^2+(thickness)^2);
I3 = 1/12*mass*((width)^2+(thickness)^2);

% Calculate constants

lambda1 = (I2-I3)/I1;
lambda2 = (I3-I1)/I2;
lambda3 = (I1-I2)/I3;

% Set initial angular velocity omega0

omega0 = [0.001, 0.001, 10];  %[rad/s] initial angular velocity