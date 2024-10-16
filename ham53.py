# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:05:10 2024

@author: Vivobook
Nhập vào một số nguyên dương n và viết các phương thức sau
a) S = 1 + 2 + 3 +......+ n
b) S = 12 +22 +32 +......+n2
c) S = 1 + 1/2 + 1/3 +......+ 1/n
d) S = 1! + 2! + 3! +......+ n!
e) S = 1 * 2 * 3 *......* n
"""

#a 
def nhap_n(n):
    S = 0
    for i in range(1,n+1):
        S += i
    return S
#b
def nhap_mu(n):
    S = 0
    for i in range(1,n+1):
        S += i**2
    return S
#c 
def nhap_chia(n):
    S = 0
    for i in range(1,n+1):
        S += 1/i
    return S
#d 
def giai_thua(n):
    S = 0
    giaithua = 1
    for i in range(1,n+1):
        giaithua *= i
        S += giaithua
    return S
        
#e
def tinh_nhan(n):
    S = 1
    for i in range(1,n+1):
        S *= i
    return S

if _name_ == "_main_":
    print(nhap_n(2))
    print(nhap_mu(2))
    print(nhap_chia(2))
    print(giai_thua(3))
    print(tinh_nhan(2)) 