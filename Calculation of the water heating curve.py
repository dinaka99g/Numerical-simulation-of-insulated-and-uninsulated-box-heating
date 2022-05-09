import math
from queue import PriorityQueue
import sys
from matplotlib import pyplot as plt


def Case1(m_material,T0_material,cp_material,T1_material,Ag,alpha_g,T_vapor,time_step):
    
    temps = [T0_material]
    time = [0]
    q=[0]

    
    while(temps[-1]<T1_material):
          t=time[-1]+time_step
          T=temps[-1]+ alpha_g*Ag*time_step*(T_vapor-temps[-1])/(m_material*cp_material)
          Q=m_material+cp_material*(T-T0_material)
          q.append(Q)
          temps.append(T)
          time.append(t)
                 
    return time,temps,q



                  
def Case2(m_material,T0_material,cp_material,T1_material,Ag,alpha_g,T_vapor,T_environment,Ao,alpha_o,time_step):

    temps2=[T0_material]
    time2=[0]
    t2=0 
    q2=[0]

    while(temps2[-1]<T1_material):
          t2=(time2[-1]+time_step)
          T2=temps2[-1]+ alpha_g*Ag*time_step*(T_vapor-temps2[-1])/(m_material*cp_material)-alpha_o*Ao*time_step*(temps2[-1]-T_environment)/(m_material*cp_material)
          Q2=m_material+cp_material*(T2-T0_material)
          q2.append(Q2)
          temps2.append(T2)
          time2.append(t2)
    return time2,temps2,q2

    
'''
m_material=float(input("Enter the mass of material [kg]"))
cp_material=float(input("Enter the specific heat capacity of the material [J/kgK]"))
T0_material=float(input("Enter the initial value of the material temperature [°C]"))#Initial material temperature
T1_material=float(input("Enter the final temperature to which the material needs to be heated [°C]"))#Final material temperature
Ag=float(input("Enter the contact surface of the heater [m]"))
alpha_g=float(input("Enter the total heat transfer coefficient through the heater[W/m2K]"))
T_vapor=float(input("Enter the water vapor temperature[°C]"))
T_environment=float(input("Enter the environment temperature[°C]"))
Ao=float(input("The outer surface of the tank exposed to the environment [m]"))
alpha_o=float(input("Enter the heat transfer coefficient on the outside [W/m2K]"))
time_step=float(input("Enter the time step")) '''


#solution1=Case1(m_material,T0_material,cp_material,T1_material,Ag,alpha_g,T_vapor,time_step) #Required by project to enter data manually
#solution2=Case2(m_material,T0_material,cp_material,T1_material,Ag,alpha_g,T_vapor,T_environment,Ao,alpha_o,time_step)

time11, temp11, q11=Case1(25000,20,2000,125,10,850,180,100) #Data for testing
time22, temp22, q22=Case2(25000,20,2000,125,10,850,180,20,32,10,100) #Data for testing

print(f'For the first case (with isolation) temperature {temp11[-1]} [°C] is reached for {time11[-1]} [s] or {time11[-1]/3600} [h]')
print(f'For the first case (with no isolation) temperature {temp22[-1]} [°C] is reached for {time22[-1]} [s] or {time22[-1]/3600} [h]')


#Temperature graph plotting
plt.plot(time11,temp11,label='Case1')
plt.plot(time22,temp22,label='Case2')
plt.xlabel('Time [s]')
plt.ylabel('Temperature [°C]')
plt.title('Temperature change: Comparation of Case1 and Case2')
plt.legend()
plt.show() 

#Heat transfer graph plotting
plt.plot(time11,q11,label='Case1')
plt.plot(time22,q22,label='Case2')
plt.xlabel('Time [s]')
plt.ylabel('Heat transfer [W]')
plt.title('Heat transfer change: Case1 and Case2')
plt.legend()
plt.show() 




