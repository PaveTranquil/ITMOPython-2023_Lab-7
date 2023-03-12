from time import perf_counter

import matplotlib.figure
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def task_1():
    print('Задание №1')
    # задаём два списка со 1_000_000 случайных чисел от 0 до 99 включительно
    np_arr_1, np_arr_2 = np.random.randint(0, 100, 10 ** 6), np.random.randint(0, 100, 10 ** 6)
    # преобразовываем эти списки к спискам Python
    py_arr_1, py_arr_2 = np.ndarray.tolist(np_arr_1), np.ndarray.tolist(np_arr_2)

    def np_performance():
        t_start = perf_counter()  # записываем время начала выполнения
        np.multiply(np_arr_1, np_arr_2)  # перемножаем матрицы
        return perf_counter() - t_start  # записываем время окончания выполнения

    def py_performance():
        t_start = perf_counter()  # записываем время начала выполнения
        [el_1 * el_2 for el_1 in py_arr_1 for el_2 in py_arr_2]  # перемножаем матрицы
        return perf_counter() - t_start  # записываем время окончания выполнения

    print('Считаем...', end='\r')
    # выполняем обе функции и выводим время выполнения (на миллионе, на самом деле, очень долго считает)
    print(f'Время выполнения на numpy: {np_performance()}\nВремя выполнения на python: {py_performance()}')


def task_2():
    # задаём массив по файлу data2.csv с разделителем [,], пропуская ↓ заголовок таблицы и используя только 3 ↓ колонку
    arr = np.genfromtxt('data2.csv', delimiter=',', skip_header=1, usecols=(2,))
    # задаём нормализованный массив по исходному
    arr2 = (arr - arr.min()) / (arr.max() - arr.min())
    # вычисляем среднеквадратичное отклонение массива (STD)
    std = np.std(arr)

    # задаём фигуру 10×4 дюйма
    fig: matplotlib.figure.Figure = plt.figure(figsize=(10, 4))
    # первые оси будут содержать в себе график по массиву и STD
    ax_1: matplotlib.pyplot.Axes = fig.add_subplot(121)
    # вторые оси будут содержать в себе график по нормализованному массиву
    ax_2: matplotlib.pyplot.Axes = fig.add_subplot(122)
    fig.subplots_adjust(wspace=0.5)  # между графиками расстояние в 0.5 дюйма

    # отрисовываем гистограмму и попутно получаем максимальное значение по оси OY — высоту гистограммы
    height = ax_1.hist(arr, bins=16)[0].max()

    ax_2.hist(arr2, bins=16, density=True, color='green')  # отрисовываем нормализованную гистограмму

    # отрисовываем прямую x = STD по высоте графика
    ax_1.plot(np.repeat(std, height[0].max()), np.arange(height), color='red')
    # указываем аннотацию к прямой
    ax_1.annotate('среднеквадратичное отклонение', xy=(std - std / 20, 0),
                  xytext=(std + std / 15, height[0].max() / 10)).set_rotation(90)

    # именуем графики и оси
    ax_1.set_title('Распределение Solids')
    ax_1.set_xlabel('значение измерения')
    ax_1.set_ylabel('интервалы измерений')

    ax_2.set_title('Нормализованное распределение Solids')
    ax_2.set_xlabel('значение измерения')
    ax_2.set_ylabel('интервалы измерений')

    plt.show()  # отображаем графики в gui


def task_3():
    xs = np.linspace(-np.pi, np.pi, 100)  # задаём по OX линейное пространство 100 точек от -π до π
    ys = 1 / xs  # по OY — гиперболу 1/x
    zs = np.sin(xs)  # по OZ — синусоиду sin(x)

    # создаём фигуру, 3D-оси и отрисовываем точками график, используя выше объявленные оси OX, OY и OZ
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(xs, ys, zs, marker='.')
    plt.show()  # отображаем график в gui


if __name__ == '__main__':
    task_1()
    # task_2()
    # task_3()
