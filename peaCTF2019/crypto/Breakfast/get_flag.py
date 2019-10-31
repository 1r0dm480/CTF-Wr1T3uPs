#! /usr/bin/python



lookup = {'A':'00000', 'B':'00001', 'C':'00010', 'D':'00011', 'E':'00100',

		'F':'00101', 'G':'00110', 'H':'00111', 'I':'01000', 'K':'01001',

		'L':'01010', 'M':'01011', 'N':'01100', 'O':'01101', 'P':'01110',

		'Q':'01111', 'R':'10000', 'S':'10001', 'T':'10010', 'U':'10011',

		'W':'10100', 'X':'10101', 'Y':'10110', 'Z':'10111'}



def decrypt(message):

	decipher = ''

	i = 0



	while True :

		if(i < len(message)-4):

			substr = message[i:i + 5]

			if(substr[0] != ' '):



				decipher += list(lookup.keys())[list(lookup.values()).index(substr)]

				i += 5



			else:

				decipher += ' '

				i += 1

		else:

			break



	return decipher



def main():

	message = "01110001000000000010100100010100100001100011010100000000010100101010100010010001"

	result = decrypt(message)

	print (result.lower())



if __name__ == '__main__':

	main() 
