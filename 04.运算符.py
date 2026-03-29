#算术运算符 + - * / // % **
# print("10 + 4 =",10 + 4 )#加
# print("10 - 4 =",10 - 4 )#减
# print("10 * 4 =",10 * 4 )#乘
# print("10 / 4 =",10 / 4 )#除,结果小数
# print("10 // 4 =",10 // 4 )#整除(结果为整数)
# print("10 % 4 =",10 % 4 )#取余/求模
# print("10 ** 4 =",10 ** 4 )#幂指数,10的4次幂

#算术运算符的优先级 ---> ** ---> * / // % ---> + -

#案例
# x = float(input("请输入x的值:"))
# y = int(input("请输入y的值:"))
# #可能精度损失,计算机底层原因,正常
# # 输入input()是字符串str类型,使用 int() float() 转换成int float 类型
# # print("x + y =",float(x)+int(y))
# # print("x - y =",float(x)-int(y))
# print("x + y =",x + y)
# print("x - y =",x - y)

#案例1 计算3个整数的平均数
# num1 = int(input("请输入第一个整数:"))
# num2 = int(input("请输入第二个整数:"))
# num3 = int(input("请输入第三个整数:"))
# print("平均数:",(num1 + num2 + num3)/3)

#案例2 求梯形的面积
# upper_base = float(input("请输入梯形上底的长度:"))
# lower_base = float(input("请输入梯形下底的长度:"))
# height = float(input("请输入梯形的高:"))
# print("梯形的面积:",(upper_base + lower_base) * height /2)

#案例3 计算圆的周长和面积
# r = float(input("请输入圆的半径:"))
# #Π的值设定为3.14
# print(f"圆的周长{2 * 3.14 * r}\n圆的面积{3.14 * r ** 2}")

#案例4 计算身体质量指数BMI
# body_weight = float(input("请输入体重(单位kg):"))
# height = float(input("请输入身高(单位m):"))
# print(f"BMI:{body_weight / height ** 2:.2f}")#:.2f表示保留2位小数(四舍五入) :.nf表示保留n位

#赋值运算符 = += -= *= /= //= %= **=
# num = 85

# num += 10
# print("num += 10后,num=",num)#95
#
# num -= 10
# print("mum -= 10后,num=",num)#85
#
# num *= 10
# print("num *= 10后,num=",num)#850
#
# num /= 10
# print("num /= 10后,num=",num)#85.0  除法转换成浮点数

# num //= 10
# print("num //= 10后,num=",num)#8.0

# num %= 10
# print("num %= 10后,num=",num)#8.0
#
# num **= 2
# print(f"num **= 10后,num={num}")#64.0

#比较运算符 == != > >= < <=
# print("100 == 100 吗?", 100 == 100)#True
# print("'100' == '100'吗?", "100" == "100")#Trur
# print("'100' == 100 吗?", "100" == 100)#False
# print("100 != 100吗?", 100 != 100)#False
# print("100 > 100吗?", 100 > 100)#False
# print("100 >= 100吗?", 100 >= 100)#True
# print("100 < 100吗?", 100 < 100)#False
# print("100 <= 100吗?", 100 <= 100)#True

#逻辑运算符 and or not
#案例1 判断键盘输入的一个数是否在10--20之间
# num = float(input("请输入一个数:"))
# # print("在10--20之间:", 10 <= num <= 20)
# print("在10--20之间:", num >= 10 and num <= 20)

#案例1 判断键盘输入的一个数是否不在10--20之间
num = float(input("请输入一个数:"))
# print("在10--20之间:", 10 <= num <= 20)
print(f"{num}不在10--20之间:", num < 10 or num > 20)