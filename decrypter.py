import os
import pyaes

#Abre o arquivo criptografado, lê, armazena os dados, fecha e exclui o arquivo.
file_name = "arquivo.txt.criptografado"
file = open(file_name, 'rb')
file_data = file.read()
file.close()


#Definindo a chave para descriptografia 
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

#Desciptografando o arquivo.
decrypt_data = aes.decrypt(file_data)

#Removo o arquivo, crio um novo com os dados descriptografados.
os.remove(file_name)
new_file = "arquivo.txt"
with open(new_file, 'wb') as file_decrypt:
    file_decrypt.write(decrypt_data)
