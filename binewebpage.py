import urllib.request
from bs4 import BeautifulSoup
import bine2txtfile

def geturl2txtfile(url, txtfile_name):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	text = soup.get_text()

	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)

	with open(txtfile_name, 'x') as f:
		f.write(text)

'''
the code above reference the answer in [Extracting text from HTML file using Python - Stack Overflow](https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python)
& [HOWTO Fetch Internet Resources Using The urllib Package — Python 3.8.4 documentation](https://docs.python.org/3/howto/urllib2.html)
'''




url1 = 'https://docs.python.org/3/tutorial/appetite.html'
txtfile1_name = 'appetite.txt'
geturl2txtfile(url1, txtfile1_name)

url2 ='https://docs.python.org/3/howto/urllib2.html'
txtfile2_name = 'urllib2.txt'
geturl2txtfile(url2, txtfile2_name)

bine2txtfile.bine2txtfile(txtfile1_name,txtfile2_name)



