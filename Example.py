# /usr/bin/python
#coding: utf-8
__author__ = 'xujw'

def less(v,w):
	return v < w

def exch(a,i,j):
	t = a[i]
	a[i] = a[j]
	a[j] = a[i]

def show(a):
	print(a)

def isSorted(a):
	for i in range(1,len(a),1):
		if less(a[i],a[i-1]):
			return False
	return True


if __name__ == "__main__":
	print(less(3,5))
	print(less("a","b"))
	print(less("张","王"))
	print(less("d","c"))
	print less("徐","g")
	print "--------------"
	a = [3,1,5,2,9,6]
	print isSorted(a)