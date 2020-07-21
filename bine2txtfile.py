import bine2lines

def bine2txtfile(txtfile1_name, txtfile2_name):

	f1 = open(txtfile1_name, 'r') 
	f2 = open(txtfile2_name, 'r')  

	lines_file1 =[]
	lines_file2 =[]

	for lines_in_file1 in f1:
		lines_file1.append(lines_in_file1)

	for lines_in_file2 in f2:
		lines_file2.append(lines_in_file2)

	#print(lines_file1)
	#print(lines_file2)

	for string1 in lines_file1:
		for string2 in lines_file2:	
			if lines_file1.index(string1) == lines_file2.index(string2) and lines_file1.index(string1) == 0 :
				print('string1:' + string1 + '/n' + 'string2:' + string2)
				#bine2lines.combine2Strings(string1, string2)
				break
			elif lines_file1.index(string1) == lines_file2.index(string2) and lines_file1.index(string1) == len(lines_file1)-1:
				string1 = string1 + '\n'
				print('string1(-1):' + string1 + '/n' + 'string2(-1):' + string2)
				#bine2lines.combine2Strings1(string1, string2)
				break
			elif lines_file1.index(string1) == lines_file2.index(string2):
				print('string1(0--1):' + string1 + '/n' + 'string2(0--1):' + string2)
				#bine2lines.combine2Strings1(string1, string2)
			else:
				pass
bine2txtfile('urllib2.txt', 'appetite.txt')

