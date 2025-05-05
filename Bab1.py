import math
import matplotlib.pyplot as peta
from collections import Counter
import pandas as pd
import seaborn as sns


#Nilai Final Exam Statistika Elementer
dataD = [
    23, 60, 79, 32, 57, 74, 52, 70, 82, 36,
    80, 77, 81, 95, 41, 65, 92, 85, 55, 76,
    52, 10, 64, 75, 78, 25, 80, 98, 81, 67,
    41, 71, 83, 54, 64, 72, 88, 62, 74, 43,
    60, 78, 89, 76, 84, 48, 84, 90, 15, 79, 
    34, 67, 17, 82, 69, 74, 63, 80, 85, 61
    ]


#Nilai 
dataC = [
    2.2, 4.1, 3.5, 4.5, 3.2, 3.7, 3.0, 2.6, 3.4, 1.6,
    3.1, 3.3, 3.8, 3.1, 4.7, 3.7, 2.5, 4.3, 3.4, 3.6,
    2.9, 3.3, 3.9, 3.1, 3.3, 3.1, 3.7, 4.4, 3.2, 4.1,
    1.9, 3.4, 4.7, 3.8, 3.2, 2.6, 3.9, 3.0, 4.2, 3.5
    ]



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

def mode(totalData):
    frekuensi = {}
    for angka in totalData:
        frekuensi[angka] = frekuensi.get(angka, 0) + 1

    maksFrekuensi = max(frekuensi.values())
    modusList = [angka for angka, jumlah in frekuensi.items() if jumlah == maksFrekuensi]

    return modusList


#Coding untuk median
def median(totalData) :
    totalData.sort()
    if len(totalData) % 2 != 0 :
        lenBAngka = int((len(totalData) - 1) / 2)
        return totalData[lenBAngka]

    elif len(totalData) % 2 == 0 :
        lenBAngka1 = int(len(totalData)/ 2) - 1
        lenBAngka2 = int(len(totalData)/ 2)
        hasilMean  = (totalData[lenBAngka1] + totalData[lenBAngka2]) / 2
        return hasilMean



#Coding untuk nilai min
def nilaiMin(totalData) :
    totalData.sort()
    return totalData[0]

#Coding untuk nilai max
def nilaiMax(totalData) :
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
def jumlah(totalData) :
    jumlah = 0
    for angka in totalData :
        jumlah = jumlah + angka
    return jumlah



# Visual



def tabelFrekuensi(totalData) :
    freq_table = pd.Series(totalData).value_counts().sort_index()
    freq_df = pd.DataFrame({'Nilai': freq_table.index, 'Frekuensi': freq_table.values})
    print(freq_df)

def histogram(totalData) :
    peta.hist(totalData,edgecolor='black')
    peta.title('Histogram')
    peta.xlabel('Nilai')
    peta.ylabel('Frekuensi')
    peta.show()


def barChart(totalData) :
    freq_table = pd.Series(totalData).value_counts().sort_index()
    freq_table.plot(kind='bar', color='skyblue', edgecolor='black')
    peta.title('Bar Chart')
    peta.xlabel('Nilai')
    peta.ylabel('Frekuensi')
    peta.xticks(rotation=0)
    peta.grid(axis='y')
    peta.show()

def pieChart(totalData) :
    freq_table = pd.Series(totalData).value_counts().sort_index()
    freq_table.plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap='Set3')
    peta.title('Pie Chart')
    peta.ylabel('')
    peta.show()

def boxplot(totalData) :
    sns.boxplot(y=totalData)
    peta.title('Boxplot')
    peta.ylabel('Nilai')
    peta.grid(True)
    peta.show()

def stemPlotD(totalData) :
    totalData.sort()

    stem_leaf = {}

    for nomor in totalData:
        stem = nomor // 10
        leaf = nomor % 10
        stem_leaf.setdefault(stem, []).append(leaf)

    
    for stem, leaves in stem_leaf.items():
        leaf_str = ' '.join(str(leaf) for leaf in leaves)
        print(f"{stem} | {leaf_str}")

def stemPlotC(totalData) :
    totalData = [round(num, 1) for num in totalData]
    totalData.sort()

    stem_leaf = {}

    for number in totalData:
        stem = int(number)
        leaf = int(round((number - stem) * 10))  
        stem_leaf.setdefault(stem, []).append(leaf)

    print("Stem | Leaf")
    print("------------")
    for stem in sorted(stem_leaf):
        leaves = ' '.join(str(leaf) for leaf in stem_leaf[stem])
        print(f" {stem}   | {leaves}")

