#! /usr/bin/python
# -*- coding:utf-8 -*-
import time as stime
import random
import re
from datetime import datetime, timedelta, time , date

def removeHTMLWidth(html):
	dr = re.compile('width[^>]*px',re.S)
	dr2 = re.compile('width[^>]*%',re.S)
	htmlStr = re.sub(dr,'',html)
	htmlStr = re.sub(dr2,'',htmlStr)
	return htmlStr

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
	#s = 'test.pdf'
	#print _rename_file(s)
	print removeHTMLWidth('<p><img src="http://aero.wisdomriver.com.cn/_uploads/files/74801033.jpg" style="width:100px" /></p>')