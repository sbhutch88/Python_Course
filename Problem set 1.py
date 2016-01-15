

#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print: 5
s = 'vynmclttgbmrxauc'


'''
counter = 0
vowels = 'aeiou'

for x in list(s):
    if  x in vowels:
        counter = counter + 1
    else:
        counter = counter
        
print 'Number of vowels: ' + str(counter)
'''

'''
counter = 0
found = 0

for i in list(s):
    if counter == len(s)-2: 
        break
    if i == 'b':
        if s[counter+1] == 'o' and s[counter+2] == 'b':
            found += 1
    counter += 1
print 'Number of times bob occurs is: '+ str(found)
'''        
        
alph = 'abcdefghijklmnopqrstuvwxyz'        
counter = 0
found = 0
bi = [0]*len(s)
counter2 = 0
inarow = [0]*len(s)
alphNum = [0]*len(s)


for i in list(s):
    alphNum[counter] = alph.index(i) #This should find where in the alphabet the current letter is
    if counter == len(s)-1:
        break
    counter += 1
#print alphNum

counter = 1
for i in alphNum[1:len(s)]:
    #print alphNum[counter-1]
    #print 'i' + str(i)
    if alphNum[counter-1] <= i:
        bi[counter] = 1
    counter += 1
#print bi
counter = 0
for i in bi:
    if i == 1:
        counter2 += 1
        inarow.insert(counter,counter2)
        counter += 1
    elif i == 0:
        counter += 1
        counter2 = 0 #restart counter

longest = inarow.index(max(inarow))

print 'Longest substring in alphabetical order is: '+ str(s[(longest)-max(inarow):longest+1])
