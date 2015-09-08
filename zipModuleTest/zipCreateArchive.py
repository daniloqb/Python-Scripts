"""
Criando um arquivo zip sem compressao utilizando a funcao write.
Ao abrir o arquivo e necessario passar o modo 'w'
se ao gravar o arquivo no zip utilizar o parametro arcname='outro_nome' o arquivo sera salvo com um novo nome
"""


from zipInfoList import print_info
import zipfile

__author__ = 'daniloqb'

print 'Creating archive'

# abrindo o arquivo no modo w
zf = zipfile.ZipFile('zipfile_write.zip', 'w')

try:
    print 'Adding README.txt'
    zf.write('README.txt')   # adicionado o arquivo README.txt

finally:   # finaliza fechando o arquivo
    print 'Closing'
    zf.close()

print
print_info('zipfile_write.zip') # utiliza a funcao anterior para obter informacoes dos arquivos do zip
