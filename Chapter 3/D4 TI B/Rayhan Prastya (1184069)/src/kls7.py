def kali(npm):
    
    i = 0
    while i<1:
        if len(npm) < 7:
            print("npm kurang dari 7 digit, silahkan masukkan npm anda kembali")
        elif len(npm) > 7:
            print("npm yang diinputkan lebih dari 7, silahkan masukkan npm anda kembali")
        else:
            i=1
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    y=0

    for x in a,b,c,d,e,f,g:
        y*=int(x)
    print(y)
