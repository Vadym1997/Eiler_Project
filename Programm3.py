# def gcd(number):
#     A = []
#     for divisor in range(number//2,int(number**(1/2)-1),-1):
#         if number % divisor == 0:
#             A.append(divisor)
#     return A
#
#
# print(gcd(6008588))
# import math
# def issimple(a):
#     r=math.ceil(math.sqrt(a))
#     lst=[]
#     for i in range(2,r):
#         if a%i==0:
#             if issimple(i)==[]:
#                 lst.append(i)
#     return lst
# r=issimple(600851475143)
# print(max(r))
# print(r)
factor=2
num=6008514751432
for factor in range (2,num):
    if num<=factor:
        break
    if num%factor==0:
        num=num/factor
print(factor)