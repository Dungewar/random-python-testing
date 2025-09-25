import matplotlib.pyplot as plt
import numpy

# ----- STARTING CONDITIONS -----
DEST_X = 10
DEST_Y = 5
ANGLE = 45 * numpy.pi/180  # degrees
DRAG_COEFFICIENT = 1.3e-3
GRAVITY = 9.81
MASS = 14 / 1000
QUADRATIC = True
MAX_TIME = 10
MAX_LAUNCH_SPEED = 100

# ----- SIMULATION VARIABLES -----
DT: float = 0.0001
ACCEPTABLE_DISTANCE = 0.001**2 # to account for quare distance

def simulate(v: float):
    points = [(0,0)]
    t = 0
    x = 0
    y = 0
    vx = v * numpy.cos(ANGLE)
    vy = v * numpy.sin(ANGLE)
    min_distance = 1e10
    closest_point = (x, y, min_distance, points)
    while y >= 0 and t < MAX_TIME:
        ax = (-DRAG_COEFFICIENT * vx * (vx if QUADRATIC else 1)) / MASS
        ay = -GRAVITY + (-DRAG_COEFFICIENT * vy * (vy if QUADRATIC else 1)) / MASS
        vx += ax*DT
        vy += ay*DT
        x += vx*DT
        y += vy*DT
        t += DT
        points.append((x,y))
        square_distance = (x - DEST_X)**2 + (y - DEST_Y)**2
        if square_distance < min_distance:
            closest_point = (x, y, square_distance, points)
            min_distance = square_distance
    return closest_point

v_bound_max = MAX_LAUNCH_SPEED
v_bound_min = 0
v = 0
prev_distance = -1
while True:
    x, y, distance, profile = simulate(v)
    print(f"Initial velocity: {v:7.3f}, Min distance: {(numpy.sqrt(distance)):7.5f}")
    if distance < ACCEPTABLE_DISTANCE or distance == prev_distance: # acceptable or best possible approximation
        print(f"----- Best case -----\nX: {x:7.5f}, X: {y:7.5f}, Distance: {distance:7.5f}")
        break
    if y < DEST_Y: # undershoots
        v_bound_min = v
    if y > DEST_Y: # overshoots
        v_bound_max = v
    v = (v_bound_min + v_bound_max) / 2
    prev_distance = distance

x_points = [p[0] for p in profile]
y_points = [p[1] for p in profile]
plt.plot(x_points, y_points, '-r', label='Regression line')
plt.legend()

plt.show()