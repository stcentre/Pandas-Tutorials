from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

# can plot specifically, after just showing the defaults:
plt.plot(x,y,'r',label='line one', linewidth=5)
plt.plot(x2,y2,'g',label='line two',linewidth=5)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()

plt.grid(True,color='k')

plt.show()
