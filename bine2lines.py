def combine2Strings(string1, string2):
	newString = string1 + string2
	# lines.append(newString)
	# for line in lines:
		# if lines.index(line) == 0:
	with open('newfile.txt', 'x') as f:
		f.write(newString)
		# else:
			# with open('newfile.txt', 'a') as f1:
				# f1.write(line)
def combine2Strings1(string1, string2):
	newString = string1 + string2
	with open('newfile.txt', 'a') as f:
		f.write(newString)
	pass

# string0 = 'can I do it?'
# string1 = 'I have no idea, but let me have a try.'
# combine2Strings(string0, string1)

# print(lines)


