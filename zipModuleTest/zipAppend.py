"""
Testando alem da criacao de um arquivo zip a possibilidade de adicionar novos arquivos ao final do arquivo
Para isso basta abrir um arquivo ja existente com o modo 'a'
"""


import zipfile
from zipInfoList import print_info


__author__ = 'danilo'


print 'creating archive'


# Abrindo o arquivo para leitura. Contudo se ao inves de inserir o modo 'w' inserir o modo 'a' tambem funciona
zf = zipfile.ZipFile('zip_archive.zip','w')

# Insere o primeiro arquivo e fecha
try:
    zf.write('README.txt')
finally:
    zf.close()

print_info('zip_archive.zip')

print 'appending to the archive'

# Abre no modo de adicionar no final
zf = zipfile.ZipFile('zip_archive.zip','a')


# Insere o mesmo arquivo, agora usando o parametro arcname para inserir com outro nome
try:
    zf.write('README.txt','README2.txt')
finally:
    zf.close()

print
print_info('zip_archive.zip')
