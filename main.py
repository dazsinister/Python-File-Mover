import os
import shutil


source_dir = 'C:\Users\User\Downloads'
target_dir_img = 'C:\Users\User\Pictures'
target_dir_video = 'C:\Users\User\Videos'
target_dir_exe = 'C:\Users\User\Installs'

while True:
file_names = os.listdir(source_dir)
for file_names in file_names:
    if os.path.join(source_dir, file_name).endswith('.exe')
        shutil.move(os.path.join(source_dir, file_name),target_dir_video)
    if os.path.join(source_dir, file_name).endswith('.mp4')
        shutil.move(os.path.join(source_dir, file_name),target_dir_video)
    if os.path.join(source_dir, file_name).endswith('.jpg')
        shutil.move(os.path.join(source_dir, file_name),target_dir_img)
