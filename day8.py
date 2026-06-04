Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 t=(1,2,3,4,5)
 
SyntaxError: unexpected indent
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1,1,1)
t
(1, 1, 1, 1, 1, 1)
t=(1,1.1,'tryu',[])
t
(1, 1.1, 'tryu', [])
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
h=(90,80,70)
t+h
(10, 20, 30, 40, 50, 90, 80, 70)
t*4
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t
(10, 20, 30, 40, 50)
t[1]
20
t[2]
30
t[4]
50
t[3]
40
t[0]
10
 t[:]
 
SyntaxError: unexpected indent
t
(10, 20, 30, 40, 50)
t[:3]
(10, 20, 30)
t[:4]
(10, 20, 30, 40)
t[2:]
(30, 40, 50)
(30, 40, 50)
(30, 40, 50)



======================================== RESTART: Shell =======================================
t[:3]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t[:3]
NameError: name 't' is not defined

t
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    t
NameError: name 't' is not defined
t=(10,20,30,40,50)
t[:4]
(10, 20, 30, 40)
t
(10, 20, 30, 40, 50)
10 in t
True
30 in t
True
60 i t
SyntaxError: invalid syntax
60 in t
False
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
len(t)
5
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
max(t)
50
sum(t)
150
t.count()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given)
t.count(10)
1
t.index(10)
0
t=1,2,3,4,5,6,7
t
(1, 2, 3, 4, 5, 6, 7)
a,b,c=(1,2,3)
a
1
b
2
c
3
a=(1,2,4)
a
(1, 2, 4)
x,y,z=a
x
1
y
2
z
4
t=1,2,3,[4,5,6],7,8)
SyntaxError: unmatched ')'
t=(1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[:1]
(1,)
t[::-1]
(8, 7, [4, 5, 6], 3, 2, 1)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[2]
3
t[4]
7
t[3]
[4, 5, 6]
t[2]=4
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t[2]=4
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t[3]
[4, 5, 6]
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
t[3].append(30)
t
(1, 2, 3, [4, 5, 6, 10, 30], 7, 8)
t[3].pop()
30
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
t[3].pop()
10
t
(1, 2, 3, [4, 5, 6], 7, 8)

==================================================================================== RESTART: Shell ====================================================================================
s=set()
s={1,1,1,1,1,1,}
s
{1}
s={7556,866,7555,87}
s
{866, 7555, 7556, 87}
s=set()
s.add(1)
s
{1}
s.add(46.346)
s
{1, 46.346}
s.add("hjky")
s
{1, 'hjky', 46.346}
s.add([1,2])
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    s.add([1,2])
TypeError: unhashable type: 'list'
s.add([1])
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s.add([1])
TypeError: unhashable type: 'list'
s
{1, 'hjky', 46.346}
1 in s
True
2 in s
False
46.346 not in s
False
a={1,2,3,45,6,7}
b={6,7,8,9}
a|b
{1, 2, 3, 6, 7, 8, 9, 45}
a.union(b)
{1, 2, 3, 6, 7, 8, 9, 45}
a.intersection(b)
{6, 7}
a&b
{6, 7}
a-b
{1, 2, 3, 45}
a^b
{1, 2, 3, 8, 9, 45}
#{1}{2}{3}{5}
a<={1}
False
a>={1}
True
a
{1, 2, 3, 6, 7, 45}
b
{8, 9, 6, 7}
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a.add(17)
a
{1, 2, 3, 17, 6, 7, 45}
a.update({11,12,13})
a
{1, 2, 3, 6, 7, 11, 12, 45, 13, 17}
a.pop
<built-in method pop of set object at 0x000001BD51DEFCA0>
>>> a.pop()
1
>>> a
{2, 3, 6, 7, 11, 12, 45, 13, 17}
>>> a.remove(6)
>>> 
>>> a.discard(3)
>>> a
{2, 7, 11, 12, 45, 13, 17}
>>> a.remove(6)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a.remove(6)
KeyError: 6
>>> a
{2, 7, 11, 12, 45, 13, 17}
>>> a.clear()
>>> a
set()
>>> a={1,23,4,57,336}
>>> b={1,3,4,45,}
>>> a.intersection_update(b)
>>> a
{1, 4}
>>> b
{1, 3, 4, 45}
>>> c=b
\
>>> c
{1, 3, 4, 45}
>>> d=c.copy()
>>> d
{1, 3, 4, 45}
>>> c
{1, 3, 4, 45}
>>> d.add(10)
>>> d
{1, 3, 4, 10, 45}
>>> len(c)
4
>>> min(c)
1
>>> max(c)
45
>>> sorted(c)
[1, 3, 4, 45]
