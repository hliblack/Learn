from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
input_again = input("> ")

read_again = open(file_again)

print(read_again.read())