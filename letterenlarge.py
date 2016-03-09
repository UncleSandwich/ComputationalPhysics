#This is the font part, to record each charater
A=\
"\
    *       \n\
   * *      \n\
  *   *     \n\
 *     *    \n\
*********   \n\
*       *   \n\
*       *   \n\
*       *   \n\
*       *   \n\
"
B=\
"\
********    \n\
*       *   \n\
*        *  \n\
*       *   \n\
*********   \n\
*       *   \n\
*        *  \n\
*       *   \n\
********    \n\
"

##------------------------------##
#This is the splitting part, to split each line of one charater into a list

#print A,'\n',B

a = A.split('\n')
b = B.split('\n')
# l = L.split('\n')
# n = N.split('\n')
# g = G.split('\n')
# i = L.split('\n')
# x = X.split('\n')
# h = H.split('\n')

#print a,'\n',b

##------------------------------##
#This is the reading part, to read the inputed word from keyboard

print "Please enter less than 10 letters' word, only alphabet and space."
input = raw_input()
LETTER = []

def letter_read(input):
	for letter in input:
		if letter == 'a':
			LETTER.append(a)
		elif letter == 'b':
			LETTER.append(b)
		elif letter == 'l':
			LETTER.append(l)
		elif letter == 'n':
			LETTER.append(n)
		elif letter == 'g':
			LETTER.append(g)
		elif letter == 'i':
			LETTER.append(i)
		elif letter == 'x':
			LETTER.append(x)
		elif letter == 'h':
			LETTER.append(h)
		elif letter == ' ':
			LETTER.append(['      ']*10)
		else:
			print "Your word has contained one invalid charaters: ", letter
			break
	
# print len(input)
# letter_read(input)	
if len(input) <= 10:
	letter_read(input)
else:
	print "Your word contains more than 8 charaters!"

##------------------------------##
#This is the displaying part, to display the output
display = ''

#print LETTER

for indx in range(len(a)):
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

