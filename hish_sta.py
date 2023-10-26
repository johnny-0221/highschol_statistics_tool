import statistics
import math
#前処理用
def fun_one(l):
        return [i*2 for i in l]
#平均、分散、標準偏差を出力する関数(一変量用)
def process_var(l_data):
    print("変換前のデータ")
    print("平均:"+str(statistics.mean(l_data)))
    print("分散:"+str(statistics.pvariance(l_data)))
    print("標準偏差:"+str(statistics.pstdev(l_data)))
    print("変換後のデータ")
    print("平均:"+str(statistics.mean(l_data)))
    print("分散:"+str(statistics.pvariance(l_data)))
    print("標準偏差:"+str(statistics.pstdev(l_data)))
#共分散、相関係数を出力する関数(二変量用)
def process_cov(l_data_square):
    #rは相関係数
    x_avl=statistics.mean(l_data_square[0])
    y_avl=statistics.mean(l_data_square[1])
    #devpは偏差積を入れていくリスト
    devp=[]
    for i in range(len(l_data_square[0])):
        devp.append((l_data_square[0][i]-x_avl)*(l_data_square[1][i]-y_avl))
    #covは共分散
    cov=(sum(devp)/len(devp))
    #rは相関係数
    r=(cov/math.sqrt(statistics.pvariance(l_data_square[0])*statistics.pvariance(l_data_square[1])))
    print("共分散:"+str(cov))
    print("相関係数:"+str(r))
#一変量実行用
if True:
    process_var([int(i)for i in input("変量を入力>>").split((",")or(" "))])
#二変量実行用
if True:
    l_data_square_real=[[0],[0]]
    l_data_square_real[0]=[int(i)for i in input("１つ目の変量を入力>>").split((",")or(" "))]
    l_data_square_real[1]=[int(i)for i in input("２つ目の変量を入力>>").split((",")or(" "))]
    process_cov(l_data_square_real)