import csv
import math
import numpy as np
import matplotlib.pyplot as plt
def data_reader(file_obj):
    reader = csv.reader(file_obj, delimiter=' ', quotechar='|')
    firstline = next(reader)
    N = int(firstline[0])
    t = float(firstline[1].replace(',', '.'))
    data = []
    data.append([N, t])
    i = 0
    for row in reader:
        data.append([float(row[0].replace(',','.')),float(row[1].replace(',','.'))])
        i+=1
    return data

def coordinates_counter(odometry_data):
    N = odometry_data[0][0]
    delta_t = odometry_data[0][1]
    print(N)
    x_coordinate=0
    y_coordinate = 0
    angle = 0
    coordinates = np.zeros((N, 2))
    for i in range(1,N):
        velocity = odometry_data[i][0]
        angular_speed = odometry_data[i][1]
        angle = angle + angular_speed*delta_t
        x_coordinate =round(x_coordinate + velocity * math.cos(angle) * delta_t , 3)
        y_coordinate = round(y_coordinate + velocity * math.sin(angle) * delta_t, 3)
        coordinates[i][0] = x_coordinate
        coordinates[i][1] = y_coordinate
        x,y = coordinates.T
    plt.scatter(x,y)
    plt.show()
    print(coordinates)
def path_plotting(coordinates):

    return 0
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_obj = open('V_omega.csv', newline='')
    velocity_angularspeed = data_reader(file_obj)
    coordinates = coordinates_counter(velocity_angularspeed)
    path_plotting(coordinates)