'''pickmefly'''
import os
import time

title = ''
vformat = ''
flag = 0

for root, dirs, files in os.walk('.', topdown=True):
    for name in files:
        f_path = os.path.join(root, name)
        if(f_path[-4:] == '.zip') and (' - ' in f_path):
            title = f_path
            flag = 1
            title = title[:-4]
            title = title[2:]
            print('Unzipping...')
            print(f_path)
            os.system('start winrar e \"' + f_path + '\"')
            print('Unzip complete ?')
            os.system('pause')
            os.system('del \"' + f_path + '\"')
    break  # Prevent modification of subdirectories

if flag == 0:
    print('zip file not found.')
    os.system('pause')
    exit()

for root, dirs, files in os.walk('.', topdown=True):
    for name in files:
        f_path = os.path.join(root, name)
        if(f_path[-4:] == '.m4a') and (' - ' in f_path):
            vformat = 'DASH'
            os.system('rename \"' + f_path + '\" audio.m4a')
        if(f_path[-4:] == '.mp4') and (' - ' in f_path):
            os.system('rename \"' + f_path + '\" video.mp4')
        if(f_path[-4:] == '.flv') and (' - ' in f_path):
            vformat = 'flv'
            os.system('rename \"' + f_path + '\" video.flv')
        if(f_path[-4:] == '.ass') and (' - ' in f_path):
            os.system('rename \"' + f_path + '\" sub.ass')
    break  # Prevent modification of subdirectories

if vformat == 'DASH':
    os.system('ffmpeg -i sub.ass -i audio.m4a -i video.mp4  -c copy \"' + title + '\".mkv')
    os.system('del audio.m4a')
elif vformat == 'flv':
    os.system('ffmpeg -i sub.ass -i video.flv -c copy \"' + title + '\".mkv')
print('Merger completed.')
os.system('del video*')
os.system('del sub.ass')
print('Format: ' + vformat)
print('Calling PotPlayer...')
os.system('PotPlayerMini64 \"' + title + '\".mkv')
print('PotPlayer exited.')

ifdel = input("Delete media file ? (y/n)")
if ifdel == 'y' or ifdel == 'Y' or ifdel == '':
    os.system('del \"' + title + '\".mkv')
