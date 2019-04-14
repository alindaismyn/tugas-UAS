
def bayar () :

        print("\nWELCOME, LETS CHOOSE\t")
        print("1. PROGRAM PEMBAYARAN UTS")
        print("2. PROGRAM PEMBAYARAN UAS")
        pilihan = input("\nMASUKAN PILIHAN BAYARAN : ")
        if   pilihan == '1' :
                uts() 
        elif pilihan == '2' :
                uas()
        else :
                akhir()
           
def uts():
        from texttable import Texttable
        table = Texttable()
        jawab = "y"

        no = 0
        nama =[]
        nim = []
        kelas = []
        jum_matkul_uts_bayar = []
        bulan_bayar = []
        while(jawab == "y") :
            nama.append(input(" Nama  : "))
            nim.append(input(" NIM    : "))
            kelas.append(input(" Kelas : "))
            jum_matkul_uts_bayar.append(input(" MATA KULIAH YANG DI BAYAR BUAT UTS : "))
            bulan_bayar.append(input("JUMLAH BULAN BIAYA YANG DIBAYAR : "))
            kas =(input("BAYAR KAS y/t  : "))
            if kas == 'y' :
                    bayar_kas = 20000
            else :
                    bayar_kas = 0
            seminar =(input("BAYAR SEMINAR y/t : "))
            if seminar == 'y' :
                    bayar_seminar = 100000
            else :
                    bayar_seminar = 0
            jawab = input("Ingin Bayar Lagi (y/t) ? ")
            no += 1
        
        for i in range (no):
            bayar_uts = int(jum_matkul_uts_bayar[i])*50000
            bayar_spp = int(bulan_bayar[i])*500000
            admin = int("5000")
            akhir = bayar_uts + bayar_spp + bayar_seminar+ bayar_kas + admin
            table.set_cols_dtype(['i','t','t','t','t','t','t','t','t','t'])
            table.set_cols_align(["i", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
            table.set_cols_width([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])
            
            table.add_rows([['No','NAMA',' NIM ','KELAS','BIAYA UTS','BIAYA SPP','SEMINAR','KAS','ADMIN','TOTAL'],
                        [i+1, nama[i],nim[i],kelas[i],bayar_uts,bayar_spp,bayar_seminar,bayar_kas,admin,akhir]])
        print (table.draw())

        alinda()

def uas():
        from texttable import Texttable
        table = Texttable()
        jawab = "y"
        no = 0
        nama =[]
        nim = []
        kelas = []
        jum_matkul_uas_bayar = []
        bulan_bayar = []
        while(jawab == "y") :
            nama.append(input(" NAMA : "))
            nim.append(input(" NIM   : "))
            kelas.append(input("KELAS : "))
            jum_matkul_uas_bayar.append(input("MATA KULIAH YANG DI BAYAR UNTUK UAS : "))
            bulan_bayar.append(input("JUMLAH BULAN BIAYA YANG DIBAYAR : "))
            kas =(input("BAYAR KAS y/t  : "))
            if kas == 'y' :
                    bayar_kas = 20000
            else :
                    bayar_kas = 0
            seminar =(input("BAYAR SEMINAR y/t  : "))
            if seminar == 'y' :
                    bayar_seminar = 100000
            else :
                    bayar_seminar = 0
            jawab = input("Ingin Bayar Lagi (y/t) ? ")
            no += 1
        
        for i in range (no):
            bayar_uas = int(jum_matkul_uas_bayar[i])*50000
            bayar_spp = int(bulan_bayar[i])*500000
            admin = int("5000")
            akhir = bayar_uas + bayar_spp + bayar_seminar + bayar_kas + admin
            table.set_cols_dtype(['i','t','t','t','t','t','t','t','t','t'])
            table.set_cols_align(["i", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
            table.set_cols_width([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])
            
            table.add_rows([['No','NAMA','NIM','KELAS','BIAYA UAS','BIAYA SPP','SEMINAR','KAS','ADMIN','TOTAL'],
                        [i+1, nama[i],nim[i],kelas[i],bayar_uas,bayar_spp,bayar_seminar,bayar_kas,admin,akhir]])
        print (table.draw())
        alinda()
        
        
def alinda():
    tanya = input("\nKEMBALI LAGI KE HALAMAN AWAL (y/t)?")
    if tanya == "y":
        print("WELCOME, LETS CHOOSE")
        print("1. PROGRAM PEMBAYARAN UTS")
        print("2. PROGRAM PEMBAYARAN UAS")
        bayar ()
    else :
            print("\n\tSORRY!!!")
            exit


