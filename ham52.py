# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:39:57 2024

@author: Vivobook
Anh/chị nhập vào một số nguyên dương n và viết các phương thức sau:
a) Phương thức tính căn bậc x của số n
b) Phương thức trả về số đảo.
c) Phương thức kiểm tra có phải là số chính phương.
d) Phương thức kiểm tra có phải là số nguyên tố
e) Phương thức tính tích các chữ số lẻ.
f) Phương thức tính tổng các số nguyên tố nhỏ hơn n
g) Phương thức tính tổng các số chính phương nhỏ hơn n.
h) Phương thức tính tổng các ước số dương của n.
"""

import math
#a
def can(x,n):
    return x ** (1/n)
#b
def sodao(n):
    n = str(n)
    return n[::-1]
#c
def chinhphuong(n):
    return math.sqrt(n)==int(math.sqrt(n))
#d
def nguyento(n):
    if n < 2 :
        return False
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True
#e
def le(n):
    tich = 1
    for i in str(n):
        if int(n) % 2 != 0:
            tich *= int(i)
    return tich
#f
def nguyen_to_nho_hon_n(n):
    tong_nt = 0
    for i in range(2,n):
        if nguyento(i):
            tong_nt += i
    return tong_nt
#g 
def cp_nho_hon_n(n):
    tong_cp = 0
    for i in range(1,n):
        if chinhphuong(i):
            tong_cp += i
    return tong_cp
#h 
def uoc_so_duong(n):
    tong = 0
    for i in range(1,n+1):
        if n % i == 0:
            tong += i
    return tong
if __name__ == "__main__":
    print(can(9,2))
    print(sodao(10))
    print(chinhphuong(9))
    print(nguyento(4))
    print(le(15))
    print(nguyen_to_nho_hon_n(6))
    print(cp_nho_hon_n(10))
    print(uoc_so_duong(10))