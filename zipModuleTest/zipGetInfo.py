"""
Para obter informacoes tambem e possivel utilizar a funcao getinfo passando como parametro os nomes dos arquivos con
tidos no arquivo zip
"""


import zipfile

__author__ = 'user'

#abre o arquivo zip
zf = zipfile.ZipFile('/home/user/bkp_code/20150908/104307.zip')

#Para cada arquivo retornado pela funcao namelist execute
for filename in zf.namelist():
    try:
        info = zf.getinfo(filename) #recupera as informacoes
    except KeyError:
        print 'Error: Did not find %s in zipfile' % filename # se o arquivo nao existir, um erro sera retornado
    else:
        print '%s is %d bytes' % (info.filename, info.file_size) #retorna algumas informacoes
