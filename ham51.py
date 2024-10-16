# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:36:17 2024

@author: Vivobook
Viết hàm kiểm tra giá trị nhập vào phải thuộc đoạn [-89, 90], nếu sai bắt
nhập lại.
"""

def ktgt():
    while True:
        gtri = input("Nhập giá trị (trong khoảng [-86, 90]): ")
        try:
            gtri = float(gtri)
            if -86 <= gtri <= 90:
                return gtri
            else:
                print("Giá trị không hợp lệ, vui lòng nhập lại.")
        except ValueError:
            print("Đầu vào không hợp lệ, vui lòng nhập một số.")

if __name__ == "__main__":
    print(ktgt())

def ktgt():
    gt=input("nHập:")
    if gt.strip("-").isdigit():
        gt=int(gt)
        if -98<=gt<=90:
            return gt
        print("khl")
        return(ktgt())
if __name__ == "__main__":
    print(ktgt())
    

