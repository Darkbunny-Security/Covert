def cbin():
	import binascii, time, sys

        nome = int(input("Exemplo: 0b10111011\n\n[+] Insira binario para converter em palavras: "))
	RETURNST = binascii.unhexlify('%x' % nome)
	print (RETURNST); print '\n'

	time.sleep(2)

if __name__ == "__main__":
	cbin()
