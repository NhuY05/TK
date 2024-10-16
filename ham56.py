# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:17:44 2024

@author: Vivobook
Áp dụng kỹ thuật kwargs, *args, ** kwargs thiết kế hàm tính chu vi, diện
tích hình vuông, hình chữ nhật, hình tròn theo các phương pháp gọi hàm
sau:
tinh(10, hinh='vuong', tinh='cv')
tinh(50, hinh='vuong', tinh='dt')
tinh(18, hinh='tron', tinh='cv')
tinh(20, 30, hinh='chu_nhat', tinh='cv')
"""

import math

def tinh(*args, **kwargs):
    hinh = kwargs.get('hinh')
    loai_tinh = kwargs.get('tinh')
    
    if hinh == 'vuong':
        canh = args[0]
        if loai_tinh == 'cv':
            return 4 * canh  # Chu vi hình vuông
        elif loai_tinh == 'dt':
            return canh ** 2  # Diện tích hình vuông

    elif hinh == 'chu_nhat':
        dai = args[0]
        rong = args[1]
        if loai_tinh == 'cv':
            return 2 * (dai + rong)  # Chu vi hình chữ nhật
        elif loai_tinh == 'dt':
            return dai * rong  # Diện tích hình chữ nhật

    elif hinh == 'tron':
        ban_kinh = args[0]
        if loai_tinh == 'cv':
            return 2 * math.pi * ban_kinh  # Chu vi hình tròn
        elif loai_tinh == 'dt':
            return math.pi * ban_kinh ** 2  # Diện tích hình tròn

if __name__ == '__main__':#
    print(tinh(10, hinh='vuong', tinh='cv'))   Chu vi hình vuông cạnh 10
    print(tinh(50, hinh='vuong', tinh='dt'))  # Diện tích hình vuông cạnh 50
    print(tinh(18, hinh='tron', tinh='cv'))   # Chu vi hình tròn bán kính 18
    print(tinh(20, 30, hinh='chu_nhat', tinh='cv'))  # Chu vi hình chữ nhật 20x30