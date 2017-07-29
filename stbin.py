def bin():
	import time, sys
	
	nome = raw_input("[+] Insira nome para corversao binaria: ")
	RETURNBIN = ' '.join(format(ord(x), 'b') for x in nome)
	print (RETURNBIN); print "\n"

	time.sleep(2)

if __name__ == "__main__":
	bin();
