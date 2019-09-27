import io, os


curDir = os.getcwd() + '/WaitToTranslate/'

files = os.listdir(curDir)

file = curDir + files[0]

filePath = file.rsplit('.', 1)[0] + '_t.txt'

f = open(filePath, 'wt')

f.write("12313\n")
f.write("aaaaa\n")
f.close()