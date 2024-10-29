import numpy as np 
arr_a = np.array([1,2,3,2,3,4,3,4,5,6])
arr_b = np.array([7,2,10,2,7,4,9,4,9,8])
print("arr a:",arr_a)
print("arr b:",arr_b)

phan_tu_chung = []
for i in arr_a:
    if i in arr_b and i not in phan_tu_chung:
        phan_tu_chung.append(i)
arr_c = np.array(phan_tu_chung)
print("arr c gồm các phần tử ở cả arr a và arr b là:",arr_c)   

phan_tu_arra = []
for i in arr_a:
    if i not in arr_b:
        phan_tu_arra.append(i)
arr_d = np.array(phan_tu_arra)
print("arr d chứa các phần tử chỉ xuất hiện ở arr a là:")            

arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
print("arr_e:",arr_e)
arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]
print("arr_f chứa các phần tử có giá trị từ 5 đến 10 của arr_e là arr_f:", arr_f)