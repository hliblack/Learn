# -*- coding: utf-8 -*-
import sys

# sys.argv 返回包含命令行参数的列表
script, encoding, error = sys.argv

def main(laguage_file, encoding, errors):
    """
    主函数，用于逐行读取语言文件并以指定编码打印。
    
    :param laguage_file: 语言文件的文件对象，用于逐行读取。
    :param encoding: 指定的文本编码。
    :param errors: 处理编码错误的策略。
    :return: 递归调用自身，直到文件读取完毕。
    """
    line = laguage_file.readline() # 读取文件中的下一行
    if line:
        print_line(line, encoding, errors)
        return main(laguage_file, encoding, errors) # 递归读取并处理文件的每一行
    
def print_line(line, encoding, errors):
    """
    打印处理后的文本行。
    
    :param line: 未经处理的文本行。
    :param encoding: 指定的文本编码。
    :param errors: 处理编码错误的策略。
    """
    next_lang = line.strip() # 去除行两端的空白字符
    raw_bytes = next_lang.encode(encoding, errors=errors) # 将文本行编码为字节串
    cooked_string = raw_bytes.decode(encoding, errors=errors) # 将字节串解码回文本

    print(raw_bytes, "<===>", cooked_string) # 打印原始字节串及其解码后的文本

languages = open('languages.txt', encoding='utf-8') # 打开语言文件

main(languages, encoding, error) # 调用主函数处理文件