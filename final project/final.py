import random

def run():
    a=[]                    #随机一个4位数字
    x=range(10)             
    for i in range(4): 
        a+=str(x.pop(random.randrange(10-i)))    #从10个数字里选4个
    b=set(a)                #用于判断猜中几个数
    end=True                #开始猜循环
    t=0                     #累计猜的次数
    while end:
        A=0                 #数字位置都正确
        C=0                 #数字猜中数
        while True:             
            c=raw_input('input four number:')
            if c in ['i love you']: #作弊
                print("Thank you! the answer is {0}".format(a))
                continue
            elif len(c)!=4:
                print('Four number,please!')
                continue
            elif len(set(c))!=4:
                print('Four different number,ok?')
                continue
            else: 
                break
        for i in range(4):
            if c[i]==a[i]:
                A+=1
            if c[i] in b:
                C+=1
        t+=1
        if A==4:
            print("Congratulations!You've just got it ".format(t))
            end=False       #结束游戏
        else:
            print("{0:2d}A{1:2d}B".format(A,C-A)) #给提示。（C-A即猜中但位置不对的数）
           
            if t==11:
                print("If you need help,just say'i love you' ")


run()
