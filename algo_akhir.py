import json
import os
import csv

def lihatdata():
  try:
    with open('note.json', 'r') as file:
      data = json.load(file)
      print('''
         
                             Data Mahasiswa Prodi Sistem Informasi Universitas Jember                             
        +____________________________________________________________________________________________________________________+''')
      print('')    
      indeks=0
      for user in data['data']:
        indeks += 1
        print(indeks)
        print('        |','NAMA: >>>>[', user['nama'] ,'] - NIM: [',user['nim'],'] - Tempat tanggal lahir: >>>>[', user['ttl'],'] - Asal: >>>>[',user['asal'],']')
        print('''        |''''-----------------------------------------------------------------------------------------------------------------------') 
        print('')

  except:
    print('\nData anda belum ada! silahkan buat data baru terlebih dahulu\n')
    buatData()

def buatData():
  data = {}
  data['data'] = [
    {"nama":input('Masukkan nama lengkap anda: '),"nim":input('Masukkan NIM anda: '), "ttl": input('Masukkan Tempat tanggal lahir anda: '), 'asal': input('Masukkan asal daerah anda: ')}
  ]
  with open('note.json','a') as filebaru:
    json.dump(data,filebaru,indent=5)

def tambah_data(data, filename='note.json'):
  with open(filename, 'w') as p:
    json.dump(data, p, indent=5)

def tambahData():
  with open ('note.json') as file_json:
    data=json.load(file_json)
    change=data['data']
    a= {"nama":input('Masukkan nama lengkap anda: '),"nim":input('Masukkan NIM anda: '), "ttl": input('Masukkan Tempat tanggal lahir anda: '), 'asal': input('Masukkan asal daerah anda: ')}
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
