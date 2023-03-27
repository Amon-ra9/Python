import os, shutil

path = r"C:/Users/amonra/Downloads/"

file_names = os.listdir(path)

folder_names = ['csv files', 'image files', 'text files', 'video files', 'music files', 'executable files', 'pdf files']

for loop in range(0, 7):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_names:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    elif ".mp4" in file and not os.path.exists(path + "video files/" + file):
        shutil.move(path + file, path + "video files/" + file)
    elif ".mp3" in file and not os.path.exists(path + "music files/" + file):
        shutil.move(path + file, path + "music files/" + file)
    elif ".exe" in file and not os.path.exists(path + "executable files/" + file):
        shutil.move(path + file, path + "executable files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)