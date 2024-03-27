# 示例：使用不同的错误处理策略解码
invalid_utf8_bytes = b'\xed\xa0\x80abc'  # 不合法的UTF-8编码

try:
    decoded_str = invalid_utf8_bytes.decode("utf-8")  # 默认 strict 模式，会抛出 UnicodeDecodeError
except UnicodeDecodeError as e:
    print(f"Strict mode error: {e}")

decoded_ignore = invalid_utf8_bytes.decode("utf-8", errors='ignore')  # 忽略无法解码的字节
decoded_replace = invalid_utf8_bytes.decode("utf-8", errors='replace')  # 替换无法解码的字节
print(decoded_ignore)
print(decoded_replace)

print("--------------------------------------------------------------------------------------------------------------")

with open("23_decode.txt", "rb") as f:
    for line in f:
        print(line.decode("utf-8", errors='replace'))