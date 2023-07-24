xxPython 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def binary_search(n, item, start, end):
...     middle = (start + end) // 2
...     if start == end:
...         return None
...     if n[middle] > item:
...         return binary_search(n, item, start, middle)
...     elif nums[middle] < item:
...         return binary_search(n, item, middle + 1, end)
...     else:
