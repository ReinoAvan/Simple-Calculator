def kalkulator():
  while True:
    try:
      a = int(input("Masukkan angka pertama: "))
      if a > 1000000:
        print("Input maksimal adalah 1 juta.")
        continue
      b = int(input("Masukkan angka kedua: "))
      if b > 1000000:
        print("Input maksimal adalah 1 juta.")
        continue
      break
    except ValueError:
      print("Input harus berupa angka.")

  operator = input("Masukkan operator (+,-,*,/): ")
  if operator == '+':
    hasil = a + b
  elif operator == '-':
    hasil = a - b
  elif operator == '*':
    hasil = a * b
  elif operator == '/':
    hasil = a / b
  else:
    print("Operator tidak valid.")
    return
  
  print(f"Hasil: {a} {operator} {b} = {hasil}")

kalkulator()
