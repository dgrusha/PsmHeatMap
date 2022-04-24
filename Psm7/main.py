import numpy as np
from point import Point
import seaborn as sns
import matplotlib.pyplot as plt


def create_list_of_points(x, y, width, height):
    list = [Point(x + 1, y, width, height, 1), Point(x, y, width, height, -4), Point(x - 1, y, width, height, 1),
            Point(x, y + 1, width, height, 1), Point(x, y - 1, width, height, 1)]
    # T(i+1, j) -4T(i,j)+T(i-1,j)+T(i,j+1)+T(i,j-1)
    list.sort(key=lambda k: [k.y, k.x])
    return list


def create_dict_of_cells(w, h):
    cell_val = {}
    index = 0
    for i in range(h):
        for k in range(w):
            print("(" + str(k + 1) + " ," + str(i + 1) + ")")
            key = [k + 1, i + 1]
            cell_val[str(key)] = index
            index += 1
    return cell_val


def generate_array_of_zeros(width, height):
    buckets = [0] * width * height
    return buckets


def generate_array_of_zeros_2d(width, height):
    buckets = [[0]]
    for k in range(width * height - 1):
        buckets.append([0])
    return buckets


def generate_array_of_zeros_for_res(width, height, data):
    buckets = [[0] * width]
    for k in range(height - 1):
        buckets.append([0] * width)
    i = height - 1
    count = 0
    while i != -1:
        for r in range(width):
            buckets[i][r] = data[count][0]
            count += 1
        i = i - 1
    return buckets


def generate_array(width, height):
    a = np.array(generate_array_of_zeros(width, height))
    for k in range(width * height - 1):
        a = np.append(a, generate_array_of_zeros(width, height), axis=0)
    arr_2d = np.reshape(a, (width * height, width * height))
    return arr_2d


def fulfil_array(w, h):
    result_array = generate_array(w, h)
    second_arr = generate_array_of_zeros_2d(w, h)
    second_arr2 = generate_array_of_zeros(w, h)
    print(second_arr2)
    print(result_array)
    print("DICT")
    dict_of_cells = create_dict_of_cells(w, h)
    print(dict_of_cells)
    row = -1
    for i in range(h):
        for k in range(w):
            row = row + 1
            print("(" + str(k + 1) + " ," + str(i + 1) + ")")
            list_of_points = create_list_of_points(k + 1, i + 1, w, h)
            for l in range(len(list_of_points)):
                point_array = str([list_of_points[l].x, list_of_points[l].y])
                cell = dict_of_cells.get(point_array)
                if (list_of_points[l].value < 2):
                    result_array[row][cell] = list_of_points[l].value
                else:
                    second_arr[row][0] = second_arr[row][0] - list_of_points[l].value
                print(str(list_of_points[l].x) + " <-x // y->" + str(list_of_points[l].y) + " value " + str(
                    list_of_points[l].value) + "//// " + str(cell))
    res_array_np = np.array(result_array)
    res_second_arr = np.array(second_arr)
    print(res_array_np)
    print(res_second_arr)
    res = np.linalg.solve(res_array_np, res_second_arr)
    print(res)
    res2 = generate_array_of_zeros_for_res(w, h, res)
    sns.heatmap(res2, cmap='coolwarm')
    sns.color_palette("coolwarm", as_cmap=True)
    plt.show()


if __name__ == '__main__':
    h = 40
    w = 40
    fulfil_array(w, h)
