"""
===================================================================================================
Kelompok            : 8
Anggota             : - 16520201 | Kirana Shely S
                      - 16520251 | Rofif Fairuz Hawary
                      - 16520261 | Khalisa Prabhasalma
                      - 16520281 | Vixell
Deskripsi Program   : Program ini untuk menggambarkan bagaimana sistem ticketing cinema

====================================================================================================

Variable Dictionary:
printSeat():
Seat = array 2 dimensi(matriks) yang mencakup koordinat seat cinema

changeVisualSB():
Seat = array 2 dimensi(matriks) yang mencakup koordinat seat cinema

getAudience():
j_org = int, jumlah orang dalam satu pesanan
slot_R = int, jumlah kursi kosong reguler
slot_SB = int, jumlah kursi kosong sweetbox
status_slot = boolean, sebagai penanda kursi masih muat untuk jumlah j_org atau tidak

typeChoice():
j_org = int, jumlah orang dalam satu pesanan
type = string, berisi jenis kursi pilihan sb atau r
slot_SB = int, jumlah kursi kosong sweetbox
slot_R = int, jumlah kursi kosong reguler

countSlotR():
slot_R = int, jumlah kursi kosong reguler

countSlotSB():
slot_SB = slot_SB = int, jumlah kursi kosong sweetbox

sweetBoxSeat():
j_org = j_org = int, jumlah orang dalam satu pesanan
temp = int, sebagai wadah nilai j_org, agar nilai j_org tidak berubah saat digunakan di fungsi lain
type = string, berisi jenis kursi pilihan sb atau r
rows = baris pilihan customer
column = kolom pilihan customer

regularSeat():
j_org = j_org = int, jumlah orang dalam satu pesanan
temp = int, sebagai wadah nilai j_org, agar nilai j_org tidak berubah saat digunakan di fungsi lain
type = string, berisi jenis kursi pilihan sb atau r
rows = baris pilihan customer
column = kolom pilihan customer
"""




# fungsi untuk traversal kondisi seluruh kursi di studio
def printSeat():
    for j in range(5):
        print(end="          ")
        for i in range(16):
            if i == 3 or i == 11:
                if j == 0:
                    print(" K ", end="    ")
                elif j == 1:
                    print(" o ", end="    ")
                elif j == 2:
                    print(" l ", end="    ")
                elif j == 3:
                    print(" o ", end="    ")
                elif j == 4:
                    print(" m ", end="    ")
            else:
                if j == 0:
                    print(" K ", end=" ")
                elif j == 1:
                    print(" o ", end=" ")
                elif j == 2:
                    print(" l ", end=" ")
                elif j == 3:
                    print(" o ", end=" ")
                elif j == 4:
                    print(" m ", end=" ")
        print()    
    print(end="         ")                
    for i in range(10):
        if i == 3 or i == 11:
            print(" ", i , end="    ")
        else:
            print(" ", i , end=" ")
    
    print("  10  11     12  13  14  15\n")

    for j in range(10):
        print("Baris ", j, end=" ")
        for i in range(16):
            if i == 3 or i == 11:       # ini untuk memberikan celah besar di line tertentu(sebagai jalan pengunjung)
                print(" ", seat[i][j], end="    ")
            else:
                print(" ", seat[i][j], end=" ")          
        print()
    print("           ============================== LAYAR ===============================")

# fungsi untuk mengubah display sweetbox menjadi character S
def changeVisualSB(seat):
    for j in range(1,3):
        for i in range(16):
            seat[i][j] = "S"

# fungsi untuk mengamil jumlah orang dalam 1 pesanan
def getAudience(j_org, slot_R, slot_SB, status_slot):
    status_slot = False
    print("slot SB adalah", slot_SB)
    j_org = int(input("Jumlah orang: "))
    while j_org < 1 or j_org > 8:
        print("Jumlah orang tidak kurang dari 1 dan tidak lebih dari 8")
        j_org = int(input("Jumlah orang: "))
    if j_org > slot_R and j_org > slot_SB:
        print("Kursi penuh untuk ", j_org, " orang")
        status_slot = False
    else:
        status_slot = True
    return j_org, status_slot

