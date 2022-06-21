
daftarMobil = [{'Nopol':'DK 101', 'Merk' : 'Daihatsu', 'Tipe' : 'Terios', 'Harga':250000, 'Kategori': 'SUV', 'Warna': 'Abu'},
{'Nopol':'DK 501','Merk' : 'Daihatsu', 'Tipe' : 'Sirion', 'Harga':150000, 'Kategori': 'City Car', 'Warna': 'Putih'},
{'Nopol':'DK 301','Merk' : 'Hyundai', 'Tipe' : 'Palisade', 'Harga':300000, 'Kategori': 'SUV', 'Warna': 'Abu'},
{'Nopol':'DK 401','Merk' : 'Mitsubishi', 'Tipe':'Pajero', 'Harga':350000, 'Kategori': 'SUV', 'Warna': 'Hitam'},
{'Nopol':'DK 691','Merk' : 'Toyota', 'Tipe':'Alphard', 'Harga':650000, 'Kategori': 'Luxury', 'Warna': 'Hitam'},
{'Nopol':'DK 601','Merk' : 'Toyota', 'Tipe':'Avanza', 'Harga':200000, 'Kategori': 'MPV', 'Warna': 'Abu'},
{'Nopol':'DK 611','Merk' : 'Toyota', 'Tipe' : 'Innova' , 'Harga':300000, 'Kategori': 'MPV', 'Warna': 'Putih'}, 
{'Nopol':'DK 211','Merk' : 'Suzuki', 'Tipe' : 'Baleno',  'Harga':150000, 'Kategori': 'City Car', 'Warna': 'Hitam'}
]

Keranjang = []

Jembatan = []

def searchmobil(): # Read
    if len(daftarMobil) == 0:
        print('''
============================================================================================
Mohon maaf, stok mobil habis. Silahkan hubungi Call Center kami untuk informasi lebih lanjut
============================================================================================''')
        Read()
    elif len(daftarMobil) > 0:
        InputSearchRead = (input('''
1. Cari Nopol (TNKB)
2. Cari Merk Mobil
3. Cari Kategori Mobil (SUV / MPV / City Car / Luxury)
4. Cari Tipe Mobil
5. Kembali

Masukkan angka Menu yang ingin dijalankan: '''))
        if InputSearchRead == '1':
            InputNopol = (input('''
Masukkan Nopol Mobil yang ingin di sewa: ''')) 
            SearchNopol = (list(filter(lambda data: data['Nopol'] == InputNopol , daftarMobil)))
            if len(SearchNopol) == 0:
                print('''
===============================================
Mohon maaf, mobil yang anda cari tidak tersedia
===============================================''')
            else:
                tampilkanmobil(SearchNopol)
        elif InputSearchRead == '2':
            InputMerk = (input('''
Masukkan Merk Mobil yang ingin di sewa: ''')) 
            SearchMerk = (list(filter(lambda data: data['Merk'] == InputMerk , daftarMobil)))
            if len(SearchMerk) == 0:
                print('''
===============================================
Mohon maaf, mobil yang anda cari tidak tersedia
===============================================''')
            else:
                tampilkanmobil(SearchMerk)
        elif InputSearchRead == '3':
            InputKategori = (input('''
Masukkan Kategori Mobil yang ingin di sewa: '''))
            SearchKategori = (list(filter(lambda data: data['Kategori'] == InputKategori , daftarMobil)))
            if len(SearchKategori) == 0:
                print('''
===============================================
Mohon maaf, mobil yang anda cari tidak tersedia
===============================================''')
            else:
                tampilkanmobil(SearchKategori)
        elif InputSearchRead == '4':
            InputTipe = (input('''
Masukkan Tipe Mobil yang ingin di sewa: '''))
            SearchTipe = (list(filter(lambda data: data['Tipe'] == InputTipe , daftarMobil)))
            if len(SearchTipe) == 0:
                print('''
===============================================
Mohon maaf, mobil yang anda cari tidak tersedia
===============================================''')
            else:
                tampilkanmobil(SearchTipe)
        elif InputSearchRead == '5':
            Read()
        else:
            print('''
=================================
Mohon masukkan angka dengan benar
=================================''')
    searchmobil()

def menampilkandaftarmobil() : # Read
    if len(daftarMobil) == 0:
        print('''
============================================================================================
Mohon maaf, stok mobil habis. Silahkan hubungi Call Center kami untuk informasi lebih lanjut
============================================================================================''')
    elif len(daftarMobil) > 0:
        tampilkanmobil(daftarMobil)
    Read()

def tampilkanmobil(x): # Untuk Umum
    print('Nopol\t| Merk Mobil \t| Tipe     \t| Harga/hari\t| Warna\t| Kategori')
    for i in range(len(x)):
            print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(x[i]['Nopol'], x[i]['Merk'],x[i]['Tipe'],x[i]['Harga'], x[i]['Warna'], x[i]['Kategori']))
            
