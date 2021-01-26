from tabulate import tabulate

x1 = [0.9, 5.21, 0.99, 4.68, 3.31, 2.59, 1.2, 4.26, 3.9, 1.91, 2.61, 3.23, 0.47, 4.14, 4.54, 0.21, 1.37, 4.33]
x4=[3.19, 2.26, 3.36, 2.3, 2.73, 3.17, 3.2, 2.26, 2.69, 3.12, 3.39, 2.44, 2.25, 2.36, 1.98, 2.08, 3.16, 2.54]
x6=[2.91, 2.53, 2.64, 3.02, 2.29, 3.61, 5.58, 0.95, 0.87, 4.94, 3.96, 1.88, 7.25, 0.54, 1.36, 7.65, 5.42, 1.12]
t=[7.0, 10.0, 7.0, 10.0, 8.33, 9.37, 9.98, 7.46, 7.45, 9.97, 9.96, 7.55, 9.96, 7.03, 7.88, 9.95, 9.95, 7.99]

table = []

for i in range(1,len(x1)+1):
    table.append([i,x1[i-1],x4[i-1],x6[i-1],t[i-1]])

print(tabulate(table,headers=["Link","X1","X4","X6","Total Traffic"],tablefmt='orgtbl'))