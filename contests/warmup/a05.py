s = input()

if int(s) == sum(map(lambda x: int(x)**len(s), s)):
    print(f'{s} is a narcissistic number.')
else:
    print(f'{s} is not a narcissistic number.')