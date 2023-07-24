Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.x
>>> def binary_search(n, item):
...     left, right= 0, len(n)
...     while right > left:
...         middle = (left + right) // 2
...         if nums[middle] > item:
...             right = middle
...         elif nums[middle] < item :
...             left = middle + 1
...         else:
...             return middle