def tampilkansewa(x): # Delete
    print('Nopol\t| Merk Mobil \t| Tipe     \t| Harga/hari\t| Warna\t| Waktu')
    for i in range(len(x)):
            print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(x[i]['Nopol'], x[i]['Merk'],x[i]['Tipe'],x[i]['Harga'], x[i]['Warna'], x[i]['Waktu']))

def pembayaran(): # Delete
    print("Mobil yang disewa")
    print('Nopol\t| Merk Mobil\t| Tipe     \t| Harga/hari\t| Warna\t| Hari\t| Total Harga')
    total = 0
    for i in Keranjang:
        print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}\t| {}'.format(i['Nopol'], i['Merk'], i['Tipe'], i['Harga'], i['Warna'], i['Waktu'], i['Harga'] * i['Waktu'] ))
        total += i['Harga'] * i['Waktu']
    while True:
        print('Total Yang Harus Dibayar = {}'.format(total))   
        bayarsewa = int(input('Masukkan jumlah uang : '))
        if(bayarsewa > total) :
            kembali = bayarsewa - total
            print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))               
            Keranjang.clear()
            Start()
        elif(bayarsewa == total) :
            print('Terima kasih')
            Keranjang.clear()                
            Start()
        else :
            kekurangan = total - bayarsewa
            print('Uang anda kurang sebesar {}'.format(kekurangan))

def Read():
    InputRead  = (input('''
Daftar Mobil

1. Tampilkan Semua Mobil
2. Cari Mobil
3. Kembali ke Menu Utama
    
Masukkan angka Menu yang ingin dijalankan: '''))

    if(InputRead == '1') :
        menampilkandaftarmobil()
    elif(InputRead == '2') :
        searchmobil()
    elif(InputRead == '3') :
        Start()
    else:
        print('''
=========================================
Mohon masukkan pilihan angka dengan benar
=========================================''')
        Read()
    
def Create():
    InputCreate  = (input('''
Menu Tambah Mobil

1. Pengembalian Mobil
2. Tambah Mobil (Admin Only)
3. Kembali ke Menu Utama
    
Masukkan angka Menu yang ingin dijalankan: '''))
    if InputCreate == '1':
        nopolbaliksewa = (input('''Masukkan Nomor Plat: '''))
        ceknopolbalik = (list(filter(lambda data: data['Nopol'] == nopolbaliksewa , daftarMobil)))
        if len(ceknopolbalik) > 0:
            print('''
                ===========
                Nopol salah
                ===========''')
            Create()
        merkbaliksewa = (input('''Masukkan Merk Mobil: '''))
        tipebaliksewa = (input('''Masukkan Tipe Mobil: '''))        
        hargabaliksewa = int(input('''Masukkan Harga Sewa (angka): ''')) 
        kategoribaliksewa = (input('''Masukkan Kategori Mobil: '''))
        warnabaliksewa = (input('''Masukkan Warna Mobil: '''))
        print(f''' 
Nopol = {nopolbaliksewa},
Merk = {merkbaliksewa},
Tipe = {tipebaliksewa},
Harga = {hargabaliksewa}
Kategori = {kategoribaliksewa}
Warna = {warnabaliksewa}''')
        validasicreate = input('''
Kembalikan mobil ini?
1. Ya
2. Tidak

Masukkan angka yang ingin dijalankan: ''')
        if validasicreate == '1':
            daftarMobil.append({
'Nopol': nopolbaliksewa,
'Merk': merkbaliksewa,
'Tipe': tipebaliksewa,
'Harga': hargabaliksewa,
'Kategori': kategoribaliksewa,
'Warna': warnabaliksewa})
            tampilkanmobil(daftarMobil)
        elif validasicreate == '2':
            Create()
        else:
            print("Maaf, input anda salah")
            Create()

    elif InputCreate == '2':
        password = input('''
Password : ''')
        if password == "purwadhika":
            inputnopolbaru = (input('''Masukkan Nomor Plat: '''))
            nopolbaru = (list(filter(lambda data: data['Nopol'] == inputnopolbaru , daftarMobil)))
            if len(nopolbaru) > 0:
                print('''
                =====================
                Nopol sudah terdaftar
                =====================''')
                Create()
            inputMerk = (input('''Masukkan Merk Mobil: '''))
            inputTipe = (input('''Masukkan Tipe Mobil: '''))
            inputHarga = int(input('''Masukkan Harga Sewa (angka): '''))
            inputKategori = (input('''Masukkan Kategori Mobil: '''))
            inputWarna = (input('''Masukkan Warna Mobil: '''))
            print(f''' 
Nopol = {inputnopolbaru},
Merk = {inputMerk},
Tipe = {inputTipe},
Harga = {inputHarga}
Kategori = {inputKategori}
Warna = {inputWarna}''')
            validasi = input('''
Tambahkan data ini?
1. Ya
2. Tidak

Masukkan angka yang ingin dijalankan: ''')
            if validasi == '1':
                daftarMobil.append({
'Nopol': inputnopolbaru,
'Merk': inputMerk,
'Tipe': inputTipe,
'Harga': inputHarga,
'Kategori': inputKategori,
'Warna': inputWarna})
                tampilkanmobil(daftarMobil)
            elif validasi == '2':
                Create()
            else:
                print("Maaf, input anda salah")
                Create()
        else:
            print('''
            ===================
            Password Anda Salah
            ===================''')
            Create()
    elif InputCreate == '3':
        Start()
    else:
        print('''
==================================================
Maaf, data salah. Mohon masukkan data dengan benar
==================================================''')
        Create()
    Create()

