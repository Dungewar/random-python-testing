import matplotlib.pyplot as plt
import numpy

# ----- STARTING CONDITIONS -----
DEST_X = 10
DEST_Y = 5
FINAL_ANGLE = -45 * numpy.pi/180  # degrees
DRAG_COEFFICIENT = 1.3e-3
GRAVITY = 9.81
MASS = 14 / 1000
QUADRATIC = True
MAX_TIME = 10
MAX_LAUNCH_SPEED = 100

# ----- SIMULATION VARIABLES -----
DT: float = 0.0001
ACCEPTABLE_DISTANCE = 0.001**2 # to account for quare distance
ACCEPTABLE_ANGLE = 1 * numpy.pi/180 # within 1 degree
# closest_point_angle = 0
def simulate(sim_v: float, sim_angle: float):
    # global closest_point_angle
    points = [(0,0)]
    t = 0
    x = 0
    y = 0
    vx = sim_v * numpy.cos(sim_angle)
    vy = sim_v * numpy.sin(sim_angle)
    min_distance = 1e10
    closest_point_angle = 0
    closest_point = (x, y, min_distance, points, closest_point_angle)
    # closest_point
    while y >= 0 and t < MAX_TIME:
        ax = (-DRAG_COEFFICIENT * vx * (numpy.abs(vx) if QUADRATIC else 1)) / MASS
        ay = -GRAVITY + (-DRAG_COEFFICIENT * vy * (numpy.abs(vy) if QUADRATIC else 1)) / MASS
        vx += ax*DT
        vy += ay*DT
        x += vx*DT
        y += vy*DT
        t += DT
        points.append((x,y))
        square_distance = (x - DEST_X)**2 + (y - DEST_Y)**2
        if square_distance < min_distance:
            min_distance = square_distance
            # closest_point_angle = 
            closest_point = (x, y, square_distance, points, numpy.atan2(vy, vx))
    return closest_point

v_bound_max = MAX_LAUNCH_SPEED
v_bound_min = 0
v = 0
prev_distance = -1
angle_bound_max = numpy.pi/2
angle_bound_min = 0
sim_angle = numpy.pi/4
prev_angle = numpy.pi/2 # vertical is not allowed anyway
while True:
    final_angle = numpy.pi/2 # vertical is not allowed anyway
    while True:
        x, y, distance, profile, final_angle = simulate(v, sim_angle)
        print(f"Initial velocity: {v:7.3f}, Min distance: {(numpy.sqrt(distance)):7.5f}, angle = {(final_angle*180/numpy.pi)}")
        if distance < ACCEPTABLE_DISTANCE or distance == prev_distance: # acceptable or best possible approximation
            print(f"----- Best case -----\nX: {x:7.5f}, Y: {y:7.5f}, Distance: {distance:.5f}, Final angle: {(final_angle*180/numpy.pi):7.5}, Velocity: {v:7.5}")
            break
        if y < DEST_Y: # undershoots
            v_bound_min = v
        if y > DEST_Y: # overshoots
            v_bound_max = v
        v = (v_bound_min + v_bound_max) / 2
        prev_distance = distance

    if numpy.abs(final_angle-FINAL_ANGLE) < ACCEPTABLE_ANGLE or prev_angle == final_angle:
        print(f"----- SIMULATION OVER -----\nGot the best possible angle ({(sim_angle*180/numpy.pi):.5}) and velocity ({(v):.5}) combo, exiting...")
        break
    if final_angle < FINAL_ANGLE: # undershoots
        angle_bound_max = sim_angle
    if final_angle > FINAL_ANGLE: # overshoots
        angle_bound_min = sim_angle
    sim_angle = (angle_bound_min + angle_bound_max) / 2
    prev_angle = final_angle
    
    
    

x_points = [p[0] for p in profile]
y_points = [p[1] for p in profile]
plt.plot(x_points, y_points, '-r', label='Regression line')
plt.legend()

plt.show()