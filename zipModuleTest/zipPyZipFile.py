"""
Utilizando uma funcao chamada PyZipFile para adicionar arquivos do python a um arquivo zip
utilizando a funcao writepy()
"""


import sys
import zipfile

__author__ = 'daniloqb'


if __name__ == '__main__':

    filename = 'zipfile_pyzipfile.zip'
    # O arquivo que sera aberto sera um objeto do tipo PyZipFile
    zf = zipfile.PyZipFile(filename,mode='w')
    try:
        zf.debug = 3
        print 'adding python files'
        zf.writepy('.')
    finally:
        zf.close()

    for name in zf.namelist():
        print name

    print

    sys.path.insert(0,filename)
    import zipPyZipFile

    print 'imported form: ', zipPyZipFile.__file__