# fungsi untuk memilih pilian kursi customer
def typeChoice(j_org, type, slot_SB, slot_R):

    print("Pilih tipe kursimu: ")
    print("Sweet Box (sb)")
    print("Regular (r)")

    status_slot = False
    while status_slot == False:
        type = input("Pilih tipe: ")
        while type != "sb" and type != "r":
            print("Tipe kursi hanya tersedia sb dan r")
            type = input("Pilih tipe: ")
        if type == "sb":    # untuk pilihan sweetbox
            if slot_SB >= j_org:
                status_slot = True
            else:
                print("Jumlah kursi sweetbox tidak cukup untuk ", j_org, " orang")
        else:   # untuk pilihan reguler
            if slot_R >= j_org:
                status_slot = True
            else:
                print("Jumlah kursi reguler tidak cukup untuk ", j_org, " orang")
    return type, status_slot        

# fungsi untuk menghitung jumlah kursi reguler yang kosong
def countSlotR(slot_R):
    for j in range(0,10):
        for i in range(16):
            if seat[i][j] == "R":
                slot_R += 1
    print("slot R adalah ", slot_R)
    return slot_R

# fungsi untuk menghitung jumlah kursi sweetbox yang kosong    
def countSlotSB(slot_SB):
    for j in range(1,3):
        for i in range(16):
            if seat[i][j] == "S":
                slot_SB += 1
    print("slot SB adalah", slot_SB)
    return slot_SB

# fungsi untuk memilih kursi sweetbox
def sweetBoxSeat(j_org, type, rows, column):
    temp = j_org
    while temp > 0:
        rows = int(input("Baris kursi: "))
        column = int(input("Kolom kursi: "))
        while rows < 1 or rows > 2 or column < 0 or column > 15:
            print("baris sweetbox hanya tersedia dari 1-2, kolom sweetbox hanya 0-15")
            rows = int(input("Baris kursi: "))
            column = int(input("Kolom kursi: "))
        if seat[column][rows] == "S":   # jika kursi pilihan kosong
            if column % 2 == 0:    # jika sweetbox pilihan genap
                seat[column][rows] = "X"
                seat[column+1][rows] = "X"
                temp -= 2
            else:   # jika sweetbox pilihan ganjil
                seat[column][rows] = "X"
                seat[column-1][rows] = "X"
                temp -= 2
        else:
            print("Kursi sweetbox tsb sudah dibooking")

# fungsi untuk memilih kursi reguler satu per satu   
def regulerSeat(j_org, type, rows, column):
    temp = j_org
    while temp > 0:
        rows = int(input("Baris kursi: "))
        column = int(input("Kolom kursi: "))
        while rows < 0 or rows > 9 or column < 0 or column > 15 or rows == 1 or rows == 2:
            print("baris reguler hanya tersedia dari 3-9 dan 0, kolom sweetbox hanya 0-15")
            rows = int(input("Baris kursi: "))
            column = int(input("Kolom kursi: "))
        if seat[column][rows] == "R":
            seat[column][rows] = "X"
            temp -= 1
        else:
            print("Kursi reguler tsb sudah dibooking")
    print()

#----------------- MAIN --------------------
seat = [["R" for j in range(10)] for i in range(16)]    # membuat default seat
changeVisualSB(seat)    # merubah visual sweet box menjadi char "R"
printSeat()     # mentraversalkan kondisi seat awal
selesai = False         
while selesai == False: # looping hingga waiters mengatakan tidak melanjutkan ambil cust
   
    # semua variable yang bersifat akan digunakan terus menerus dan berubah2 nilainya
    # di declare terlebih dahulu ke nilai yang salah sehingga dapat terus digunakan ke dalam fungsi fungsi
    # yang telah ada, karena akan terjadi looping yang akan menggunakan fungsi secara terus menerus
    j_org = 0
    type = "empty"
    slot_R = 0
    slot_SB = 0
    status_slot = False
    rows = -1
    column = -1
    slot_R = countSlotR(slot_R)
    slot_SB = countSlotSB(slot_SB)
    j_org, status_slot = getAudience(j_org, slot_R, slot_SB, status_slot)
    type, status_slot = typeChoice(j_org,type, slot_SB, slot_R)

    if status_slot == True:
        if type == "sb":
            sweetBoxSeat(j_org,type, rows, column)
        else:   # type = r
            regulerSeat(j_org, type, rows, column)
        printSeat()

    pick = input("Ingin lanjut mengambil pesanan customer? y/t:")
    while pick != "t" and pick != "y":
        pick = input("Ulangi masukan: ")
    if pick == "t":
        selesai = True 
