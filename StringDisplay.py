#This is the font part, importing from font.py
from font import *

##------------------------------##
#This is the splitting part, to split each line of one charater into a list

alphabet = []

alphabet_list = [A,B]#CDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in alphabet_list:
	# print letter
	# print letter.split('\n')
	alphabet.append(letter.split('\n'))


##------------------------------##
#This is the reading part, to read the inputed word from keyboard

print "Please enter less than 10 letters' word, only alphabet and space."

input = raw_input()

LETTER = []
eror = 0
#print 'error=', eror

def letter_read(inpt):
	for letter in inpt:
		index = 0
		if letter == 'a' or letter == 'A':
			LETTER.append(alphabet[0])
		elif letter == 'b' or letter == 'B':
			LETTER.append(alphabet[1])
		elif letter == 'c' or letter == 'C':
			LETTER.append(alphabet[2])
		elif letter == 'd' or letter == 'D':
			LETTER.append(alphabet[3])
		elif letter == 'e' or letter == 'E':
			LETTER.append(alphabet[4])
		elif letter == 'f' or letter == 'F':
			LETTER.append(alphabet[5])
		elif letter == 'g' or letter == 'G':
			LETTER.append(alphabet[6])
		elif letter == 'h' or letter == 'H':
			LETTER.append(alphabet[7])
		elif letter == 'i' or letter == 'I':
			LETTER.append(alphabet[8])
		elif letter == 'j' or letter == 'J':
			LETTER.append(alphabet[9])
		elif letter == 'k' or letter == 'K':
			LETTER.append(alphabet[10])
		elif letter == 'l' or letter == 'L':
			LETTER.append(alphabet[11])
		elif letter == 'm' or letter == 'M':
			LETTER.append(alphabet[12])
		elif letter == 'n' or letter == 'N':
			LETTER.append(alphabet[13])
		elif letter == 'o' or letter == 'O':
			LETTER.append(alphabet[14])
		elif letter == 'p' or letter == 'P':
			LETTER.append(alphabet[15])
		elif letter == 'q' or letter == 'Q':
			LETTER.append(alphabet[16])
		elif letter == 'r' or letter == 'R':
			LETTER.append(alphabet[17])
		elif letter == 's' or letter == 'S':
			LETTER.append(alphabet[18])
		elif letter == 't' or letter == 'T':
			LETTER.append(alphabet[19])
		elif letter == 'u' or letter == 'U':
			LETTER.append(alphabet[20])
		elif letter == 'v' or letter == 'V':
			LETTER.append(alphabet[21])
		elif letter == 'w' or letter == 'W':
			LETTER.append(alphabet[22])
		elif letter == 'x' or letter == 'X':
			LETTER.append(alphabet[23])
		elif letter == 'y' or letter == 'Y':
			LETTER.append(alphabet[24])
		elif letter == 'z' or letter == 'Z':
			LETTER.append(alphabet[25])
		elif letter == ' ':
			LETTER.append(['      ']*10)
		else:
			print "Your word has contained at least one invalid charaters: ", letter
			return 2
			


if len(input) > 10:
	eror = 1
elif len(input) <= 10:
	eror = letter_read(input)
else:
	eror = 3

# print len(input)

##------------------------------##
#This is the displaying part, to display the output

def display_letter():

	display = ''

	#print LETTER

	for indx in range(len(A.split('\n'))):
		for inx in range(len(LETTER)):
			display += LETTER[inx][indx]
		display += '\n'

	#print display


	import time
	import sys

	def delay_print(s):
		for c in s:
			sys.stdout.write( '%s' % c )
			sys.stdout.flush()
			time.sleep(0.005)

	delay_print(display)

#print 'error=', eror

if eror == None:
	display_letter()
elif eror == 1:
	print "Your word contains more than 10 charaters!"
elif eror == 3:
	print "An unknown error has occurred."

	
