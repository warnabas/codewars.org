#decipherThis('72olle 103doo 100ya') // 'Hello good day'
#decipherThis('82yade 115te 103o')   // 'Ready set go'
def decipher_this(string):
		
	string = string.split(' ')
	print(string)
	res=""

	for n in list(range((len(string)))):
		#print len(string)
		l = len(string[n])
		#print l

		if (l > 2):

					res = res + str(ord(string[n][0])) + \
						string[n][len(string[n])-1] + \
						string[n][2:len(string[n])-2] + \
						string[n][1] + " "
					print(string[n][0])
		elif (l==2): 

					res += str(ord(string[n][0])) + string[n][1]

		else: 
					res += str(ord(string[n][0]))

	return res[:len(res)-1]


print(decipher_this('82yade 115te 103o'))


