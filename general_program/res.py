#递归程序 （计算理论作业） 11.13
#1 X+Y
def add(x,y):
    if y==0:
        return x
    else:
        return add(x,y-1)+1

#2 x*y
def mul(x,y):
    if y==1:
        return x
    elif y==0:
        return 0
    else:
        return mul(x,y-1)+x

#3 n!
def fac(x):
    if x==0:
        return 1
    if x==1:
        return x
    if x >=2:
        return fac(x-1)*x
    pass
#4 x^y
def exp(x,y):
    if y==0 and x==0:
        return "无意义"
    elif y==0:
        return 1
    elif x==0:
        return 0
    elif x==1:
        return x
    elif y==1:
        return x
    elif y>=2:
        return exp(x,y-1)*x
    pass

#5 p(x)   前驱函数 非零数讨论
def p(x):
    if x>0:
        return x-1
    else:
        return 0
    pass

#6 x-y
def sub(x,y):
    if x>y:
        return x-y
    else:
        return 0
    pass

#7 |x-y|
def abs(x,y):
    return sub(x,y)+sub(y,x)
    pass

#8 alpha
# x=0 alpha(x)=1 else alpha(x)=0
def alpha(x):
    if x == 0:
        return 1
    else:
        return 0
    pass

#9
#10  受限制条件下原始递归函数证明

#11 d(x,y)
#x=y d(x,y)=0 else d(x,y)=1
def d(x,y):
    if x==y:
        return 0
    else:
        return 1
    pass

#12  与11一致  x=y

#递归程序11.15
#13 x>y
def bigger(x,y):
    a = alpha(sub(x,y))
    if a==0 :
        return True
    elif a==1:
        return False
    else:
        return "Wrong!"
    pass

#14 x<=y
def smaller_equal(x,y):
    a=bigger(x,y)
    if a :
        return False
    else:
        return True
    pass

#15 y|x
def div(x,y):
    for i in range(x):
        if mul(y,i)==x:
            return True
    return False

#16 [y|x]
def exact_divide(x,y):
    for i in range(x):
        if bigger(mul(y,i+1),x):
            return i
    return "wrong!"

#17 prim(x)
def prim(x):
    if x>1:
        for i in range(2,x):
            if div(x,i):
                return False
        return True
    else:
        return "wrong"

#18 Pi(x)
def pi(x):
    if x==0:
        return 0
    if x==1:
        return 2
    temp=pi(x-1)+1
    temp_last=fac(temp)+1
    for i in range(temp,temp_last):
        if prim(i)==True:
            return i
    return "wrong!"

#19 r(x,y) x除以y的余数
def R(x,y):
    a=exact_divide(x,y)
    return sub(x,mul(y,a))

#20 th(X) x的素因子分解中非零指数个数
def th(x,y):
    if y==0:
        return 0
    if  (div(x,pi(y))):
        return th(x,y-1)+1
    else:
        return th(x,y-1)
def T(x):
    if prim(x):
        return th(x,x)-1
    else:
        return th(x,x)

#21 xi(x,i) x素因子分解中的第i个素数的指数
def xi(x,i):
    if div(x,pi(i)):
        return xi(exact_divide(x,pi(i)),i)+1
    else:
        return 0

#22 Lt(x) x的素因子分解中，非0指数的最大序号
def Lt(x):
    tmp=0
    for i in range(1,x):
        if div(x,pi(i)):
            tmp=i
    return tmp

#23 GN(x) 所有的i<-Lt(x) 且 xi！=0 时为真
def GN(x):
    tmp=Lt(x)+1
    print(tmp)
    for i in range(1,tmp):
        if xi(x,i)==0:
            return False
    return True

#24 [a1,a2,...,an] 哥德尔数
def godel(x):
    tmp=[]
    temp=Lt(x)+1
    for i in range(1,temp):
        temp_xi=xi(x,i)
        tmp.append(temp_xi)
    return tmp

#25 godel X*Y godel数的乘法
def godel_x_y(x,y):
    tmp_x = godel(x)
    tmp_y = godel(y)
    tmp=tmp_x+tmp_y
    return tmp
#xy是list
def godel_xy(x,y):
    tmp = x+y
    return tmp

