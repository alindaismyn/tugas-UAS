def penggajian() :
    from texttable import Texttable
    table1 = Texttable ()
    no1 = 0
    nama1 = []
    jabatan = []
    gaji = []
    jawab1 = "y"

    while (jawab1 == 'y'):
        nama1.append(input("Masukan Nama: "))
        jab = input("Jabatan : ")
        jabatan.append(jab)
        if  (jab == 'Programer') :
            gaji.append('30000000')
            no1+=1
        
            jawab1 = input("\nTambah Lagi? ")
        elif (jab == 'Leader') :
            gaji.append('3000000')
            print (" ")
            no1+=1
        
            jawab1 = input("\nTambah Lagi? ")
        elif (jab == 'Manager') :
            gaji.append('1500000')
            print (" ")
            no1+=1
            jawab1 = input("\n tambah lagi : ")
            
        else:
            break
            
        
    for i1 in range (no1) :
        table1.add_rows([['No','Nama','Jabatan','Gaji'],
                         [i1+1, nama1[i1],jabatan[i1],gaji[i1]]])                  
    print(table1.draw())

