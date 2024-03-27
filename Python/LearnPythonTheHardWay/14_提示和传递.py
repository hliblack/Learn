from sys import argv

script, user_name = argv
prompt = ">>> "

print(f'Hi {user_name}! I\'m the {script} script.')
print('I\'m going to ask you a few questions.')
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f'What\'s your favorite color?')
color = input(prompt)

print(f'What\'s your favorite number?')
number = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
And your favorite color is {color}.
And your favorite number is {number}.
""")