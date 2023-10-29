import numpy as np
import matplotlib.pyplot as plt
#前処理用
def vary(l):
        return [i*2 for i in l]
#平均、分散、標準偏差を出力する関数(一変量用)
def process_var(l_data):
    print("変換前のデータ")
    print("平均:"+str(np.mean(l_data)))
    print("分散:"+str(np.var(l_data)))
    print("標準偏差:"+str(np.std(l_data)))
    print("変換後のデータ")
    print("平均:"+str(np.mean(vary(l_data))))
    print("分散:"+str(np.var(vary(l_data))))
    print("標準偏差:"+str(np.std(vary(l_data))))
#共分散、相関係数を出力する関数(二変量用)
def process_cov(x,y):
    if x.ndim==y.ndim==1 and x.size==y.size:
        cov=np.sum((x-np.mean(x))*(y-np.mean(y)))/x.size
        print("共分散:"+str(cov))
        print("標準偏差:"+str(cov/(np.std(x)*np.std(y))))
        print("散布図を出力...")
        plt.scatter(x,y)
        plt.show()
#一変量実行用
if True:
    input_list=[int(i)for i in input("変量を入力>>").split((",")or(" "))]
    numpy_list=np.array(input_list)
    process_var(numpy_list)
#二変量実行用
if True:
    input_list_x=[int(i)for i in input("１つ目の変量を入力>>").split((",")or(" "))]
    input_list_y=[int(i)for i in input("２つ目の変量を入力>>").split((",")or(" "))]
    process_cov(np.array(input_list_x),np.array(input_list_y))