#ex1 
import os 
path = 'g:\\xpath\\' 
print('directories: ') 
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]) 
print("files:") 
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ]) 
print('directories and files:') 
print([ name for name in os.listdir(path)])

#ex2
import os 
print('exist -', os.access('path.docx', os.F_OK)) 
print('readable -', os.access('path.docx', os.R_OK)) 
print('writable -', os.access('path.docx', os.W_OK)) 
print('executable -', os.access('path.docx', os.X_OK))

#ex3
import os
print('exist or not:')
path = r'g:\\path\\a.txt'
print(os.path.exists(path))
path = r'g:\\path\\p.txt'
print(os.path.exists(path))
print('\nfile name: ')
print(os.path.basename(path))
print('\ndir name: ')
print(os.path.dirname(path))

#ex4
def cnt(n):
        with open(n) as f:
                for x, l in enumerate(f):
                        pass
        return x + 1
print('number of lines: ',cnt('file1.txt'))

#ex5
fruits = ['apple', 'banana', 'cherry', 'blackberry', 'orange', 'grape', 'pomegranade']
with open('file2.txt', 'w') as myfile:
        for c in fruits:
                myfile.write('%s\n' % c)

x = open('file2.txt')
print(x.read())

#ex6
import string
import os
if not os.path.exists('ABC'):
   os.makedirs('ABC')
for x in string.ascii_uppercase:
   with open(x + '.txt', 'w') as f:
       f.writelines(x)

#ex7
from shutil import copyfile
copyfile('1.py', '2.py')

#ex8
import os
os.remove('file3.txt')
