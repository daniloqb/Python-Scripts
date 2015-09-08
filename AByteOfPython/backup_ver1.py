#!/usr/bin/python2.7

'''
Primeira versao de teste para realizacao de backup de arquivos usando python
'''

import os
import time

#Source representa uma lista de diretorios que serao salvos
source = ['/home/user/test_code','/home/user/test2_code']
#target_dir sera o diretorio que contera os arquivos de backup
target_dir = '/home/user/bkp_code'

#target sera o nome do arquivo de backup com seu caminho
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#se o diretorio de backup nao existir, ele sera criado
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#zip_command sera o comando que o SO executara
zip_command = "zip -r {0} {1}".format(target,' '.join(source))


#Informacoes
print "Zip command is"
print zip_command
print "Running"

#Executa o comando e testa se obteve sucesso
if os.system(zip_command) == 0:
    print "Successful backup to", target
else:
    print "Backup FAILED."
    
