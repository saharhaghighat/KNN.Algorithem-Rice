import main
import statistics
from tkinter import *
import matplotlib.pyplot as plt

from colorama import Fore
import numpy as np
import pandas as pd
from pandastable import Table

pd.set_option('display.max_columns', None)

# Section 1

try:
    df = pd.read_excel('Rice.xlsx')
except FileNotFoundError as e:
    print(e)

print("**************************************")

# Section 2

# Part 1:
TenRows = df.iloc[0:10]
print(TenRows)
# print(TenRows)

print("--------------------------------------------------")
# part 2 :
rows = len(df)
columns = len(df.columns)
print(f"Number of rows :{rows}")
print(f"Number of Columns: {columns}")

print("--------------------------------------------------")


# part 3:

def minmax(f):
    return pd.Series(index=['min', 'max'], data=[f.min(), f.max()])


_minmax = df.apply(minmax)
print(_minmax)

print("**************************************")

# Section 3
std = df.loc[:, df.columns != 'Class'].std()  # calculating Standard variation
avg = df.loc[:, df.columns != 'Class'].mean()
df.loc[:, df.columns != 'Class'] = (df.loc[:, df.columns != 'Class'] - avg) / std

av1 = df.loc[:, df.columns != 'Class'].mean()
print("Average after Normalization :")
print(av1.astype(int))
print("Standard Variation after Normalization :")
std2 = df.loc[:, df.columns != 'Class'].std()
print(std2)

print("**************************************")


# Section 4

