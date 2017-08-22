"""
Neste script foi utilizado um objeto do tipo zipinfo para passar mais informacoes para a criacao de um arquivo com uma
mensagem dentro para o zip
zipfile.ZipInfo() neccessita de 02 parametros para a criacao do objeto. nome do arquivo e a data de criacao
"""

import zipfile
import time
from zipInfoList import print_info

__author__ = 'daniloqb'

# mensagem a ser salva no zip
#msg = 'This message did not exist in a file before being added to the zip file'
msg = range(0,10,2)

# abertura do arquivo zip
zf = zipfile.ZipFile('zipfile_writestr_zipinfo.zip','w')

try:
    # criacao do objeto zipInfo com as informacoes de nome e de tempo local
    info = zipfile.ZipInfo('from_string-even.txt',date_time=time.localtime(time.time()))
    # passagem de informacoes adicionais para o zipinfo
    info.compress_type = zipfile.ZIP_DEFLATED
    info.comment = 'Remarks go here'
    info.create_system = 0
    # ao inves de utilizar um arc_name e passado o zipinfo como parametro e depois os dados
    zf.writestr(info,str(msg))
finally:
    zf.close()

print_info('zipfile_writestr_zipinfo.zip')

