# wiki dump download link: https://dumps.wikimedia.org/bnwiki/latest/bnwiki-latest-pages-articles.xml.bz2

import bz2

filepath = "bnwiki-latest-pages-articles.xml.bz2"
zipfile = bz2.BZ2File(filepath) # open the file
data = zipfile.read() # get the decompressed data
newfilepath = filepath[:-4] # assuming the filepath ends with .bz2
print(newfilepath)
open(newfilepath, 'wb').write(data) # write a uncompressed file