#26 #(a,x) x的素因子中指数时a的素因子个数
def F(a,i,x):
    if i==0:
        return 0
    if xi(x,i)==a:
        return F(a,i-1,x)+1
    else:
        return F(a,i-1,x)
def ax(a,x):
    return F(a,x,x)

#27 28 29 是康托对数
#27 cantor(x,y)  a(x,y)表示的数
def cantor(x,y):   #hava problem
    return (x+y)*(x+y+1)/(2+y)
# 27 递归正确
def cantor_res(x,y):
    if x==0 and y==0:
        return 0
    if x>0:
        return cantor_res(x-1,y)+x+y
    if y>0:
        return cantor_res(x,y-1)+x+y+1

# 28 cantor_r(x,y) =y  h(n)=z-y z=<x,y> n=x+y h(n+1)=h(n)+n+1
#证明 h(n)<=z<h(n+1)
def cantor_rr(x,y):
    tmp_xy = cantor_res(x,y)
def add_oneself(x):
    if x==0:
        return x
    else:
        return add_oneself(x-1)+x
def cantor_r(x,y):
    tmp_xy=cantor_res(x,y)
    for i in range(tmp_xy):
        hn = add_oneself(i)
        hn1=add(add(hn,i),1)
        if smaller_equal(hn,tmp_xy) and bigger(hn1,tmp_xy):
            hn=add_oneself(i)
            return sub(tmp_xy,hn)
    return False
#28 返回康拓对数分解右边   true 修改版本
def cantor_r(x):
    temp = x
    for i in range(x):
        hn=add_oneself(i)
        hn1=add(add(hn,i),1)
        if smaller_equal(hn,temp) and bigger(hn1,temp):
            return sub(temp,hn)
    return 0
#29 cantor_L(x,y)=x
def cantor_l(x,y):
    tmp_xy=cantor_res(x,y)
    for i in range(tmp_xy):
        hn = add_oneself(i)
        hn1=add(add(hn,i),1)
        if smaller_equal(hn,tmp_xy) and bigger(hn1,tmp_xy):
            return i - cantor_r(x,y)
    return False
    pass
#29 cantor_l(x)  返回康拓对数分解左边 修改版本
def cantor_l(x):
    temp = x
    for i in  range(x):
        hn = add_oneself(i)
        hn1= add(add(hn,i),1)
        if smaller_equal(hn,temp) and bigger(hn1,temp):
            return i-cantor_r(x)
    pass

#30 prom（x)
def prom(x):
    ltx = Lt(x)
    res = True
    list_temp=[]
    for i in range(1,ltx+1):
        temp_xi = xi(x,i)
        if cantor_r(temp_xi) ==0:
            res = False
            return res
        temp_xi_l = cantor_l(temp_xi)
        if  temp_xi_l != 0:
            if temp_xi_l in list_temp:
                res =False
                return res
            else:
                list_temp.append(temp_xi_l)
    return res
    pass
#对单个输入数据x的处理
def tape_temp(xn):
    tape_list =[]
    for i in range(xn):
        tape_list.append(2)
    tape_list.append(2)
    return tape_list
    pass
	
#整合所有输入数据 形成一个输入数据的纸带 2和1组成
def tape(xn):
    temp_list = []
    for i in xn:
        xn_i = int(i)
        tape_temp_list = tape_temp(xn_i)
        temp_list = godel_xy(temp_list,tape_temp_list)
        if i !=xn[-1]:
            temp_list.append(1)
    return temp_list

	
#对指令计数器的操作i_number
def op_i_number():
	pass
#对带上计数器的操作v_number
def op_v_number():
	pass
#对纸带的右移操作
def right(z,x,v_number)：
	pass
#对纸带的左移操作
def left():
	pass
#对纸带的写1操作(其实是写2)
def wirte_1():
	pass
#对纸带的写b操作（其实是写1）
def write_b():
	pass
#右边大于4的奇数
#to ai if b  2*i+3=right_number 不是b则顺序执行
def odd_4():
	pass
#to ai if 1 2*i+4 = right_number 不是1则顺序执行
#右边大于4的偶数
def even_4():
	pass
