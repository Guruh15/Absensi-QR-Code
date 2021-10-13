from random import randint

pilihan = ["Gunting", "Batu", "Kertas"]

komputer = pilihan[randint(0,2)]
player = False

while player == False:
    #Set pemain ke True
    print("Masukkan pilihan anda")
    player = input("Gunting, Batu, Kertas : ")
    if player == komputer:
        print("Imbang")
    elif player == "Batu":
        if komputer == "Kertas":
            print("Anda Kalah", komputer, "mengalahkan", player)
        else:
            print("Anda Menang!", player, "mengalahkan", komputer)
    elif player == "Kertas":
        if komputer == "Gunting":
            print("Anda Kalah", komputer, "mengalahkan", player)
        else:
            print("Anda Menang", player, "mengalahkan", komputer)
    elif player == "Gunting":
        if komputer == "Batu":
            print("Anda Kalah", komputer, "mengalahkan", player)
        else:
            print("Anda Menang", player, "mengalahkan", komputer)
    else:
        print("Pilihan yang kamu masukan salah...")

    player = False
komputer = pilihan[randint(0,2)]