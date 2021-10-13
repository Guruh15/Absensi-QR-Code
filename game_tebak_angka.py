import random

angka_random = random.randint(1, 100)

nyawa = 5
for percobaan in range(nyawa):
  jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukkan tebakkan anda: '))

  if jawaban == angka_random:
    print('Selamat, tebakan anda benar!')
    break
  else:
    print(
      'Tebakan anda terlalu',
      'kecil' if jawaban < angka_random else 'besar'
    )
else:
  print(f'\nNyawa anda telah habis, dan anda telah kalah')