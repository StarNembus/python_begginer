import os
import shutil


temp_path = "my_project/templates"
if not os.path.exists(temp_path):
    os.mkdir(temp_path)

root_path = os.walk("my_project")
dir_list = list()
for i in root_path:
    if i[0].endswith("templates"):
        if len(i[1]) == 1:
            tmp = os.path.join(temp_path, i[1][0])
            if not os.path.exists(tmp):
                os.mkdir(tmp)
            dir_list.append(i[1][0])

print(dir_list)
print("----------------")

for i in dir_list:
    root_path = os.walk("my_project")
    for j in root_path:
        if j[0].endswith(str(os.path.join(i, "templates", i))):
            for k in j[2]:
                print(k, temp_path, i, k)
                shutil.copy(str(os.path.join(j[0], k)), str(os.path.join(temp_path, i)))
