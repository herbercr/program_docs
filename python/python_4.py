#!/usr/bin/env 
#lists and loops

fav_things = ['octopus', 'music', 'mountains', 'chemistry', 'sleeping']
#print(fav_things)
#print(fav_things[2])
fav_things.insert(2,'hills')
fav_things.pop(3)
#print(fav_things)
fav_things.append('drinking')
#print(fav_things)
fav_things.insert(0,'las vegas')
#print(fav_things)
fav_things.pop()
#print(fav_things)
fav_things.remove('las vegas')
#print(fav_things)

#splitting strings
taxa = ['sapiens', 'erectus', 'neanderthalensis']
#print(taxa)
#print(taxa[1])
#print(type(taxa))
species,species2,species3 = taxa[:1],taxa[1:2],taxa[2:]
#print(species, species2, species3)
#print(species[1])
print(type(species))
print(sorted(taxa))
print(sorted(taxa, key = len))

 
#while loops
count = 0
while count < 101:
	print('count:', count)
	count+=1
	if count == 101:
		break
#print('Done')


exp_list = [10 ** x for x in range(4)]
#print(exp_list)

for x in (101,2,15,22,95,33,2,27,72,15,52):
	if x % 2 == 0: 
		print(x)

newlist = [101,2,15,22,95,33,2,27,72,15,52]
sorted_list = sorted(newlist)
#print(sorted_list)

evens = []
odds = []
for i in sorted_list:
	if i % 2 == 0: 
		evens.append(i)
	if i % 2:
		odds.append(i)
print(evens)
print(odds)
print(sum(evens))
print(sum(odds))

for x in sorted_list:
	if x in range(100):
		print(x)	

range_list = [range(100) for x in sorted_list]
	
