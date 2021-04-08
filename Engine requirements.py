# Calculating the Required Gearing and Power at the Energy Source

#Writing all the Inputs

m = input("Enter the mass of the vehicle")     #mass of the vehicle in Kg
Cd = input("Enter the Coefficient of Drag")   #Coefficient of Drag
A = input("Enter the frontal area of the vehicle in m2")  #Frontal area of vehicle
theta = input("Enter the sine of gradient of the Road") #gradient of the road
mu = input("Enter the rolling resistance")  #Rolling resistance
a = input("Enter the maximum acceleration of the vehicle in m/s2")
g = 9.8   #acceleration due to gravity in m/s2

#Cacluating the resistive forces required to just move the vehicle

Fin1 = 1.25*m*a   #Inertial force calculation
Faero1 = 0 #aerodynamic drag of vehicle (velocity is Zero)
Fgr1 = m*g*theta  #Gradient force
Frr1 = mu*m*g  #rolling resistance

#Cacluating the required resistive forces for vehicle with constant velocity

v = input("Enter the maximum velocity of the vehicle")  #Maximum velocity of the vehicle
Fin2 = 0 #Inertial force
Faero2 = 0.5*Cd*1.2*A*v*v  #Aerodynamic drag
#Gradient force and Rolling resistance will be the same

#Calculating the required resistive forces for vehicle accelerating

Fin3 = 1.25*m*a  #Inertial force
# All the forces will be same here

Fres1 = Fin1+Faero1+Fgr1+Frr1  #resisitive force required to move the vehicle
Fres2 = Fin2+Faero2+Fgr1+Frr1  #resistive force required for vehicle at constant speed
Fres3 = Fin3+Faero2+Fgr1+Frr1  #resistive force requred for vehicle to accelerate during motion

#Calculating required power at Wheels

Pres1 = 0    #Resistive power at the wheels at the starting
Pres2 = Fres2*v  #Resistive Power when vehicle is at constant speed
Pres3 = Fres3*v   #Resistive Power when vehicle is accelerating while moving

#Cacluating required Torque at Wheels

r = input("Enter the radius of tyre in meter") #radius of tyre

Tres1 = Fres1*r    #Resistive Torque at the wheels at the starting
Tres2 = Fres2*r    #Resistive Power when vehicle is at constant speed
Tres3 = Fres3*r   #Resistive Power when vehicle is accelerating while moving

#Cacluating required Torque and Power at the Engine using a standard 4 speed gearbox

gear1 = input("Enter the gear-ratio for the first gear")
gear2 = input("Enter the gear-ratio for the Second gear")
gear3 = input("Enter the gear-ratio for the third gear")
gear4 = input("Enter the gear-ratio for the fourth gear")

Treq1 = Tres1/gear1  #required torque at the gear during start
Treq2 = Tres2/gear4  #required torque at the Fourth gear
Treq3 = Tres3/gear4 

print(Fres1)
print(Fres2)
print(Fres3)
print(Tres1)
print(Tres2)
print(Tres3)
print(Pres1)
print(Pres2)
print(Pres3)
print(Treq1)
print(Treq2)
print(Treq3)

#End of the program



