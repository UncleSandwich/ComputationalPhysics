# This is a program used to solve promotionectile related problems.
# Detail description and update progress of this program are written in the README.md.
import numpy as numpy
import matplotlib.pyplot as pyplot


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
                if self.t >= 10:
                    break

            if self.motion[-1]["y"] < 0:
                self.motion[-1] = {"x": self.x, "y": self.y, "distance": self.d,
                                   "v_x": self.v_x, "v_y": self.v_y, "v": self.v, "t": self.t} 
                                     # need modified
        except:
            pass

    def final_position(self):
        self.final_position = self.motion[-1]

    def highest_position(self):
        y = []
        self.highest_position = []
        for motion in self.motion:
            y.append(motion["y"])
        for motion in self.motion:
            if abs(motion["y"] - max(y)) <= 0.00000001:
                self.highest_position.append(motion)

    def highest_velocity(self):
        v_array = []
        self.highest_velocity = []
        for motion in self.motion:
            v_array.append(motion["v"])
        for motion in self.motion:
            if abs(motion["v"] - max(v_array)) <= 0.00000001:
                self.highest_velocity.append(motion)

    def shortest_deviation_from_target(self, target_x=10, target_y=0):
        distance = []
        for motion in self.motion:
            distance.append(numpy.sqrt((motion["x"] - target_x)**2 + (motion["y"] - target_y)**2))
        return min(distance)


def analysis():
    error = []
    shooting = []
    for i in range(1000):
        shooting.append(shell())
        shooting[-1].shoot()
        error.append(shooting[-1].shortest_deviation_from_target())
    # variance = numpy.var(error)
    standard_deviation = numpy.std(error)
    print "standard_deviation: ", standard_deviation


# analysis(dt=0.1)
shooting = shell()
shooting.have_gravity()
shooting.shoot()
x, y = [], []
for motion in shooting.motion:
    x.append(motion["x"])
    y.append(motion["y"])
pyplot.plot(x, y)
pyplot.show()