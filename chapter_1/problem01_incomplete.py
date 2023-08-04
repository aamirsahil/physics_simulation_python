# import numpy as np
import matplotlib.pyplot as plt
# to plot graph
def plot_data( x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
# to print out data on terminal
def print_data( block_pos, left_wedge_force, right_wedge_force, t):
    print("Data at time = " + str(t))
    print("--------------------")
    print("Block Position = " + str(block_pos))
    print("left wedge force = " + str(left_wedge_force))
    print("right wedge force = " + str(right_wedge_force))
    print("################################")
# beam data
beam_length = 10
beam_weight = 400
wedge_sep = 2
# block data
block_weight = 800
block_pos = 4
block_vel = -7
block_pos_data = [block_pos] # block data for plotting
# force data
left_wedge_force = ((6 - 5)*400 + (6 - block_pos)*800)/2
right_wedge_force = ((5 - 4)*400 + (block_pos - 4)*800)/2
if(left_wedge_force < 0):
    left_wedge_force = 0
if(right_wedge_force < 0):
    right_wedge_force = 0
left_wedge_force_data = [left_wedge_force] # force data for plotting(left)
right_wedge_force_data = [right_wedge_force] # force data for plotting(right)
# time data
dt = 0.001
t = 0
time_data = [t] # time data for plotting

print_data(block_pos, left_wedge_force, right_wedge_force, t)
# main loop
while(block_pos < 10 and block_pos >= 0):
    
    t += dt
    block_pos += block_vel*dt
    left_wedge_force = ((6 - 5)*400 + (6 - block_pos)*800)/2
    right_wedge_force = ((5 - 4)*400 + (block_pos - 4)*800)/2
    if(left_wedge_force < 0):
        left_wedge_force = 0
    if(right_wedge_force < 0):
        right_wedge_force = 0

    time_data.append(t)
    block_pos_data.append(block_pos)
    left_wedge_force_data.append(left_wedge_force)
    right_wedge_force_data.append(right_wedge_force)
print_data(block_pos, left_wedge_force, right_wedge_force, t)

# plot_data(time_data, block_pos_data, "time vs block pos", "time", "block pos")
# plot_data(time_data, left_wedge_force_data, "time vs left wedge force", "time", "left wedge force")
# plot_data(time_data, right_wedge_force_data, "time vs right wedge force", "time", "right wedge force")
