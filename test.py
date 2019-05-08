import sys
import os

f = open("unit_config_index.txt", "r")
new = f.readlines()
for x in range(0, 184):
	os.system("echo %s >> new_unit_config_index.txt" % new[x].split(" ")[0])
f.close()
