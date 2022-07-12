from os import read
import random
import time
import asyncio
from collections import Counter

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)
    return wrapped

@background
def word_count(str):
	counts = dict()

	for char in ':,.-;\/n':
		str = str.replace(char, ' ')

	str = str.lower()
	words = str.split()

	start = time.time()
	for word in words:
		if word in counts:
			counts[word]+=1
		else:
			counts[word] = 1
	end = time.time()
	print ('Time: ', round(end-start, 3))
	return counts


i = 1
while (i == 1):
	length = int(input("Enter array size: "))
	if length == 1:
		file = open('1test.txt', 'rt')
	if length == 100000:
		file = open('100000test.txt', 'rt')
	if length == 200000:
		file = open('200000test.txt', 'rt')
	if length == 300000:
		file = open('300000test.txt', 'rt')
	if length == 400000:
		file = open('400000test.txt', 'rt')
	if length == 500000:
		file = open('500000test.txt', 'rt')
	if length == 600000:
		file = open('600000test.txt', 'rt')
	if length == 700000:
		file = open('700000test.txt', 'rt')
	if length == 800000:
		file = open('800000test.txt', 'rt')
	if length == 900000:
		file = open('900000test.txt', 'rt')
	if length == 1000000:
		file = open('1000000test.txt', 'rt')

	data = file.read()
	#word_count(data)
	background(word_count(data))
print ()
