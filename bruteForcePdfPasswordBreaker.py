import PyPDF2

#file to be decrypted
pdf_file = 'c://users//daniel//desktop//encryptedWatermark.pdf'


def decrypt(file):
	print('Please be patient, human. This may take awhile.')
	pdfReader = PyPDF2.PdfFileReader(file)
	dictionary = open('Dictionary.txt').read()
	words = dictionary.split()
	attempts = 0
	for word in words:
		attemptUpper = pdfReader.decrypt(word.upper())
		attemptLower = pdfReader.decrypt(word.lower())
		if attemptUpper == 1:
			input('The password is: ' + word.upper())
			break
		if attemptLower == 1:
			input('The password is: ' + word.lower())
			break
		attempts+=2
		if (attempts/1000).is_integer() == True:
			print('Please be patient, human. I have tried ' + str(attempts) + ' passwords.')

decrypt(pdf_file)