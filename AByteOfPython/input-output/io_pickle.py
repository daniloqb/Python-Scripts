import pickle

__author__ = 'daniloqb'


shoplistfile = 'shoplist.data'

shoplist = ['mango', 'apple', 'carrot']

f = open(shoplistfile,'wb')

pickle.dump(shoplist,f)


del shoplist

f.close()


f = open(shoplistfile,'rb')

storedList = pickle.load(f)

print storedList