#执行pt-程序  z是t程序的哥德尔数 x是操作纸带
#康拓对数 左边不为0 则调到对应标号编码为0 执行右边对应的操作  则顺序执行i_number++
#         左边为0  则按照右边的编码执行 或者完成跳转 
def conduct(z,x):
    ltz=Lt(z)
    godel_z = godel(z)
    i_number = 1 #指令计数器
    v_number = 1 #带上计数器
    while i_number>=1 and i_number<=ltz:
		temp_cantor_r_z = cantor_r(xi(z,i_number))
		if temp_cantor_r_z == 1:
			#调用右移
			pass
		elif temp_cantor_r_z == 2:
			#调用左移
			pass
		elif temp_cantor_r_z == 3:
			#写1
			pass
		elif temp_cantor_r_z == 4:
			#写b
			pass
		elif R(temp_cantor_r_z,2)== 1:
			# 奇数 指令为to ai if b
			pass
		else:
			# 偶数 指令为to ai if 1
			pass
    pass
#主函数
def main():
    # print(prom(60))
    z = int(input("代表程序的哥德尔数z："))
    xn = input("程序的输入数据:(空格为界)")
    xn_list = xn.split()
    input_tape_x =tape(xn_list)
    print(input_tape_x)
    if prom(z):
        couduct(z,x)
    else:
        print( "bad godel number!")

    pass
if __name__=='__main__':
    main()
#test 各个阶段
#x+y
    #print("x+y")
    #print(add(3,0),add(0,3),add(2,3))
#x*y
    #print("x*y")
    #print(mul(3,0),mul(0,3),mul(2,3))
#n!
    # print("n!")
    # print(fac(0),fac(1),fac(5))
# x^y
     # print("x^y")
     #  print(exp(2,0),exp(3,3),exp(0,0),exp(0,2),exp(1,3),exp(3,1))
#p(x)
    # print("前驱函数p(x)")
    #print(p(0),p(3))
#x-y
    # print("x-y")
    # print(sub(3,4),sub(4,3))
#|x-y|
    #print("|x-y|")
    #print(abs(3,4),abs(8,4))
#alpha
    # print("alpha(x)")
    # print(alpha(3),alpha(0))
#9
#10
#11d(x,y)
    # print("d(x,y)")
    # print(d(2,3),d(3,3))

#12 与11一致
#13 x>y
    # print("x>y")
    # print(bigger(5,4),bigger(4,5))
#14 x<=y
    # print("x<=y")
    # print(smaller_equal(4,5),smaller_equal(4,4),smaller_equal(5,4))
#15 y|x
    # print("y|x")
    # print(div(6,3),div(6,4))
#16[y|x]
    # print("[y|x]")
    # print(exact_divide(18,4),exact_divide(18,6))
#17prim(x)
    # print("prim(x)")
    # print(prim(7),prim(23),prim(21))

#18 pi(x)
    # print("pi(x)")
    # print(pi(9),pi(10))

#19 r(x,y)
    # print("r(x,y)")
    # print(R(18,4),R(18,3))
#20 T(x)
    # print("T(x)")
    # print(T(20),T(23))
#21 xi(x,i)
    # print("xi(x,i)")
    # print(xi(20,1),xi(120,6))
#22 Lt(x)
    # print("Lt(x)")
    # print(Lt(9),Lt(8))
#23 GN(x)
    # print("GN(x)")
    # print(GN(8),GN(9))
#24 godel(x)
    # print("godel(x)")
    # print(godel(9),godel(20))
#25 godel_x_y
    # print("godel_x_y(x,y)")
    # print(godel_x_y(9,20))
#26 ax(a,x)
    # print("ax(a,x)")
    # print(ax(2,20),ax(1,9))
#27 cantor(x,y)
    # print("cantor(x,y)")
    # print(cantor(5,0),cantor(0,5),cantor_res(5,0),cantor_res(0,5))
#28 cantor_r(x,y)
    # print("cantor_r(x,y)")
    # print(cantor_r(4,5),cantor_r(8,6))
#29cantor_l(x,y)
    # print("cantor_l(x,y)")
    # print(cantor_l(4,5),cantor_l(8,6))
