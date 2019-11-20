'''
os module has the features to use related to operating system. 
The features related to paths, folders and os commands are shown in the example below. 
'''
import os
print(os.name)
path = os.path.join('db', 'sqlite.py')
print(path)
print(os.getcwd())
print(os.chdir('B:/soft'))
# print(os.makedirs('B:/soft/tt'))
print(os.system('cls'))
sys1 = os.system('ipconfig ifcount')
print(sys1)