"""
Teste interessante com a funcao writestr(), onde um texto que nao existe dentro de um arquivo e passado diretamente
para um arquivo zip. Um arquivo e criado dinamicamente com o conteudo passado
"""


from zipInfoList import print_info
import zipfile

__author__ = 'user'

# nome do arquivo zip
filename = 'zipfile_write_str.zip'

# dados que serao salvos
msg = 'This data did not exist in a file before being added to the archive'

#abrindo o arquivo zip, passando o modo como escrita e a compressao como deflate
#zf = zipfile.ZipFile(filename,mode='w',compression=zipfile.ZIP_DEFLATED)
#Fiz uma modificacao no codigo passando a compressao para a funcao writestr. No tutorial esta dizendo que nao era possi
#vel, contudo deu certo

zf = zipfile.ZipFile(filename,mode='w')
try:
    zf.writestr('from_string_txt',msg,compress_type=zipfile.ZIP_DEFLATED)
finally:
    zf.close()

print_info(filename)

zf = zipfile.ZipFile(filename,'r')

print zf.read('from_string_txt')