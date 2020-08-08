import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(1,15) 
y = 3 * x + 7 
plt.title("Amanpreet Singh") 
plt.xlabel("x axis ") 
plt.ylabel("y axis ") 
plt.plot(x,y) 
#plt.plot(x,y,"ob") 
plt.show()
