"""
Este script utiliza o modulo zipfile para obter diversas informacoes dos arquivos contidos em um arquivo comprimido
utilizando a funcao infolist() e possivel obter diversas informacoes
Esta funcao retorna uma lista de objetos do tipo ZipInfo no qual e possivel obter diversas informacoes
info.filename
info.comment
info.date_time
info.create_system
info.create_version
info.compress_size
info.file_size
"""

import zipfile
import datetime

__author__ = 'daniloqb'
__version__ = '1'


def print_info(archive_name):
    zf = zipfile.ZipFile(archive_name)

    for info in zf.infolist():
        print info.filename
        print '\tComment\t', info.comment
        print '\tModified\t', datetime.datetime(*info.date_time)
        print '\tSystem\t', info.create_system, '(0 - Windows, 3 - Unix)'
        print '\tZip version\t', info.create_version
        print '\tCompressed\t', info.compress_size, ' bytes'
        print '\tUncompressed\t', info.file_size, ' bytes'
        print


if __name__ == '__main__':
    print_info('/home/user/bkp_code/20150908/104307.zip')
