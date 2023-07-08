import hashlib

file = input('Введите имя файла №1: ')
file1 = input('Введите имя файла №2: ')

file_hash = hashlib.sha256()
with open(file, 'rb') as f:
    fb = f.read()
    while len(fb) > 0: 
        file_hash.update(fb)
        fb = f.read()

fileHash = file_hash.hexdigest()

file_hash1 = hashlib.sha256()
with open(file1, 'rb') as f:
    fb = f.read()
    while len(fb) > 0: 
        file_hash1.update(fb)
        fb = f.read()

fileHash1 = file_hash1.hexdigest()


if fileHash == fileHash1:
    print('Файлы одинаковые')
else:
    print('Файлы разные')