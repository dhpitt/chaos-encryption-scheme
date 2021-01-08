from logMap import logisticEq
import matplotlib.pylab as plt

x = []
r = []

# Generate the attractor for every value of r
for i in range(400,1600,1):
    r.append(i*0.0025)
    #attractor = logisticEq(i*0.0025,0.7,200)
    #x.append(attractor[100:])
    x.append(logisticEq(i*0.0025,0.7,200)[100:])

ax = plt.subplot(111)
plt.xlabel('r')
plt.ylabel('x')
plt.title(r'$x_n = rx_{n-1}(1-x_{n-1})$')

for i in range(len(r)):
    for j in x[i]:
        ax.plot(r[i],j,'bo',ms=0.2)
plt.show()