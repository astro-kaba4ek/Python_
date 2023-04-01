# coding: utf-8

from matplotlib import pyplot as plt
from argparse import ArgumentParser
import requests
import numpy as np


parser = ArgumentParser() 
parser.add_argument("-bt_min", dest="bt", default=13)

bt = parser.parse_args().bt


payload = {"d": "objname, bt, vrot, modbest", # SELECT <...>
			"n": "meandata", # FROM <...>
			"sql": f"bt<{bt} and vrot IS NOT NULL and incl>60 and modbest IS NOT NULL", # WHERE <...>
			"ob": "", # ORDER BY <...>
			"a": "t[]" # Output as Formatted text
			}
col = 4 # #payload.d

response = requests.get("http://leda.univ-lyon1.fr/fG.cgi?c=o&of=1,leda,simbad&nra=l&nakd=1", 
# response = requests.get("http://leda.univ-lyon1.fr/fG.cgi", 
						params=payload)
	

if response.status_code != 200:
	print(response)
	print(f"URL: {response.url}")
	exit()


data = response.text.split("\n")

data = data[9+col : -6]

table = np.array([[0.0]*col for i in range(len(data))])


for i, str in enumerate(data):
	table[i][0], table[i][1], table[i][2] = list(map(float, str.split()[1:4]))

table[:, 3] = table[:, 0] - table[:, 2]


M = table[:, 3]
log10_v = np.log10(table[:, 1])

plt.xlabel("M")
plt.ylabel("log10_Vrot")
plt.title("Tully-Fisher relation")
plt.plot(M, log10_v, "r+")

plt.show()
