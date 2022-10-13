#!/usr/bin/env python3

import sys

fav_things = {"song" : "I remember", "color" : "purple", "tree" : "Aspen"}
#print(fav_things)
#print(fav_things["color"])
#print(fav_things["tree"])

fav_things2 = {"organism" : 'sea slug'}
fav_things.update(fav_things2)
#print(fav_things)
print('List of keys')
#print(fav_things["color"])
#print(fav_things.keys())

#using input from cl to call keys in dic
print('Choose one or die')
for things in fav_things: 
	print(things)
	print
dic_call = input()
print(fav_things[dic_call])
#input to change fav organism
print('Choose a new organism or die')
organism_new = input()
fav_things["organism"] = organism_new
print(fav_things.items())

