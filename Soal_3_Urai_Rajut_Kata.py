###SOAL UJIAN 3###
'''
Buatlah sebuah file python yang berisi 2 buah return function, dengan 1 argumen yang dapat digunakan untuk mengurai & merajut sebuah string.

fungsi urai(...) akan mengurai string. contoh output yang diharapkan adalah sebagai berikut:

# Function Initialization :
def urai(...):
    ......
 
def rajut(...):
    ......
    
    
# Use the function

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

# Output:
CCoCodCode
PPyPytPythPythoPython
PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika
Sedangkan fungsi rajut(...) akan merajut kembali string yang terurai menjadi bentuk kata asalnya. contoh output yang diharapkan adalah sebagai berikut:

# Use the function

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# Output:

Code
Python
Purwadhika
'''

def urai(kata):
    kata_urai = ''
    for i in range(len(kata)):
        for j in range(i+1):    # Menggunakan looping untuk mengambil index
            kata_urai = kata_urai + kata[j]
    return kata_urai

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

print ("=" * 50)

def rajut (kata):
    kata_rajut = []
    panjangkata = len(kata)
    for i in range(50):
        huruf = int(i*(i+1)/2) # Mengetahui urutan keberapa dari huruf pertama yang akan diambil
        kata_rajut.append(huruf)    # Urutan tersebut dimasukkan kedalam list, agar mudah indexing

        if panjangkata in kata_rajut:
            indexhuruf = kata_rajut.index(panjangkata) # Mengetahui index keberapa hasil panjang kata tersebut
            # print(indexloncat)
            total = panjangkata - indexhuruf # Mengetahui index keberapa kata yang paling lengkap
            print(total)
            return kata[(total):] # Mengambil kata paling terakhir karena paling lengkap, dimulai dari huruf pertama hingga terakhir [(total):] 

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))