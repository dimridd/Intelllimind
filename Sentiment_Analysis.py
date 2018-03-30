#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:12:17 2018

@author: divyanshu
"""

#%%
#Sentiment Analysis
import re
from string import punctuation
from nltk.corpus import stopwords

# RAW string : 
#print(r'\tTab')

lst = []
text = """
Neural words are words with objectivity equal to 0 i.e.,
if positive score and negative score is zero.

if negative score and positive score are equal to 0.5 than
our objectivity is zero we also refer to them as neural, 
As the dirct consequences of thse values for the positive
and negative score, the objectivity score of these word is
zero, despite there "neural" label.
We will name them as half positive and half Negative words.

We also have weak positive and weak negative words for them
the value of objective score varies from 0.166 to 0.98
"""
#pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")

#matches = pattern.finditer(text)

#for match in matches:
#    print(match)

Useless_pattern_lst1 = re.compile(r"[0-9]")
Useless_pattern_lst2 = re.compile(r"\W")
Useless_pattern_lst3 = re.compile(r"([a-z]+.)+")
stop_words = set(stopwords.words('english'))

Scores_of_Doc = []

n = int(input("Enter Number Of Documents: "))

inputs = []
for i in range(n): # loop 3 times
	inputs.append(input())

for i in range(len(inputs)):       
    with open(inputs[i], 'r') as f:
        contents = f.read().split()

    open('filteredtext.txt','w')

    for r in contents:
        if not r in stop_words:
            appendFile = open('filteredtext.txt','a')
            appendFile.write(" "+r)
            appendFile.close()
    
    
    with open('filteredtext.txt', 'r') as f:
        contents = f.read().split()
        
    lst = []
    lst1 = []
    
    for i in contents:
        i = i.replace(",","")
        i = i.replace('"',"")
        i = i.replace("'","")
        lst1.append(i)
    
    for i in lst1:
        if Useless_pattern_lst1.search(i) or Useless_pattern_lst2.search(i) :
            lst.append(i)
            #print(i)
    
    extra_words = []
    for word in lst:
        count = 0
        for value in word:
            count = count + 1
            if value == punctuation[12]:
                lst1.append(word[0:count-1])
                extra_words.append(word[0:count-1])
                count = 0
                break
        
    def Diff(li1, li2):
        #return [i for i in li1 + li2 if i not in li1 or i not in li2]
        return (list(set(li1) - set(li2)))
    
    #Example
    #contents = [10, 15, 20, 25, 30, 35, 40, 40]
    #lst = [25, 40, 35]
        
    
    contents = (Diff(lst1, lst)) + extra_words
    
    from nltk.corpus import sentiwordnet as swn
    #nltk.download()
    #Objectivity = 1 - (Positive + Negative)
    
    contents = list((set(contents)))
    
    a = []
   
    
    positivity = negitivity = objectivity = 0
    length = 0
    
    for word in contents: 
        word0 = swn.senti_synsets(word)
        word1 = list(word0)
        if len(word1) == 0:
            contents.remove(word)
        else:   
            positivity = positivity + word1[0].pos_score() 
            negitivity = negitivity + word1[0].neg_score()
            objectivity = objectivity + word1[0].obj_score()
            
            length = length + 1
            #a.append(word1[0].pos_score())
            #a.append(word1[0].neg_score())
            #a.append(word1[0].obj_score())
            #b.append(a)
        #a = []
        
    
    a.append(positivity/length)
    a.append(negitivity/length)
    a.append(objectivity/length)
    
    
    contents = []  
    Scores_of_Doc.append(a)
       
pos_doc = 0
neg_doc = 0

for doc in Scores_of_Doc:
    if doc[0] > doc[1]:
        pos_doc = pos_doc + 1
    else:
        neg_doc = neg_doc + 1
    
print("Number of Positive Documents are: ", pos_doc,"\n")
print("Number of Negative Documents are: ", neg_doc)    
#%%