Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=15
>>> y=4
>>> print('x+y=',x+y)
x+y= 19
>>> print('x-y')
x-y
>>> 
KeyboardInterrupt
>>> print('x-y=',x-y)
x-y= 11
>>> print('x/y=',x/y)
x/y= 3.75
>>> print('x//y=',x//y)
x//y= 3
>>> print('x**y=',x**y)
x**y= 50625
>>> x=10
>>> y=12
>>> print('x>y=',x>y)
x>y= False
>>> print('x<y',x<y)
x<y True
>>> print('x==y=',x==y)
x==y= False
>>> print('x>=y=',x>=y)
x>=y= False
>>> print('x<=y=',x<=y)
x<=y= True
>>> x=true
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x=true
NameError: name 'true' is not defined
>>> x=True
>>> y=False
>>> print('x and y is')
x and y is
>>> 
KeyboardInterrupt
>>>  print('x and y is',x and y)
 
SyntaxError: unexpected indent
>>>  print('x and y is',x and y)
 
SyntaxError: unexpected indent
>>> print('x and y',x and y)
x and y False
>>> printf('x or y',x or y)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    printf('x or y',x or y)
NameError: name 'printf' is not defined
>>> print('x or y',x or y)
x or y True
>>>  print('not x',not x)
 
SyntaxError: unexpected indent
>>> print('not x ',not x)
not x  False
>>> x1=5
>>> y1=5
>>> x2='hello'
>>> y2='hello'
>>> x3=[1,2,3]
>>> y3=[1,2,3]
>>> print(x1 is not y1)
False
>>> print(x2 is y2)
True
>>> print(x3 is y3)
False
>>> x='hello world'
>>> y={1:'a',2:'b'}
>>> print('h' in x)
True
>>> print('Hello' not in x)
True
>>> print(1 in y)
True
>>> print('a' in y)
False
>>> 