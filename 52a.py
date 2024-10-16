# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:39:57 2024

@author: Vivobook
"""

def canbac(n, x):
    return n **(1/x)
#b trả về số đảo
def sodao(n):
    return int(str(n)[::-1])
#c kiểm tra số chính phương
import math
def ktchinhphuong(n):
    return math.sqrt(n)==int(math.sqrt(n))
#d kiểm tra số nguyên tố:
def ktnguyento(n):
    if n<=2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
#e tích các số lẻ
def tichcacsole(n):
    tich=1
    m=0
    while n>0:
        m=n%10
        if m%2!=0:
            tich*=m
        n=n//10
    return tich
#f tông số nguyên tố
def tongnguyento(n):
    tong=1
    for i in range(2,n):
        tong +=i
    return tong
#g tổng chính phương nhỏ hơn n
def tongchinhphuong(n):
    tong=1
    for i in range(1,n):
        if math.isqrt(i)**2==i:
            tong+=i
    return tong
#h tổng số dương
def tongsoduong(n):
    tong=0
    for i in range(1, n+1):
        if n%i==0:
            tong+=i
    return tong


if __name__=="__main__":
    print(canbac(8, 3))
    print(sodao(6))
    print(ktchinhphuong(7))
    print(ktnguyento(13))
    print(tichcacsole(1235))
    print(tongnguyento(579))
    print(tongchinhphuong(17))
    print(tongsoduong(12))