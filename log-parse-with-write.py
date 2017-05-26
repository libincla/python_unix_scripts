#!/usr/bin/env python
#coding:utf-8

'''
Usage: this script needs to take one commandline argument
The argument is a log of file  to parse
'''


import sys

def dictify_logline(line):
	split_line = line.split('^^A')
	return {'remote_addr': split_line[1],
		'status':      split_line[10],
		'uri':	       split_line[8],
		'bytes_sent':  split_line[12],
		}
	
def generate_log(logfile):
	my_dict = {}
	
	with open('/tmp/result.log','w+') as f:
		for i in logfile:
			line_dict = dictify_logline(i)
			print line_dict
			f.write(str(line_dict) +"\n")
		
	try:
		bytes_sent = line_dict['bytes_sent']
	except ValueError:
		pass

	f.close()
	my_dict.setdefault(line_dict['remote_addr'],[]).append(bytes_sent)

	return my_dict



if __name__ == "__main__":
	if not len(sys.argv) > 1:
		print __doc__
		sys.exit(1)
	file_name = sys.argv[1]

	try:
		infile = open(file_name,'r')
	except IOError:
		print 'file error'
		print __doc__
		sys.exit(1)

	log_report =  generate_log(infile)
	#print log_report

	infile.close() 


