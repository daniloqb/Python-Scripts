"""
Script que faz uso do modulo zipfile para testar se um arquivo e um arquivo zip.
funcao principal zipfile.is_zipfile(filename)
"""

import zipfile

__author__ = 'daniloqb'

__version__ = '1'



#lista de nomes de possiveis arquivos que serao testados para saber se sao arquivos zip
listOfFiles = ['/home/user/test_code/backup_ver1.py','/home/user/test_code/sysArgv.py',\
                  '/home/user/bkp_code/20150908/104307.zip']

#Para cada nome de arquivo verificar e retornar True ou False se for um arquivo zip
for filename in listOfFiles:
    print '%40s    %s' % (filename, zipfile.is_zipfile(filename))



