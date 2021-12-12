import json
import os
import csv

def lihatdata():
  try:
    with open('note.json', 'r') as file:
      data = json.load(file)
      print('''
         
                                        Data Mahasiswa Universitas Jember                             
        +_____________________________________________________________________________________________+''')
      print('')    
      indeks=0
      for user in data['data']:
        indeks += 1
        print(indeks)
        print('        |','NAME: >>>>[', user['nama'] ,'angkatan: ',user['angkatan'],'] - UMUR >>>>[', user['umur'],']')
        print('''        |''''-------------------------------------------------------------------------') 
        print('')

  except:
    print('Data anda belum ada! silahkan buat data baru terlebih dahulu')
    buatData()

def buatData():
  data = {}
  data['data'] = [
    {'nama': input('masukkan nama anda: '), 'umur': input('masukkan umur anda: '), 'angkatan': input('masukkan angkatan berapa: ')}
  ]
  with open('note.json','a') as filebaru:
    json.dump(data,filebaru,indent=4)

def tambah_data(data, filename='note.json'):
  with open(filename, 'w') as p:
    json.dump(data, p, indent=4)

def tambahData():
  with open ('note.json') as file_json:
    data=json.load(file_json)
    change=data['data']
    a={"nama":input('masukkan nama anda: '),"umur":input('masukkan umur lo: '), "angkatan": input('masukkan angkatan: ')}
    change.append(a)
    tambah_data(data)

def program():
  print(''''
  >-----------------------------------------------<
  | Data Mahasiswa Sistem Informasi angkatan 2021 |
  >-----------------------------------------------<
  
  [1] Lihat data
  [2] Tambah data
  [3] Buat data baru
  [4] Hapus data 
  ''')

  jawaban = input("silahkan pilih : ")
  if jawaban == "1" :
    lihatdata()

  elif jawaban == "2" :
    tambahData()
  elif jawaban == "3" :
    buatData()
  else:
    program()
    
program() 
