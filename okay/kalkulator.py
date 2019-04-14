def kalkulator () :
    

    def tambah () :
        print ('\n1.penjumlahan')
        a = int(input('masukan nilai x = '))
        b = int(input('masukan nilai y = '))
        c = a+b
        print ('x + y =',c)
        print ('')
        tanya ()

    def kurang () :
        print ('\n2.pengurangan')
        a = int(input('masukan nilai x = '))
        b = int(input('masukan nilai y = '))
        c = a-b
        print ('x - y =',c)
        print ('')
        tanya ()

    def kali () :
        print ('\n3.perkalian')
        a = int(input('masukan nilai x = '))
        b = int(input('masukan nilai y = '))
        c = a*b
        print ('x . y =',c)
        print ('')
        tanya ()

    def bagi () :
        print ('\n4.pembagian')
        a = int(input('masukan nilai x = '))
        b = int(input('masukan nilai y = '))
        c = a/b
        print ('x/y =',c)
        print ('')
        tanya ()

    def tanya () :
        choose = input (' apakah anda ingin mengulang (y/t)? ')
        if choose == 'y' :
            kalkulator ()
        elif choose == 't' :
            print ('thanks for use this program ^_^')
        else :
            print ('sorry, the input entered is incorrect')

        tanya ()

    print ('program kalkulator sederhana')
    print ('1. penjumlahan')
    print ('2. pengurangan')
    print ('3. perkalian')
    print ('4. pembagian')
    print ('')

    pil = input ('masukan pilihan : ')
    if pil == '1':
        tambah ()
    elif pil == '2':
        kurang ()
    elif pil == '3':
        kali ()
    elif pil == '4':
        bagi ()
    else :
        print ('sorry, the input entered is incorrect')
        print ('lets try again')
        tanya ()


