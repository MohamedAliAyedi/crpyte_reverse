print("crypte and decrypte message with reverse it \n")
msg = raw_input("msg > ")
word = ''
i = len(msg) - 1
while i >= 0:
 word = word + msg[i]
 i = i - 1
print("\nResulta >  "+word)
