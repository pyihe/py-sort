#二分查找:二分搜索是一种在有序数组中查找某一特定元素的搜索算法。搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；
#如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，
#则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。
def BinarySearch(array, left, right, target):
	#判断right和left大小关系
	if left > right:
		return -1
	#获取中间位置
	mid = int(left + (right - left)/2)	

	if target == array[mid]: #如果元素正好在中间
		return mid
	elif target > array[mid]: #元素大于中间元素，则在右边继续查找
		return BinarySearch(array, mid+1, right, target)
	else: #否则在左边继续查找元素
		return BinarySearch(array, left, mid-1, target)


#线性查找:按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止。
def LineSearch(array, size, target):
	for i in range(0, size):
		if (array[i] == target):
			return i
	return -1		