#coding: utf-8

import os
import argparse
import threading
import Queue
import re
import subprocess


#defind global arguments
sqlmap_url_list = list()
if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("--sqlmap", dest="sqlmap", help="input the file name contain URLs(Also arguments)", type=str)

	args = parser.parse_args()

#default sqlmap's command:
#python sqlmap.py -u "target url" --threads=10 --tamper=randomcomments --random-agent --level=5 
	try:
		with open(args.sqlmap, 'r') as f:
			for url in f.readlines():
				#check the URL format
				if url[0:7] == 'http://':
					url = re.sub('\s', '',url)
					sqlmap_url_list.append(url)
				#read urls, and output for commandlins's
				for i in sqlmap_url_list: 
					output_commands = r'python sqlmap.py -u ' + i + r' --threads=10 --tamper=randomcomments --random-agent --level=5'
					process = subprocess.Popen(output_commands, stdin=subprocess.PIPE, 	stdout= subprocess.PIPE, stderr= subprocess.PIPE, shell= False)
					while process.poll() == None:
						print process.stdout.readline()
	except Exception as e:
		print e