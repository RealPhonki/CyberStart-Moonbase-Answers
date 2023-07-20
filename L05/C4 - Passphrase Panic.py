#
# Write a script to generate a passphrase by taking words from
# /tmp/words.txt
# The wordNumbers array holds three random numbers. Each number
# corresponds to a word in words.txt. So for example
# wordNumbers[1] is the second word in /tmp/words.txt.
# Put a space between each word and print it out
#


with open("/tmp/randomwordsnumbers.txt", "r") as file:
    data = file.read()

wordNumbers = data.rstrip().split("\n")

file = open("/tmp/words.txt")
content = file.readlines()
print(''.join([content[int(n)].strip('\n') + ' ' for n in wordNumbers]))
