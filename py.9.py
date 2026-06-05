Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d=[]
d=dict()
typr(d)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    typr(d)
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
 d[23]
 
SyntaxError: unexpected indent
d[23]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[23]
KeyError: 23
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[23]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d[23]
KeyError: 23
d={}
d[1=1
  
SyntaxError: '[' was never closed
d[1]=1
  
d
  
{1: 1}
d[23]=23.4
  
d[3]
  
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d[3]
KeyError: 3

==================================== RESTART: Shell ===================================
d=
  
SyntaxError: invalid syntax
d={}
  
d[1]=2
  
d[2]=2
  
d[3]=2
  
d[4]=2
  
d
  
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
  
2
d=
  
SyntaxError: invalid syntax
d={1:2,2:4,3:6,4:8,5:10,6:12}
  
d[4]
  
8
d[6]
  
12
d[1]
  
2
d[4]
  
8
d={'veda':120,'nandana':16,'sru':90,'rishi':89}
  
d
  
{'veda': 120, 'nandana': 16, 'sru': 90, 'rishi': 89}
d['veda']
  
120
d['rishi']
  
89
d.get('sai')
  
d.get('subbu')
  
d
  
{'veda': 120, 'nandana': 16, 'sru': 90, 'rishi': 89}
d.get('bab','user not found')
  
'user not found'
d.get('veda','user not found')
  
120
d
  
{'veda': 120, 'nandana': 16, 'sru': 90, 'rishi': 89}
'veda' in d
  
True
'sru' in d
  
True
'rishi' not in d
  
False
d.keys
  
<built-in method keys of dict object at 0x000001F3800B3FC0>
d.keys()
  
dict_keys(['veda', 'nandana', 'sru', 'rishi'])
d.values()
  
dict_values([120, 16, 90, 89])
d.items()
  
dict_items([('veda', 120), ('nandana', 16), ('sru', 90), ('rishi', 89)])
sorted(d)
  
['nandana', 'rishi', 'sru', 'veda']
max(d)
  
'veda'
min(d)
  
'nandana'
len(d)
  
4
d
  
{'veda': 120, 'nandana': 16, 'sru': 90, 'rishi': 89}
d['vead']
  
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    d['vead']
KeyError: 'vead'
d['veda']
  
120
d
  
{'veda': 120, 'nandana': 16, 'sru': 90, 'rishi': 89}
d['sru']
  
90
d.update({'nandu':100,'madhu':80})
  
d
  
{'veda': 120, 'nandana': 16, 'sru': 90, 'rishi': 89, 'nandu': 100, 'madhu': 80}
d.popitem()
  
('madhu', 80)
d
  
{'veda': 120, 'nandana': 16, 'sru': 90, 'rishi': 89, 'nandu': 100}
d.pop()
  
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d.pop('subbu')
...   
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    d.pop('subbu')
KeyError: 'subbu'
>>> d.pop('nandu')
...   
100
>>> del d['nandana']
...   
>>> d
...   
{'veda': 120, 'sru': 90, 'rishi': 89}
>>> d.clear()
...   
>>> d
...   
{}
>>> d={'veda':120,'nandana':16,'sru':90,'rishi':89}
... d
...   
SyntaxError: multiple statements found while compiling a single statement
>>> d
...   
{}
>>> d={'veda':120,'nandana':16,'sru':90,'rishi':89}
... 
>>> d
...   
{'veda': 120, 'nandana': 16, 'sru': 90, 'rishi': 89}
>>> d.setdefault('rishi',0)
...   
89
>>> d
...   
{'veda': 120, 'nandana': 16, 'sru': 90, 'rishi': 89}
>>> d.getdefault('veda',0)
...   
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    d.getdefault('veda',0)
AttributeError: 'dict' object has no attribute 'getdefault'. Did you mean: 'setdefault'?
