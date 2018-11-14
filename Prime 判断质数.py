while True:
    n = input('Please input a *natural number*: ')
    #一般来说数论中的自然数不包括0，但本程序中的自然数默认包含0
    if n.isdigit():
        break
    #isdigit（）检测输入是否只由数字组成
    else:
        print(n,' is not a *natural number*')
'''
使用While循环保证输入的值为纯数字
'''
n = int(n)
'''
input输入的数据类型为str，只有将其转换为int型才能继续以下操作
'''
if n < 2:
    print(n,' is not a prime number')
#0和1都不是质数
elif n == 2:
    print('2 is a prime number')
#2是质数，但为了以下循环能够完美运行，故将2单独做一个判断
else:
    for i in range(2, n):
    #当n大于等于2时进入循环
        if n % i == 0:
            print(n,' is not a prime number')
            print(n, '=', i,'*', int(n/i), sep=' ')
            break
        #若n有除1和n本身以外的因数，则n必为合数
        else:
            i += 1
        if i == n:
            print(n,' is a prime number')
            break
        #当i=n时退出循环并输出n为质数
'''
根据质数的定义
若自然数n除以（2，n-1）范围内所有自然数，其余数都不为零
则n必为素数
'''
