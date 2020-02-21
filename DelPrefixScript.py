from os import rename, listdir

badprefix = "x" #which prefix delete
fnames = listdir('.') #path

for fname in fnames:
    if fname.startswith(badprefix):
        rename(fname, fname.replace(badprefix, ''))
