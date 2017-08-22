"""
Criar um arquivo zip comprimido utilizando zipfile
Para utilizar a compressao e necessario adicionar o modulo zlib
"""


from zipInfoList import print_info
import zipfile

__author__ = 'user'


try:
    import zlib    #tentando importar zlib
    compression = zipfile.ZIP_DEFLATED   # se a importacao ocorrer sera utilizado a compressao ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED     # se nao for possivel importar zlib a compressao sera ZIP_STORED que e a
                                         # compressao padrao


#dicionario com as informacoes de compressao para impressao
modes = {zipfile.ZIP_DEFLATED : 'deflated',
         zipfile.ZIP_STORED : 'stored'}

print 'creating archive'
#criacao do arquivo zip
zf = zipfile.ZipFile('zipfile_write_compressed.zip',mode = 'w')

try:
    print 'adding README.txt with compression mode ',modes[compression]
    zf.write('README.txt',compress_type=compression) #adicionando o arquivo ao zip e passando o modo de compressao
finally:
    print 'closing'
    zf.close()

print
print_info('zipfile_write_compressed.zip')

