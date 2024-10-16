# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:31:49 2024

@author: Vivobook
Viết phương thức kiểm tra một số nhập vào là số chẵn có giá trị âm. Đúng
trả về true. Sai trả về false.
"""

def ktso(n):
    return n<0 and n%2==0
if __name__=="__main__":
    n=float(input("Nhập n: "))
    print(ktso(n))


        