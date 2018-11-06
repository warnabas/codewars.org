#encryptThis("Hello") == "72olle"
#encryptThis("good") == "103doo"
#encryptThis("hello world") == "104olle 119drlo"
def encrypt_this(text):
    
    words=text.split( )
    
    result=''
	
    for i in list(range(len(words))):

		if (len(words[i])==1):
			
			result += repr(ord(words[i][0])) + ' ' 

		elif (len(words[i])==2):
		
			result += repr(ord(words[i][0])) + words[i][1] + ' '

		else:

			result += repr(ord(words[i][0])) + words[i][(len(words[i])-1)] + words[i][2:len(words[i])-1] + words[i][1] + ' '


    return result[:len(result)-1]    	

print encrypt_this("hello world")


			