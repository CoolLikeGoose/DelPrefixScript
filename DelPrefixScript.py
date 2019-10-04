from os import rename, listdir

badprefix = "x" #Какой префикс удалять
fnames = listdir('.') #путь до папки

for fname in fnames:
    if fname.startswith(badprefix):
        rename(fname, fname.replace(badprefix, ''))