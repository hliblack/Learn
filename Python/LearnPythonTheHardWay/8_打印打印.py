formatter = "{}, {}, {}, {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("a", "b", "c", "d"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."))