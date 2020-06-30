import matplotlib.pyplot as plt
import numpy as np 


DIMS = 2
PARTICLES = 50
UPDATES_PER_SECOND = 5


def initiate(dims, particles):
    intial_position = (np.random.rand(particles, dims) - 0.5)*1.0
    initial_velocity = (np.random.rand(particles, dims) - 0.5)*1.0
    mass = np.linspace(1,50,particles)
    return [intial_position, initial_velocity, mass]

start_position, start_velocity , masses = initiate(DIMS, PARTICLES)
print(start_velocity)

x ,y = start_position.T


plt.ion()
fig, ax = plt.subplots()

sc = ax.scatter(x,y, marker = 'o', s=2)
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.draw()
new_position = np.zeros((PARTICLES,DIMS))
for i in range(1000):
    new_position = start_position + start_velocity
    x, y = new_position.T 
    print(x[0], y[0])
    start_position = new_position
    sc.set_offsets(np.c_[x,y])
    fig.canvas.draw_idle()
    plt.pause(0.1)

plt.waitforbuttonpress()



