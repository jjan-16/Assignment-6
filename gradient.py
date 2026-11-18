import numpy as np
import matplotlib.pyplot as pp


#T(x, y) = T₀ exp[−(x² + y²)/σ²]

sigma = 1 #m
T0 = 100 #K
dx = 0.1
dy = 0.1

x = np.arange(-3,3+dx,dx)
y = np.arange(-3,3+dy,dy)


X,Y = np.meshgrid(x,y)


temperature = T0*np.exp(-(X**2+Y**2)/(sigma**2))

dtdx = (temperature[:,2:] - temperature[:,0:-2])/(2*dx)
dtdy = (temperature[2:,:] - temperature[0:-2,:])/(2*dy)
grad = np.gradient(temperature,dx)

plot = pp.contourf(X,Y,temperature)
pp.xlabel('x position (m)')
pp.ylabel('y position (m)')
pp.colorbar(plot,label="Temperature (K)")
pp.savefig('t_plate.png') 
