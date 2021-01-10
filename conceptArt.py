from logMap import logisticEq
import matplotlib.pylab as plt

x = []
r = []

# Generate the attractor for every value of r
for i in range(3000):
    r.append(3.5+i*0.001)
    #attractor = logisticEq(i*0.0025,0.7,200)
    #x.append(attractor[100:])
    x.append(logisticEq(3.5+i*0.001,0.7,200)[100:])

ax = plt.subplot(111)
ax.set(xlim=(3.5,3.8),ylim=(0,1))
plt.xlabel('r')
plt.ylabel('x')
plt.title(r'$x_n = rx_{n-1}(1-x_{n-1})$')

for i in range(len(r)):
    for j in x[i]:
        ax.plot(r[i],j,'ro',ms=0.2)

plt.savefig("images/bifurcation_diagram_2.png",dpi=300)
plt.show()
