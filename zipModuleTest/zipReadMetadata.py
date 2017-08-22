"""
Script que utiliza o modulo zipfile para ler o conteudo de um arquivo zip
funcoes importantes sao
abertura de um arquivo zip: zip = zipfile.ZipFile(filename,mode)
lista de arquivos: zip.namelist()
"""


import zipfile

__author__ = 'daniloqb'
__version__='1.0'


#realiza a abertura de um arquivo zip
zf = zipfile.ZipFile('/home/user/bkp_code/20150908/104307.zip','r')

#utiliza o comando namelist() para retornar a lista de arquivos contidos no arquivo zip
print zf.namelist()