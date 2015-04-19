# /usr/bin/python
#coding: utf-8
__author__ = 'xujw'

def less(v,w):
	return v < w

def exch(a,i,j):
	t = a[i]
	a[i] = a[j]
	a[j] = t

def sort(a):#插入排序
	n = len(a)
	for i in range(1,n):
		#a[i]插入到a[i-1,i-2,i-3]之中...
		j = i
		while j > 0 and less(a[j],a[j-1]):
			exch(a,j,j-1)
			j = j - 1

def show(a):
	print(a)

if __name__ == "__main__":
	a = [3,5,9,2]
	sort(a)
	show(a)