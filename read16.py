from sys import argv

script, filename = argv
# 'r' is not necessary as the default for open(filename) is read, 'w' is write and 'a' is append.
ex16 = open(filename, 'r')

print ex16.read()

