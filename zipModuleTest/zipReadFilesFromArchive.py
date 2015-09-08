"""
Le o conteudo dos arquivos dentro de um zip
utiliza a funcao read para cada nome de arquivo contido dentro do zip
"""


import zipfile

__author__ = 'user'

zf = zipfile.ZipFile('/home/user/bkp_code/20150908/104307.zip')

for filename in zf.namelist():
    try:
        data = zf.read(filename)
    except KeyError:
        print 'Error: Did not file %s in zip file' % filename
    else:
        print filename, ':'
        print repr(data)
    print


