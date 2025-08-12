# standard library
# os
import os
print(os.getcwd())

directory = 'WastedDirectory'
parent_dir = r'C:\Users\SystemName\PycharmProjects'

path = os.path.join(parent_dir, directory)
# os.mkdir(path)
directory2 = 'WastedDirectory2'
path2 = os.path.join(directory2, parent_dir)
# os.makedirs(path, path2)
print(os.listdir(parent_dir))
# os.remove() used to remove a file
# os.rmdir() used to remove an empty director
print(os.name)
print(os.path.abspath(r'PycharmProjects\Algorithms'))  # relative path
print(os.path.relpath(r'C:\Users\SystemName\PycharmProjects\Algorithms'))  # absolute path
