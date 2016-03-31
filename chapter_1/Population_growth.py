import matplotlib.pyplot as plt
# import matplotlib.animation as ani

# define global constants
print "Please enter the initial population: "
N_0 = float(raw_input())

# initiate variables
N = [N_0, ]
t = [0, ]

# # New figure with white background
# fig = plt.figure(figsize=(6, 6), facecolor="white")

# # New axis over the whole figure, no frame and a 1:1 aspect ratio
# ax = fig.add_axes([0, 0, 1, 1], frameo1n=False, aspect=1)

# # Scatter plot
# scat = ax.scatter(N, t)


def growth(N, t, t_terminal, dt, a, b):
    # calculate the population growth and record
    # global a, b, N_0
    # print a, b
    while (t[-1] <= t_terminal and N[-1] >= 0):
        t.append(t[-1] + dt)
        N.append(N[-1] + dt*(a*N[-1] - b*(N[-1]**2)))
        if N[-1] < 0:
            N.pop()
            t.pop()
            break
    # print N, "\n", t


def update(t, N):
    global N_0

    print "Please enter a: "
    a = float(raw_input())

    print "Please enter b: "
    b = float(raw_input())

    # a = 1
    # b = 0.001
    t_terminal = 10
    dt = 0.1

    growth(N, t, t_terminal, dt, a, b)

    plt.plot(t, N)
    plt.xlabel('t')
    plt.ylabel('N')
    plt.title('population growth')

    plt.show()
    # Return the modified object
    # return scat

update(t, N)
# fig = plt.plot(t, N)
# animation = ani.FuncAnimation(fig, update, interval=50, blit=False, frames=len(N))


# print t
# print N
# plt.show()
