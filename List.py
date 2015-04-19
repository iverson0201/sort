#!/usr/bin/python
# coding: utf-8
__author__ = 'xujw'

word = "abcdefg"

t1 = word[2]
print t1

t2 = word[1:3]
print t2

t3 = word[:2]
print t3

t4 = word[0]
print t4

t5 = word[-2]
print t5

print "--------------------"

for i in word:
	print i

print range(len(word))

print "--------------------"

print list(xrange(len(word)))

print (xrange(len(word)))