def menu():
    Input = input(Fore.BLUE + '''
      W W
      O O          Hi!
      ---

     Menu is here:
       |1.Insert new Data
       |2.Bar Chart
       |3.Exit

        ''')
    distance = []
    # Data Frame for testing :)
    dftest = pd.DataFrame(columns=['Area', 'Perimeter', 'Major_Axis_Length', 'Minor_Axis_Length', 'Eccentricity',
                                   'Convex_Area', 'Extent'])

    match Input:


        case "1":
            Area = float(input(Fore.CYAN + "Input Your Area:"))
            Perimeter = float(input(Fore.CYAN + "Input Your Perimeter:"))
            Major_Axis_Length = float(input(Fore.CYAN + "Input Your Major_Axis_Length:"))
            Minor_Axis_Length = float(input(Fore.CYAN + "Input Your Minor_Axis_Length:"))
            Eccentricity = float(input(Fore.CYAN + "Input Your Eccentricity:"))
            Convex_Area = float(input(Fore.CYAN + "Input Your Convex_Area:"))
            Extent = float(input(Fore.CYAN + "Input Your Extent:"))

            dftest.loc[len(dftest)] = [Area, Perimeter, Major_Axis_Length, Minor_Axis_Length,
                                       Eccentricity, Convex_Area, Extent]

            # Normalizing new Data
            dftest = (dftest - avg) / std
            print("Added AND Normalized successfully :)")
            print("**************************************")
            # Section 5
            testArray = dftest.to_numpy()
            array = df.loc[:, df.columns != 'Class'].to_numpy()
            for i in range(len(array)):
                dis = np.linalg.norm(array[i] - testArray[len(testArray) - 1])
                distance.append(dis)
            df['Distance'] = distance
            _df = df.sort_values('Distance')
            selective = _df.iloc[0:17]
            print(selective)
            print(Fore.GREEN + "Your Rice's Class is " + selective['Class'].mode())
            exit()
        case "2":
            df2 = pd.read_excel('Rice.xlsx')  # Before Normalization
            random = df.sample(n=10)
            i = random.index
            random2 = df2.iloc[i, :]
            print(Fore.YELLOW + 'Random before Normalization')
            print(random2)
            print(Fore.YELLOW + 'Random after Normalization')
            print(random)

            def bar():
                insert = input(Fore.BLUE + '''

                    Which column do you want to see?
                       |1.Area
                       |2.Perimeter
                       |3.Major Axis Length
                       |4.Minor Axis Length
                       |5.Eccentricity
                       |6.Convex Area
                       |7.Extent
                       |8.Main Menu

                        ''')

                x = ['data1', 'data2', 'data3', 'data4', 'data5', 'data6', 'data7', 'data8', 'data9',
                     'data10']
                match insert:
                    case "1":
                        y = random.iloc[:, [0]].values.flatten()
                        y2 = random2.iloc[:, [0]].values.flatten()

                        plt.subplot(2, 1, 1)
                        plt.bar(x, y, color='#c787dd')
                        plt.title("Area after Normalizing", color='#e72c3d')
                        plt.ylabel("Area", labelpad=2, color='#2a4e86')

                        plt.subplot(2, 1, 2)
                        plt.title("Area before Normalizing", color='#e72c3d')
                        plt.bar(x, y2, color='#88c999')
                        plt.ylabel("Area", labelpad=2, color='#2a4e86')

                        plt.subplots_adjust(hspace=0.4)

                        plt.show()
                        bar()

                    case '2':
                        y = random.iloc[:, [1]].values.flatten()
                        y2 = random2.iloc[:, [1]].values.flatten()

                        plt.subplot(2, 1, 1)
                        plt.bar(x, y, color='#c787dd')
                        plt.title("Perimeter after Normalizing", color='#e72c3d')
                        plt.ylabel("Perimeter", labelpad=2, color='#2a4e86')

                        plt.subplot(2, 1, 2)
                        plt.title("Perimeter before Normalizing", color='#e72c3d')
                        plt.bar(x, y2, color='#88c999')
                        plt.ylabel("Perimeter", labelpad=2, color='#2a4e86')

                        plt.subplots_adjust(hspace=0.4)

                        plt.show()
                        bar()
                    case '3':
                        y = random.iloc[:, [2]].values.flatten()
                        y2 = random2.iloc[:, [2]].values.flatten()

                        plt.subplot(2, 1, 1)
                        plt.bar(x, y, color='#c787dd')
                        plt.title("Major Axis Length after Normalizing", color='#e72c3d')
                        plt.ylabel("Major Axis Length", labelpad=2, color='#2a4e86')

                        plt.subplot(2, 1, 2)
                        plt.title("Major Axis Length before Normalizing", color='#e72c3d')
                        plt.bar(x, y2, color='#88c999')
                        plt.ylabel("Major Axis Length", labelpad=2, color='#2a4e86')

                        plt.subplots_adjust(hspace=0.4)

                        plt.show()
                        bar()
                    case '4':
                        y = random.iloc[:, [3]].values.flatten()
                        y2 = random2.iloc[:, [3]].values.flatten()

                        plt.subplot(2, 1, 1)
                        plt.bar(x, y, color='#c787dd')
                        plt.title("Minor Axis Length after Normalizing", color='#e72c3d')
                        plt.ylabel("Minor Axis Length", labelpad=2, color='#2a4e86')

                        plt.subplot(2, 1, 2)
                        plt.title("Minor Axis Length before Normalizing", color='#e72c3d')
                        plt.bar(x, y2, color='#88c999')
                        plt.ylabel("Minor Axis Length", labelpad=2, color='#2a4e86')

                        plt.subplots_adjust(hspace=0.4)

                        plt.show()
                        bar()
                    case '5':
                        y = random.iloc[:, [4]].values.flatten()
                        y2 = random2.iloc[:, [4]].values.flatten()

                        plt.subplot(2, 1, 1)
                        plt.bar(x, y, color='#c787dd')
                        plt.title("Eccentricity after Normalizing", color='#e72c3d')
                        plt.ylabel("Eccentricity", labelpad=2, color='#2a4e86')

                        plt.subplot(2, 1, 2)
                        plt.title("Eccentricity before Normalizing", color='#e72c3d')
                        plt.bar(x, y2, color='#88c999')
                        plt.ylabel("Eccentricity", labelpad=2, color='#2a4e86')

                        plt.subplots_adjust(hspace=0.4)

                        plt.show()
                        bar()
                    case '6':
                        y = random.iloc[:, [5]].values.flatten()
                        y2 = random2.iloc[:, [5]].values.flatten()

                        plt.subplot(2, 1, 1)
                        plt.bar(x, y, color='#c787dd')
                        plt.title("Convex Area  after Normalizing", color='#e72c3d')
                        plt.ylabel("Convex Area ", labelpad=2, color='#2a4e86')

                        plt.subplot(2, 1, 2)
                        plt.title("Convex Area before Normalizing", color='#e72c3d')
                        plt.bar(x, y2, color='#88c999')
                        plt.ylabel("Convex Area", labelpad=2, color='#2a4e86')

                        plt.subplots_adjust(hspace=0.4)

                        plt.show()
                        bar()
                    case '7':
                        y = random.iloc[:, [6]].values.flatten()
                        y2 = random2.iloc[:, [6]].values.flatten()

                        plt.subplot(2, 1, 1)
                        plt.bar(x, y, color='#c787dd')
                        plt.title("Extent after Normalizing", color='#e72c3d')
                        plt.ylabel("Extent", labelpad=2, color='#2a4e86')

                        plt.subplot(2, 1, 2)
                        plt.title("Extent before Normalizing", color='#e72c3d')
                        plt.bar(x, y2, color='#88c999')
                        plt.ylabel("Extent", labelpad=2, color='#2a4e86')

                        plt.subplots_adjust(hspace=0.4)

                        plt.show()
                        bar()
                    case '8':
                        menu()

            bar()
            exit()

        case "3":
            print(Fore.RED + "Goodbye!")
            exit()


menu()
