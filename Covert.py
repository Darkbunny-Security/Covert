#! /usr/bin/env python
# -*- coding: Latin-1 -*-
#
# Coder by: //Agent-Smith
#	    //Agent-2k40
#
# -  DarkBunny
#
# Conversor de binario
#______________________________________________________________________

import os, sys, time;

sys.path.insert(0,'Setup/')
from stbin import *;
from logg import *;
from binst import *;

def Reply():
	REPLY = raw_input('[+] Deseja realizar:\n    1 - Palavra »»»» binario\n    2 - Binario »»»» palavra\n\nAguardando: ');
	if REPLY == '1':
        	os.system('clear');log(); print "[!] Iniciando\n";time.sleep(2);log(); bin(); time.sleep(2);os.system('clear'); log(); Reply()
	elif REPLY == '2':
        	os.system('clear');log(); print "[!] Iniciando\n";time.sleep(2);log(); cbin(); time.sleep(2);os.system('clear'); log(); Reply()
	else:
		print "[!] Opcao invalida"; time.sleep(2); os.system('clear');log(); Reply()

log();
Reply();
