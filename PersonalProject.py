import matplotlib.pyplot as plt
import numpy as np
import time

number = 30
capacity = 10149
weight = [508,1021,1321,111,1098,1196,204,939,1107,399,
     474,719,803,1054,1781,525,1050,1362,530,641,
     903,432,583,894,754,806,1241,1056,1092,1545]
profit = [408,921,1329,11,998,1009,104,839,943,299,374,
     673,703,954,1657,425,950,1375,430,541,971,
     332,483,815,654,706,1360,956,992,1948]

w_np = np.array(weight)
p_np = np.array(profit)
ratio = p_np / w_np
print("价值与重量之比：")
for a in ratio:
    print(format(a, '.6f'), end="  ")
    
print("\n\n非递增排序后：")
res = sorted(ratio, reverse = True)
for b in res:
    print(format(b, '.6f'), end="  ")

def backpack(number, capacity, w, v):
    result = [[0 for i in range(capacity+1)]for i in range(number+1)]
    for i in range(1, number+1):
        for j in range(1, capacity+1):
            if j < w[i-1]:
                result[i][j] = result[i-1][j]
            else:
                result[i][j] = max(result[i-1][j], result[i-1][j-w[i-1]]+v[i-1])
    return result

def main():
    start = time.time()
    result = backpack(number, capacity, weight, profit)
    end = time.time()
    print("\n\n***动态规划算法***")
    print("共耗时：" + str(end - start) + "s")
    print("最优解：" + str(result[number][capacity]))
    print("所选取的物品为：")
    item = [0 for i in range(number+1)]
    j = capacity
    for i in range(1, number+1):
        if result[i][j] > result[i-1][j]:
            item[i-1] = 1
            j -= weight[i-1]
    for i in range(number):
        if item[i] == 1:
            print(str(i+1), end=" ")
            
if __name__ == '__main__':
    main()

plt.figure(figsize=(8,6), dpi=80)
plt.scatter(weight,profit,s=20)
plt.xlabel("Weight", fontsize=12,color="r")
plt.ylabel("Profit",fontsize=12, color='r')
plt.show()

