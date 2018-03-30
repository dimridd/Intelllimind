#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 01:40:02 2018

@author: divyanshu
"""

#%%

#Named-Entiny-Recognition
import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()

n = int(input("Enter Number Of Documents: "))
#from nltk.corpus import stopwords
files = []   
for inputs in range(n):
    doc = input()
    files.append(doc)    

for inputs in range(n):  
    with open(files[inputs], 'r') as f:
        contents = f.read().split()
    
    for item in contents:
        doc=nlp(item)
        for ent in doc.ents:
            print(ent.text,'/',ent.label_)
            
    print("\n")
    
#%%