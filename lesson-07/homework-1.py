import os


def create_dir(parent, child):
    child_path = os.path.join(parent, child)
    if not os.path.exists(child_path):
        os.mkdir(child_path)


root_path = 'my_project'
if not os.path.exists(root_path):
    os.mkdir(root_path)
create_dir(root_path, 'settings')
create_dir(root_path, 'authapp')
create_dir(root_path, 'adminapp')
create_dir(root_path, 'authapp')

