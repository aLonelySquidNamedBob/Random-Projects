import os

path = "C:\\Users\\nicop_ny6irwr\\Dropbox\\Coding\\Python"
for root, dirs, old_files in os.walk(path):
    new_files = []
    for old_file in old_files:
        new_file = old_file.replace(' ', '_')
        new_files.append(new_file)

    for new_file, old_file in zip(new_files, old_files):
        os.rename(f"{root}\\{old_file}", f"{root}\\{new_file}")