def Update():
    Inputupdate = input('''
Menu Ubah Data

1. Ubah Data
2. Kembali ke Menu Awal

Silahkan pilih angka menu yang ingin dijalankan: ''')
    if Inputupdate == '1':
        password = input('''
Password : ''')
        if password == "purwadhika":
            tampilkanmobil(daftarMobil)
            ubahdata = input('''
Silahkan masukkan Nopol Mobil yang ingin diubah: ''')
            validasiupdate = (list(filter(lambda data: data['Nopol'] == ubahdata , daftarMobil)))
            if len(validasiupdate) == 0:
                print('''
                    ===============
                    Nopol tidak ada
                    ===============''')
                Update()
            elif len(validasiupdate) > 0:
                tampilkanmobil(validasiupdate)
                pilihanupdate = input('''
Ingin mengubah data mobil ini?
1. Ya
2. Tidak

Masukkan angka pilihan anda: ''')
            
                if pilihanupdate == '1':
                    pemilihan = input('''
1. Ganti Nopol (TNKB)
2. Ganti Harga Sewa
3. Ganti Warna Mobil

Silahkan pilih angka yang ingin dijalankan: ''')
                    if pemilihan == '1':
                        updateNopol = input('''
Silahkan masukkan Nopol Baru: ''')
                        print('Nopol\t| Merk Mobil \t| Tipe     \t| Harga/hari\t| Warna')
                        for i in range(len(validasiupdate)):
                            print('{}\t| {}  \t| {}\t| {}\t| {}'.format(updateNopol, validasiupdate[i]['Merk'],validasiupdate[i]['Tipe'],validasiupdate[i]['Harga'], validasiupdate[i]['Warna']))
                        validasiNopol = input('''
Update data mobil ini?
1. Ya
2. Tidak

Masukkan angka pilihan anda: ''')
                        if validasiNopol == '1':
                            validasiupdate[0]['Nopol'] = updateNopol
                            tampilkanmobil(daftarMobil)
                            Update()
                        elif validasiNopol == '2':
                            Update()
                        else:
                            print('''
    =================================
    Mohon masukkan angka dengan benar
    =================================''')
                            Update()
                    elif pemilihan == '2':
                        while True:
                            updateHarga = (input('''
Silahkan masukkan Harga Baru (angka): '''))
                            x = updateHarga.isnumeric()
                            if x == True:
                                x = int(updateHarga)
                                break
                            else:
                                print('''
    =========================================
    Mohon masukkan harga (angka) dengan benar
    =========================================''')
                        print('Nopol\t| Merk Mobil \t| Tipe     \t| Harga/hari\t| Warna')
                        for i in range(len(validasiupdate)):
                            print('{}\t| {}  \t| {}\t| {}\t| {}'.format(validasiupdate[i]['Nopol'], validasiupdate[i]['Merk'],validasiupdate[i]['Tipe'],updateHarga, validasiupdate[i]['Warna']))
                        validasiHarga = input('''
Update data mobil ini?
1. Ya
2. Tidak

Masukkan angka pilihan anda: ''')
                        if validasiHarga == '1':
                            validasiupdate[0]['Harga'] = updateHarga
                            tampilkanmobil(daftarMobil)
                            Update()
                        elif validasiHarga == '2':
                            Update()
                        else:
                            print('''
    =================================
    Mohon masukkan angka dengan benar
    =================================''')
                            Update()
                    elif pemilihan == '3':
                        updateWarna = input('''
Silahkan masukkan Warna Baru: ''')
                        print('Nopol\t| Merk Mobil \t| Tipe     \t| Harga/hari\t| Warna')
                        for i in range(len(validasiupdate)):
                            print('{}\t| {}  \t| {}\t| {}\t| {}'.format(validasiupdate[i]['Nopol'], validasiupdate[i]['Merk'],validasiupdate[i]['Tipe'],validasiupdate[i]['Harga'], updateWarna))
                        validasiWarna = input('''
Update data mobil ini?
1. Ya
2. Tidak

Masukkan angka pilihan anda: ''')
                        if validasiWarna == '1':
                            validasiupdate[0]['Warna'] = updateWarna
                            tampilkanmobil(daftarMobil)
                            Update()
                        elif validasiWarna == '2':
                            Update()
                        else:
                            print('''
    =================================
    Mohon masukkan angka dengan benar
    =================================''')
                            Update()
                    else:
                        Update()
                elif pilihanupdate == '2':
                    Update()
                else:
                    print('''
    =================================
    Mohon masukkan angka dengan benar
    =================================''')
                    Update()
        else:
            print('''
    ==============
    Password Salah
    ==============''')
            Update()
    elif Inputupdate == '2':
        Start()
    else:
        print('''
    =================================
    Mohon masukkan angka dengan benar
    =================================''')
    Update()

