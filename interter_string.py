def inverter_string(string_original):
  return string_original[::-1]
  
string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)