# 从sys模块导入argv
from sys import argv 

# 解析命令行参数，获取脚本名和文件名
script, filename = argv

# 打印准备删除文件的提示信息
print(f"Wr are going to earse {filename}.")
print("If you don't want that, hit CTRL=C (^C).")
print("If you do want that,hit RETRUN.")

# 等待用户确认
input("?")

# 打印打开文件的提示
print("Opening the file...")

# 以写入模式打开文件
target = open(filename, 'a')

# 清空文件内容
print("Truncating the file. Goodbye")
target.truncate()

# 提示用户输入三行内容
print("Now I am going to ask you for three lines.")

# 读取用户输入的三行内容
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# 打印将写入文件的提示
print("I'm going to write these to the file.")

# 将用户输入的内容写入文件
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

target.close

readfile = open(filename, 'r')
print(readfile.read())

# 写入文件
with open("16_sample.txt", "a") as file:
    file.write("This is a new line\n")
    file.write("This is another new line\n")
    file.close()

# 读取文件
with open("16_sample.txt", "r") as file:
    print(file.read())

# 错误用法
with open("16_sample.txt", "r+w") as file:
    file.write("This is a third line\n")
    file.seek(0)
    print(file.read())
    file.close()
