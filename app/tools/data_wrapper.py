import time as stime
import random
from datetime import datetime, timedelta, time , date

def _str2date(dstr):
	ym = [int(d) for d in dstr.split('-')]
	return date(ym[0],ym[1],ym[2])

def _str2time(tstr):
	tm = [int(t) for t in tstr.split(':')]
	return time(tm[0],tm[1])

def _mk_timestamp(dt):
	return stime.mktime(dt.timetuple())

def _get_random():
	return str(int(_mk_timestamp(datetime.now())/random.randint(2,100)))

def _rename_file(filename):
	offset = filename.rfind('.')
	last_str = filename[offset:]
	final_name = _get_random() + str(last_str)
	return final_name

if __name__ == '__main__':
	s = 'test.pdf'
	print _rename_file(s)