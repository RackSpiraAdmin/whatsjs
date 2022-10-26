listnilai = []
i = 'y'
while i == 'y' :
    print ("==================================================================")
    print ("                     Program Entry Matakuliah")
    print ("==================================================================")
    matkul = input("Nama Matakuliah : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS : "))
    uas = float(input("Nilai UAS : "))
    rumus = (float(tugas * 30/100) + (uts * 30/100) + (uas * 40/100))
    tot = str (round(rumus))
    print ("Nilai Angka : " + tot)
    a=80
    b=60
    c=40
    d=20
    if rumus >= 80 :
        NilHuruf = "A"
        print ("Nilai Huruf : " + NilHuruf)
    elif rumus >= 60 :
        NilHuruf = "B"
        print ("Nilai Huruf : " + NilHuruf)
    elif rumus >= 40 :
        NilHuruf = "C"
        print ("Nilai Huruf : " + NilHuruf)
    elif rumus >= 20 :
        NilHuruf = "D"
        print ("Nilai Huruf : " + NilHuruf)
    else : 
        NilHuruf = "E"
        print ("Nilai Huruf : " + NilHuruf)
    i = input("Apakah Entry Lagi ? [y] / [t] : ")
    dictNilai = {
        'matkul' : matkul,
        'tugas' : tugas,
        'uts' : uts,
        'uas' : uas,
        'tot' : tot,
        'NilHuruf' : NilHuruf
    }
    listnilai.append(dictNilai)

print ("==================================================================")
print('{:^65}'. format('Data Nilai'))
print ("==================================================================")
print('{0:<14} {1:<10} {2:<8} {3:<8} {4:<10} {5:<10}' .format('NamaMataKuliah', 'NilaiTugas', 'NilaiUts', 'NilaiUas', 'NilaiAngka', 'NilaiHuruf'))
print ("==================================================================")

for dictNilai in listnilai :
    print('{0:<14} {1:>10} {2:>8} {3:>8} {4:>10} {5:>10}'.format(dictNilai['matkul'], dictNilai['tugas'], dictNilai['uts'], dictNilai['uas'], 
                                                                dictNilai['tot'], dictNilai['NilHuruf']))
print ("==================================================================")
