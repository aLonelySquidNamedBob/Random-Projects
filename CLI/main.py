import argparse

parser = argparse.ArgumentParser(description='Add some integers.')
parser.add_argument("name", help="name of the project")
args = parser.parse_args()
name = args.name
print(name)

