'''
正则表达式
'''
#！/usr/bin/env python 
#coding=utf-8

import re

pattern = re.compile(r'(\w+) (\w+)(?P<sign>.*)')
m=re.match(pattern, 'hello world!')
print('m.string:',m.string)
print('m.re:',m.re)
print('m.pos:',m.pos)
print('m.endpos:',m.endpos)
print('m.lastindex:',m.lastindex)
print('m.lastgroup:',m.lastgroup)
print('m.group():',m.group())
print('m.group(1,2):',m.group(1,2))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print( "m.start(2):", m.start(2))
print("m.end(2):", m.end(2))
print("m.span(2):", m.span(2))
print(r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3'))

# finditer()
pattern=re.compile(r'\d+')
for m in re.finditer(pattern, 'one1two2three3four4'):
    print(m.group(),)

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print(re.sub(pattern,r'\2 \1', s))

def func(m):
    print(m.group(1))
    return m.group(1).title() + ' ' + m.group(2).title()   # title()首字母大写

print(re.findall(pattern, s))     #  [('i', 'say'), ('hello', 'world')]
print(re.sub(pattern,func, s))