def Delete():
    Inputdelete = input('''
1. Sewa Mobil
2. Hapus Mobil dari Daftar (Admin Only)
3. Kembali ke Menu Utama

Masukkan angka menu yang ingin dijalankan: ''')
    if Inputdelete == '1':
        print('Daftar Mobil')
        tampilkanmobil(daftarMobil)
        while True:
            sewamobil = input('''
Masukkan Nopol mobil yang ingin di sewa: ''')
            Durasi = int(input('''
Masukkan Waktu sewa mobil yang diinginkan (hari): '''))
            for i in range(len(daftarMobil)):
                x=0
                if sewamobil in daftarMobil[i]['Nopol']:
                    Jembatan.append(daftarMobil[i])
                    Jembatan[x]['Waktu'] = Durasi
                    x += 1
                    tampilkansewa(Jembatan)
                    validasiitemsewa = input('''
Sewa mobil ini?
1. Ya
2. Tidak

Masukkan angka menu pilihan anda: ''')
                    if validasiitemsewa == '1':
                        Keranjang.append(Jembatan[0])
                        Jembatan.clear()
                        print('Daftar Mobil yang dipesan')
                        tampilkansewa(Keranjang)
                        
            ceksewa = input('''
Ingin sewa mobil lainnya?
1. Ya
2. Tidak

Masukkan angka menu pilihan anda: ''')
            if ceksewa == '1':
                continue
            elif ceksewa == '2':
                pembayaran()
            else:
                print('''
=================================
Mohon masukkan angka dengan benar
=================================''')
                Delete()

    elif Inputdelete == '2':
        password = input('''
Password : ''')
        if password == "purwadhika":
            tampilkanmobil(daftarMobil)
            hapusmobil = (input('''
Masukkan Nopol Mobil yang ingin dihapus: '''))
            datadihapus = (list(filter(lambda data: data['Nopol'] == hapusmobil, daftarMobil)))
            if len(datadihapus):
                tampilkanmobil(datadihapus)
                while True:
                    validasidelete = input('''
Hapus data mobil ini?
1. Ya
2. Tidak

Masukkan angka menu pilihan anda: ''')
                    if validasidelete == '1':
                        for i in range(len(daftarMobil)):
                            if daftarMobil[i]['Nopol'] == hapusmobil:
                                del daftarMobil[i]
                                break
                        tampilkanmobil(daftarMobil)
                        Delete()
                    elif validasidelete =='2':
                        Delete()
                    else:
                        print('''
=================================
Mohon masukkan angka dengan benar
=================================''')
                        Delete()
            else:
                print('''
                    ====================
                    Maaf, Data Tidak Ada
                    ====================''')
                Delete()
        else:
            print('''
            ===================
            Password Anda Salah
            ===================''')
            Delete()
    elif Inputdelete == '3':
        Start()
    else:
        print('''
=================================
Mohon masukkan angka dengan benar
=================================''')
        Delete()

def Start():
    print('''
Semua Password = purwadhika''')
    while True :
        pilihanMenu = input('''
Selamat Datang di Bali Mitra Kencana Car Rental

List Menu :
1. Daftar Mobil
2. Pengembalian Mobil
3. Update Info Mobil (Admin Only)
4. Sewa Mobil
5. Exit Program

Masukkan angka Menu yang ingin dijalankan : ''')

        if(pilihanMenu == '1') :
            Read()
        elif(pilihanMenu == '2') :
            Create()
        elif(pilihanMenu == '3') :
            Update()
        elif(pilihanMenu == '4') :
            Delete()
        elif(pilihanMenu == '5') :
            exit()    
        else:
            print('''
==================================================
Maaf, data salah. Mohon masukkan data dengan benar
==================================================''')
Start()