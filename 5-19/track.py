import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk


def my_map(over_x, over_y, in_x, in_y):
    plt.figure()
    plt.scatter([-900, -600, -100, -600, -100, -900, -600, -100], [-100, -100, -100, -300, -300, -700, -700, -700])
    plt.plot([-600, -600], [-100, -700], linestyle='--', color='blue')
    plt.plot([-900, -100], [-100, -100], linestyle='--', color='blue')
    plt.plot([-600, -100], [-300, -300], linestyle='--', color='blue')
    plt.plot([-900, -900], [-100, -700], linestyle='--', color='blue')
    plt.plot([-100, -100], [-100, -700], linestyle='--', color='blue')
    plt.plot([-900, -100], [-700, -700], linestyle='--', color='blue')

    # plt.plot(over_x * 100, over_y * 100, color='red')

    for i, j in zip(over_x, over_y):
        plt.plot(i, j, color='red')

    for i, j in zip(in_x, in_y):
        plt.plot(i, j, color='black')

    plt.show()


def data_process(x, y, file_name):
    over_x = []
    over_y = []
    in_x = []
    in_y = []
    temp_x = []
    temp_y = []
    flag = True
    for i, j in zip(x * 100, y * 100):
        if is_overstep(i, j, file_name):
            if flag:
                temp_x.append(i)
                temp_y.append(j)
            else:
                temp_x.append(i)
                temp_y.append(j)
                over_x.append(temp_x.copy())
                over_y.append(temp_y.copy())
                temp_x.clear()
                temp_y.clear()
                temp_x.append(i)
                temp_y.append(j)
                flag = True
        else:
            if flag:
                temp_x.append(i)
                temp_y.append(j)
                in_x.append(temp_x.copy())
                in_y.append(temp_y.copy())
                temp_x.clear()
                temp_y.clear()
                temp_x.append(i)
                temp_y.append(j)
                flag = False
            else:
                temp_x.append(i)
                temp_y.append(j)
    return over_x, over_y, in_x, in_y


def is_overstep(x, y, file_name):
    if file_name == 'data/loc5.csv':
        if -900 < x < -100 and -700 < y < -100:
            return True
        else:
            return False
    elif file_name == 'data/loc1.csv' or file_name == 'data/loc4.csv':
        if -900 < x < -600 and -700 < y < -100:
            return True
        else:
            return False
    elif file_name == 'data/loc2.csv':
        if -600 < x < -100 and -300 < y < -100:
            return True
        else:
            return False
    elif file_name == 'data/loc3.csv':
        if -600 < x < -100 and -700 < y < -300:
            return True
        else:
            return False


if __name__ == '__main__':
    file_name = 'data/loc5.csv'
    data = pd.read_csv(file_name, usecols=[1, 2, 3, 4], low_memory=False, names=['Time', 'tagId', 'LocX', 'LocY'],
                       header=0)
    data = data[data['tagId'] == 364]
    loc_x = data['LocX']
    loc_y = data['LocY']
    plt.figure()
    plt.plot(loc_x*100,loc_y*100)
    plt.show()
    plt.close()
    over_x, over_y, in_x, in_y = data_process(loc_x, loc_y, file_name)
    my_map(over_x, over_y, in_x, in_y)
    # my_map(loc_x, loc_y, in_x, in_y)
