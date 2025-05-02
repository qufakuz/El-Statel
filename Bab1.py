import math
import matplotlib.pyplot as peta
from collections import Counter

dataD = [
    10, 15, 17, 23, 25, 32, 34, 36, 41, 41,
    43, 48, 52, 52, 54, 55, 57, 60, 60, 61,
    62, 63, 64, 64, 65, 67, 67, 69, 70, 71,
    72, 74, 74, 74, 75, 76, 76, 77, 78, 78,
    79, 79, 80, 80, 80, 81, 81, 82, 82, 83,
    84, 84, 85, 85, 88, 89, 90, 92, 95, 98
]

dataC = [2.2,4.1,3.5,4.5,3.2,3.7,3.0,2.6,3.4,1.6,3.1,3.3,3.8,3.1,4.7,3.7,2.5,4.3
         ,3.4,3.6,2.9,3.3,3.9,3.1,3.3,3.1,3.7,4.4,3.2,4.1,1.9,3.4,4.7,3.8,3.2,
         2.6,3.9,3.0,4.2,3.5]



#Coding untuk rata-rata atau mean
def rataRata(totalData):
    angka = 0
    for nomor in totalData :
        angka = angka + nomor
    return angka/len(totalData)



#Coding untuk thrimmed mean
def tRataRata(totalData,angka) :
    totalData.sort()
    persen = angka/100
    dataLen = len(totalData)
    tTrim = int(dataLen * persen)
    dataBaru = totalData[tTrim : dataLen-tTrim]
    return rataRata(dataBaru)



#Coding untuk modus
def modus(totalData) :
    bAngkaDanAngka = (0,0)
    for nomor in totalData :
        bAngka = totalData.count(nomor)
        if bAngka > bAngkaDanAngka[0] :
            bAngkaDanAngka = (bAngka,nomor)
    return bAngkaDanAngka[1]



#Coding untuk median
def median(totalData) :
    totalData.sort()
    if len(totalData) % 2 != 0 :
        lenBAngka = int((len(totalData) - 1) / 2)
        return totalData[lenBAngka]

    elif len(totalData) % 2 == 0 :
        lenBAngka1 = int(len(totalData)/ 2)
        lenBAngka2 = int(len(totalData)/ 2) + 1
        hasilMean  = (totalData[lenBAngka1] + totalData[lenBAngka2]) / 2
        return hasilMean



#Coding untuk nilai min
def min(totalData) :
    totalData.sort()
    return totalData[0]

#Coding untuk nilai max
def max(totalData) :
    totalData.sort()
    l = len(totalData) - 1
    return totalData[l]


#Coding untuk range
def range(totalData) :
    totalData.sort()
    bAngka = len(totalData) - 1
    return totalData[bAngka] - totalData[0]



#Coding untuk varians
def varians(totalData) :
    s = 0
    leng = int(len(totalData)-1)
    for nomor in totalData:
        s = s + ((totalData[leng] - rataRata(totalData))**2)
        leng = leng - 1
    return s/(len(totalData)-1)



#Coding untuk standar deviasi atau simpangan baku
def sDeviasi (totalData) :
    s = varians(totalData)
    return math.sqrt(s)



#Coding untuk jumlah
def sum(totalData) :
    jumlah = 0
    for angka in totalData :
        jumlah = jumlah + angka
    return jumlah


#Coding untuk histogram
#peta.hist(data,edgecolor="white")
#peta.xlabel("HP")
#peta.ylabel("Banyak Mobil")
#peta.title("Car Battery Life")

#Coding box plot
#peta.boxplot(data)

#peta.show()

#Coding untuk stem leaf
def stemPlotD(totalData) :
    totalData.sort()

    stem_leaf = {}

    for nomor in totalData:
        stem = nomor // 10
        leaf = nomor % 10
        stem_leaf.setdefault(stem, []).append(leaf)

    # Tampilkan
    for stem, leaves in stem_leaf.items():
        leaf_str = ' '.join(str(leaf) for leaf in leaves)
        print(f"{stem} | {leaf_str}")

def stemPlotC(totalData) :
    totalData = [round(num, 1) for num in totalData]
    totalData.sort()

    stem_leaf = {}

    for number in totalData:
        stem = int(number)
        leaf = int(round((number - stem) * 10))  # ambil angka di belakang koma
        stem_leaf.setdefault(stem, []).append(leaf)

    # Cetak stem plot
    print("Stem | Leaf")
    print("------------")
    for stem in sorted(stem_leaf):
        leaves = ' '.join(str(leaf) for leaf in stem_leaf[stem])
        print(f" {stem}   | {leaves}")

def tabelFrekuensi(totalData) :
    # Hitung frekuensi tiap nilai
    frekuensi = Counter(totalData)

    # Cetak tabel frekuensi
    print("Nilai\tFrekuensi")
    for value in sorted(frekuensi):
        print(f"{value}\t{frekuensi[value]}")

