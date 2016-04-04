# This is a program used to solve projectile related problems.
# Detail description and update progress of this program are written in the README.md.
import numpy as numpy
import matplotlib.pyplot as pyplot
import random as random


class force(object):
    """docstring for force"""
    def __init__(self):
        self.gravity = False
        self.air_friction = False
        self.coriolis_force = False

    def have_gravity(self):
        self.gravity = True

    def have_air_friction(self):
        self.air_friction = True

    def have_coriolis_force(self):
        self.coriolis_force = True


class shell(force):
    """docstring for shell"""
    def __init__(self, x=0, y=0, v=50, theta=numpy.pi/4, t=0, dt=0.1):
        super(shell, self).__init__()
        self.x = x
        self.y = y
        self.d = numpy.sqrt(self.x**2+self.y**2)

        sigma_v = 0.05*v/3
        sigma_theta = 0.01*theta/3
        v = random.gauss(v, sigma_v)
        theta = random.gauss(theta, sigma_theta)
        self.v_x = v*numpy.cos(theta)
        self.v_y = v*numpy.sin(theta)
        self.v = numpy.sqrt(self.v_x**2+self.v_y**2)

        mass = 10
        self.mass = mass
        self.t = t
        self.dt = dt

        self.motion = [{"x": self.x, "y": self.y, "distance": self.d,
                        "v_x": self.v_x, "v_y": self.v_y, "v": self.v, "t": self.t}, ]

    def shoot(self):
        try:
            while self.y >= 0:
                self.x += self.v_x*self.dt
                self.y += self.v_y*self.dt
                self.d = numpy.sqrt(self.x**2+self.y**2)

                force_x = 0
                force_y = 0

                if self.gravity:
                    g = 10
                    force_x += 0
                    force_y += -self.mass*g

                if self.air_friction:
                    B_2 = 4*(10**(-5))*self.mass
                    force_x += B_2*self.v_x
                    force_y += B_2*self.v_y

                if self.coriolis_force:
                    pass

                self.v_x += force_x/self.mass*self.dt
                self.v_y += force_y/self.mass*self.dt
                self.v = numpy.sqrt(self.v_x**2+self.v_y**2)

                self.t += self.dt

                self.motion.append({"x": self.x, "y": self.y, "distance": self.d,
                                    "v_x": self.v_x, "v_y": self.v_y, "v": self.v, "t": self.t})
                if self.t >= 100:
                    break

            if self.motion[-1]["y"] < 0:
                self.motion[-1] = {"x": self.x, "y": self.y, "distance": self.d,
                                   "v_x": self.v_x, "v_y": self.v_y, "v": self.v, "t": self.t} 
                                     # need modified
        except:
            pass

    def final_position(self):
        return self.motion[-1]

    def highest_position(self):
        y = []
        highest_position = []
        for motion in self.motion:
            y.append(motion["y"])
        for motion in self.motion:
            if abs(motion["y"] - max(y)) <= 0.0000000001:
                highest_position.append(motion)
        return highest_position

    def highest_velocity(self):
        v_array = []
        highest_velocity = []
        for motion in self.motion:
            v_array.append(motion["v"])
        for motion in self.motion:
            if abs(motion["v"] - max(v_array)) <= 0.0000000001:
                highest_velocity.append(motion)
        return highest_velocity

    def shortest_deviation_from_target(self, target_x=10, target_y=0):
        distance = []
        for motion in self.motion:
            distance.append(numpy.sqrt((motion["x"] - target_x)**2 + (motion["y"] - target_y)**2))
        return min(distance)


def analysis(dT, times, Theta, Velocity):
    error = []
    final_position = []
    # Highest_Position = []
    # Highest_Velocity = []
    shooting = []
    # print "dT: ", dT
    for i in range(times):
        shooting.append(shell(dt=dT, theta=Theta, v=Velocity))
        shooting[-1].have_gravity()
        # shooting[-1].have_air_friction()
        shooting[-1].shoot()
        final_position.append(shooting[-1].final_position()["distance"])
        error.append(shooting[-1].shortest_deviation_from_target())
        # Highest_Position.append(shooting[-1].highest_position())
        # Highest_Velocity.append(shooting[-1].highest_velocity())
    # variance = numpy.var(error)
    # standard_deviation = numpy.std(error)
    # print "standard_deviation: ", standard_deviation
    # print "HP: ", Highest_Position
    # print "HV: ", Highest_Velocity
    # print "FP: ", final_position

    for trace in shooting:
        x, y = [], []
        for motion in trace.motion:
            x.append(motion["x"])
            y.append(motion["y"])
        pyplot.plot(x, y)
    pyplot.show()


# for k in range(10):
#     ran = random.uniform(0, numpy.pi/2)
#     analysis(dT=0.01, times=1, Theta=ran, Velocity=100)
analysis(dT=0.01, times=10, Theta=numpy.pi/2, Velocity=100)
# pyplot.show()
# shooting = shell()
# shooting.have_gravity()
# shooting.shoot()
# x, y = [], []
# for motion in shooting.motion:
#     x.append(motion["x"])
#     y.append(motion["y"])
# pyplot.plot(x, y)
# pyplot.show()
