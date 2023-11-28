# -*- coding: utf-8 -*-
"""week2pythontuples,sets,dict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Y3yrhULTW9Q9asWCBk_-igz-EOUC-L_
"""

t = ()

type(t)

t1 = (1, 2, 3, 4, 45, 45.45, 45+7j, "sudh", True)

type(t1)

l = [1,2,3,4]

type(l)

t1

t1[0]

t1[7]

t1[::-1]

t1 = t1[::-1]

t1

t1[0:3]

t1.count(4)

t1.count("abc")

t1.index(1)

t1.index("sudh")

t1

t1.count(True)

t1.count(1)

t1

l

t1[0]

#Tuple are basically follows immutability concepts where it is not going to allow to change any element at a particular index

#t1[0] = 345

l[0]

l[0] = 100

l

t1

for i in t1 :
  print(i,type(i))

t2 = (1,2,3,3,4)

t2

t2 * 3

max(t2)

min(t2)

t1 = (1,2,32,4)
t2 = (4,5,6,7,8)

t3 = (t1,t2)

t3

t4 = ((1,2,3,4,5), [1,3,5,6,7,8])

t4

del t4

t1

len(t1)

t1

"sudh" in t1

2 in t1

"""sets"""

s = {}
type(s)

s1 = {1,2,3,4,5}

type(s1)

s2 = {1,1,12,3,3,3,4,5,5,5,55,523,34,3,45,6,67}

s2

l = list(s2)

tuple(s2)

l

set(l)

#s4 = {1, 2, 3, 4, [1,2,3,4]}

s5 = {1,2,3,4,(1,2,3,4)}

s5

s6 = {"sudh", "Sudh", 2,3,4,5}

s6

s7 = {"sudh", "sudh",2,3,4,5}

s7

#s7[0]

#s7[::-1]

s7

for i in s7:
  print(i)

s7.add(34)

s7

s7.add(2)

s7

len(s7)

s7.pop()

s7

s7.pop()

s7.pop()

s7.pop()

s7

s7.clear()

s7

s8 = {1,2,3,4}
s9 = {1,2,3,5}

s8.difference(s9)

s9.difference(s8)

d = {}

type(d)

d1 = {"name" : "sudh" ,"email_id" : "ss@gmail.com" ,"number":234324}

type(d1)

d1

d2 = {"name" : "sudh" , "name" : "sudhanshu"}

d2

d3 = {23234 : "abc"}

d3

d4 = {234.45 : "abc"}

d4

d5 = {True : "abc"}

d5

#d6 = {# : "abc"}

#d8 = {[1,2,3] :"abc"}

d9 = {(1,2,3):"abc"}

#d10 = {{1,2,3}:"abc"}

#d11 = {{"key":234} : "abc"}

d12 = {"course_name" : ["data science master","web dev","java with dsa and system design"]}

d12

d13 = {"key" : (1,2,3,4,5)}

d14 = {"key" : (1,2,3,4)}

d15 = {"key" : {"name" : "sudhanshu" , "class" : "DSM"}}

d15

d16 = {"batch_name" :["data science masters","web dev","JDS"],"start_date":(28,14,21),"mentor_name" : {"krish naik","sudhanshu kumar"}}

d16

d16["timing"] = (8,8,8)

d16

d16['batch_name']

d16['mentor_name']

type(d16['mentor_name'])

#not available
#d16["key"]

d16["name"] = "sudhanshu"

d16

d16['name'].upper()

d15

d15['key']

type(d15['key'])

d15['key']

d15['key']['class']

d15["key1"] = "abc"

d15

del d15['key1']

d15

d15.clear()

d15

len(d16)

d16

d16.keys()

d16.values()

list(d16.values())

list(d16.keys())

d16.items()

list(d16.items())

d16

d17 = d16.copy()

d17

del d16['name']

d16

d18 = d16

d17

d18

d18

d16.pop("timing")

d16

d.fromkeys((1,2,3),("a","b","c"))

d19 = {"key1" : "value" , "key2" : "value2"}
d20 = {"key3" : "value3" , "key4" : "value4"}

(d19,d20)

d19.update(d20)

d19

d20

d20.update(d19)

d20

d20.get("sudh")

d20.get("key3")

d20["key3"]

#d20["sudh"]

{i : i**2 for i in range(1,11)}

list(range(1,11))

{i : i+10 for i in range(1,11)}

import math
d21 = {i :math.log10(i) for i in range(1,11)}

d16

"batch_name" in d16

d21

d21.keys()

for i in d21.keys():
    if i % 2 == 0 :
        print(d21[i])

