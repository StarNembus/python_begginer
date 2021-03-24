import os
from sys import argv
my_dict = {1000: 0, 10000: 0, 1000000: 0}

folder = argv[1]
if os.path.isdir(folder):
    root_path = os.walk(folder)
    for i in root_path:
        inner_list = i[2]
        for j in inner_list:
            file = os.path.join(i[0], j)
            size = os.stat(file).st_size
            for k in sorted(my_dict.keys()):
                if size <= k:
                    my_dict[k] += 1
else:
    print("Директории не существует")

print(my_dict)
