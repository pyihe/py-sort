from collections import defaultdict

#插入排序: 是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
def InsertSort(array):
	for i in range(1, len(array)):
		key = array[i]

		j = i - 1

		while j >= 0 and key < array[j]:
			array[j+1] = array[j]
			j -= 1
		array[j+1] = key



#快速排序:快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

#步骤为：

#挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
#分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
#递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
#递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。
#选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。
#找基准值
def partition(array, low, high):
	i = (low -1)
	pivot = array[high]
	for j in range(low, high):
		if array[j] <= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]
	array[i+1], array[high] = array[high], array[i+1]		

	return (i + 1)

def QuickSort(array, low, high):
	if low < high:
		pivot = partition(array, low, high)

		QuickSort(array, low, pivot-1)
		QuickSort(array, pivot+1, high)


#选择排序:选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，
#存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
def SelectSort(array, size):
	for i in range(size):
		minIdx = i
		for j in range(i+1, size):
			if array[minIdx] > array[j]:
				minIdx = j
		array[i], array[minIdx] = array[minIdx], array[i]		


#冒泡排序:冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
#走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。
def BubbleSort(array, size):
	for i in range(size):
		for j in range(0, size-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]


#归并排序: 归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
#分治法:
#分割：递归地把当前序列平均分割成两半。
#集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
def merge(array, left, mid, right):
	n1 = mid - left + 1
	n2 = right - mid

	#创建临时数组
	L, R = [0] * (n1), [0] * (n2)

	#将元素拷贝到临时数组
	for i in range(0, n1):
		L[i] = arr[left + i]

	for j in range(0, n2):
		R[j] = arr[mid+1+j]

	#归并临时	到array[left...right]
	i, j, k = 0, 0, left

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			array[k] = L[i]
			i += 1
		else:
			array[k] = R[j]
			j += 1
		k += 1
		
	#拷贝L[]的保留元素
	while i < n1:
		array[k] = L[i]
		i += 1
		k += 1
			
	while j < n2:
		array[k] = R[j]
		j += 1
		k += 1

def MergeSort(array, left, right):
	if left >= right:
		return
	mid = int((left + (right -1))/2)	

	MergeSort(array, left, mid)
	MergeSort(array, mid+1, right)
	merge(array, left, mid, right)



#堆排序:堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
#即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。
def heap(array, size, idx):
	largest = idx
	left = 2 * idx + 1
	right = 2 * idx + 2

	if left < size and array[idx] < array[left]:
		largest = left
	if right < size and array[largest] < array[right]:
		largest = right
	if largest != idx:
		array[idx], array[largest] = array[largest], array[idx]
		heap(array, size, largest)

def HeapSort(array, size):
	for i in range(size, -1, -1):
		heap(array, size, i)

	for i in range(size-1, 0, -1)	:
		array[i], array[0] = array[0], array[i]
		heap(array, i, 0)

#计数排序: 计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
def CountSort(array, size):
	outPut = [0 for i in range(256)]

	count = [0 for i in range(256)]

	ans = ["" for _ in array]

	for i in arr:
		count[ord(i)] += 1

	for i in range(256):
		count[i] += count[i-1]

	for i in range(size):
		outPut[count[ord(array[i])] -1] = array[i]
		count[ord(array[i])] -= 1

	for i in range(len(array)):
		ans[i] = outPut[i]
	return ans	


#希尔排序: 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。
#希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
def ShellSort(array, size):
	gap = int(size/2)

	while gap > 0:
		for i in range(gap, size):
			temp = array[i]
			j = i
			while j >= gap and array[j-gap] > temp:
				array[j] = array[j-gap]
				j -= gap
			array[j] = temp
		gap = int(gap/2)	


#拓扑排序
class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.V = vertices

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def topologicalSortUtil(self, v, visited, stack):
		visited[v] = True

		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)
		stack.insert(0, v)

	def topologicalSort(self):
		visited = [False]*self.V
		stack = []

		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)
		print(stack)		