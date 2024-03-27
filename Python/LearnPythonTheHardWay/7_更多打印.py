print("Mary had a little lamb.")
print("Its fleece was white as {}.".format("snow"))
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# 在Python的print()函数中，end 参数用于指定每次打印结束后添加的结束字符，默认情况下 end='\n'，即在输出内容后添加一个换行符，使得下一次的 print() 输出出现在新的一行。
# 当你改变 end 参数的值时，你可以控制每次调用 print() 后输出的内容末尾是什么字符

print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)