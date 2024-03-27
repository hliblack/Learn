from sys import argv
from os.path import exists

# script, from_file, to_file = argv

# print(f'Copying from {from_file} to {to_file}...')

# # we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# indata = open(from_file).read()

# print(f'The input file is {len(indata)} bytes long')
# print(f'Does the output file exist? {exists(to_file)}')
# print(f'Ready, hit RETURN to continue, CTRL-C to abort')
# input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print('Alright, all done.')

# out_file.close()
# in_file.close()

with open("17_in_file.txt", "r") as f:
    data = f.read()
    print(data)

if(exists("17_out_file.txt")):
    with open("17_out_file.txt", "w") as f:
        f.write(data)
        f.close()

print(open("17_out_file.txt").read())