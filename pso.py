import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

# Make data.
X = np.arange(-10, 10, 0.01)
Y = np.arange(-10, 10, 0.01)
X, Y = np.meshgrid(X, Y)
#https://en.wikipedia.org/wiki/Rosenbrock_function
Z = -np.sin(X)*((np.sin(X**2/3.14)**(2*10))-np.sin(Y))*(np.sin(Y**2/3.14)**(2*10))
upsize=1
num_func_params = 2
num_swarm = 102
position = -3 + 6 * np.random.rand(num_swarm, num_func_params)
velocity = np.zeros([num_swarm, num_func_params])
personal_best_position = np.copy(position)
personal_best_value = np.zeros(num_swarm)

for i in range(num_swarm):
    #Z = (1-X)**2 + 1 *(Y-X**2)**2
    personal_best_value[i] = (1-position[i][0])**2 + 1 *(position[i][1]-position[i][0]**2)**2

tmax = 300
c1 = 0.05
c2 = 0.06
levels = np.linspace(-1, 35, 100)
global_best = np.min(personal_best_value)
global_best_position = np.copy(personal_best_position[np.argmin(personal_best_value)])

personal_best_position[100][0]=-8
personal_best_position[100][1]=-8
personal_best_position[101][0]=8
personal_best_position[101][1]=8
foodsize=12
for t in range(tmax):
    if foodsize < 1:
        personal_best_position[100][0]+=1
        personal_best_position[100][1]+=1
        personal_best_position[101][0]-=1
        personal_best_position[101][1]-=1
        upsize+=1
        foodsize=12

    for i in range(100):

        error = (1-position[i][0])**2 + 1 *(position[i][1]-position[i][0]**2)**2
        if personal_best_value[i] > error:
            personal_best_value[i] = error
            personal_best_position[i] = position[i]
    best = np.min(personal_best_value)
    best_index = np.argmin(personal_best_value)
        
    for i in range(100):
        #update velocity
        x1= position[i][0]-personal_best_position[100][0]
        x2= position[i][0]-personal_best_position[101][0]

        if x1<0:
            x1 = x1*-1
        if x2<0:
            x2= x2*-1
        if x1 < x2 : 
            if position[i][1]<personal_best_position[100][1]:
                if x1<0.1:
                    velocity[i][0]= 0 * np.random.rand()
                    velocity[i][1]= 0.2 * np.random.rand()
                    foodsize-=0.03
                else:
                    velocity[i][0]= -0.2 * np.random.rand()
                    velocity[i][1]= 0.2 * np.random.rand()
            else:
                if x1<0.1:
                    velocity[i][0]= 0 * np.random.rand()
                    velocity[i][1]= -0.2* np.random.rand()
                    foodsize-=0.03
                else:
                    velocity[i][0]= -0.2 * np.random.rand()
                    velocity[i][1]= -0.2 * np.random.rand()
            if position[i][0]<personal_best_position[100][0]:
                velocity[i][0]= 0.2 * np.random.rand()
            else:
                velocity[i][0]=-0.2 * np.random.rand()
                        
        else :
            if position[i][1]<personal_best_position[101][1]:
                if  x2 < 0.1:
                    velocity[i][0]= 0 * np.random.rand()
                    velocity[i][1]= 0.2 * np.random.rand()
                    foodsize-=0.03
                else:
                    velocity[i][1]= 0.2 * np.random.rand()
            else:
                if x2 < 0.1:
                    velocity[i][0]= 0 * np.random.rand()
                    velocity[i][1]= -0.2 * np.random.rand()
                    foodsize-=0.03
                else:
                    
                    velocity[i][1]= -0.2 * np.random.rand()

            if position[i][0]<personal_best_position[101][0]:
                velocity[i][0]= 0.2 * np.random.rand()
            else:
                velocity[i][0]=-0.2 * np.random.rand()
            
        position[i] += velocity[i]
    
    fig = plt.figure()
    CS = plt.contour(X, Y, levels =levels, cmap=cm.gist_stern)
    plt.gca().set_xlim([-10,10])
    plt.gca().set_ylim([-10,10])
    for i in range(100):
        plt.plot(position[i][0], position[i][1], 'go',markersize=upsize)
        plt.plot(personal_best_position[100][0], personal_best_position[100][1], 'r^',markersize=foodsize)
        plt.plot(personal_best_position[101][0], personal_best_position[101][1], 'r^',markersize=foodsize)
    
    plt.title('{0:03d}'.format(t))
    filename = 'img{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)
