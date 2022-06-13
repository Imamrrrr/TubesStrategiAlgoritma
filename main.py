import pandas as pd
import time

data = pd.read_excel("./TUBES_SA/test.xlsx")
arr_data = data.values.tolist()

def bruteforce(x): #fungsi brute force sequential search 
    promising = []
    for val in arr_data:
        if x >= val[2]:
            promising.append(val)

    return promising

# prosedur untuk nggabungin array kiri dan kanan secara terurut
def merge(arr, left, mid, right): 
    n1 = mid - left + 1
    n2 = right - mid

    #menyimpan array sementara untuk data kiri dan kanan
    L = [0] * (n1)
    R = [0] * (n2)

    #untuk masukin data sebelah kiri ke data temporary
    for i in range(n1):
        L[i] = arr[left+i]

    #untuk masukin data sebelah kanan ke data temporary
    for j in range(n2):
        R[j] = arr[mid+1+j]

    #iterasi saat memasukkan data yang sudah dibandingkan 
    i = 0
    j = 0
    k = left

    
    while i < n1 and j < n2:
        if L[i][2] < R[j][2]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = left+(right-left)//2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)

def binarySearch(x):
    if x <= arr_data[0][2]:
        return 0
    if x >= arr_data[len(arr_data)-1][2]:
        return len(arr_data)-1
    
    i = 0
    j = len(arr_data)
    mid = 0
    while i < j:
        mid = (i+j)//2

        if arr_data[mid][2] == x:
            return mid
        
        if x <= arr_data[mid][2]:
            if mid > 0 and x >= arr_data[mid-1][2]:
                return closest(mid-1, mid, x)
            j = mid
        else:
            if mid < len(arr_data)-1 and x <= arr_data[mid+1][2]:
                return closest(mid, mid+1, x)
            i = mid+1
    return mid

def closest(a, b, x):
    if x-arr_data[a][2] >= arr_data[b][2]-x:
        return b
    else:
        return a

p = int(input("Masukkan Jumlah Uang anda(50-10000: "))

print("====== Brute Force ======")

start_bf = time.time()
bf = bruteforce(p)
for i in range(len(bf)):
    print(bf[i])
stop_bf = (time.time()-start_bf)
print("brute force runtime:", stop_bf)

print("====== Divide and Conquer ======")

start_dac = time.time()
mergeSort(arr_data, 0, len(arr_data)-1)
if arr_data[binarySearch(p)][2] > p:
    dac = arr_data[:binarySearch(p)]
else:
    dac = arr_data[:binarySearch(p)+1]

for i in range(len(dac)):
    print(dac[i])
stop_dac = (time.time()-start_dac)
print(stop_dac)
