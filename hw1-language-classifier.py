#!/usr/bin/env python

import numpy as np
import string


# Read the language statistics

def readLangStats( filename ):
    # first version
    peng = np.zeros( 26, dtype = float )
    i = 0
    for line in open( filename ):
        dum = line.split( ' ' )
        pdum = float( dum[ 2 ] )/1000.
        peng[ i ] = pdum
        i = i+1
    #second and simpler version
    pengi = []

    for line in open( filename ):
        dum = line.split( ' ' )
        pdum = float( dum[ 2 ] )/1000.
        pengi.append( pdum )

    peng = np.array( pengi )
    return peng

def normalize( vec):
    svec = sum( vec )
    vec = vec / svec
    return None  #optional


# main 

peng = readLangStats( 'english-1.dat' )
pger = readLangStats( 'german-1.dat' )
pfr = readLangStats( 'french-1.dat' )
psp = readLangStats( 'spanish-1.dat' )

alphabet = 'abcdefghijklmnopqrstuvwxyz'
nletters = len(alphabet)
languages = ['English', 'German ', 'Spanish', 'French ' ] #space added to make them all equal length

while True:
    sentence = input('Enter a sentence:' )

    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    translator = str.maketrans('', '', string.punctuation)
    sentence = sentence.translate(translator)

    letter_counts = {}
    for ch in sentence:
        if ch in letter_counts:
            letter_counts[ch] += 1
        else:
            letter_counts[ch] = 1        

    ll = {}
    ll['English'] = 0
    ll['German'] = 0
    ll['French'] = 0
    ll['Spanish'] = 0
    for ch in letter_counts.keys():
        ll['English'] = ll['English'] + (letter_counts[ch] * np.log2(peng[ord(ch) - 97]/1000))
        ll['German'] = ll['German'] + (letter_counts[ch] * np.log2(pger[ord(ch) - 97]/1000))
        ll['French'] = ll['French'] + (letter_counts[ch] * np.log2(pfr[ord(ch) - 97]/1000))
        ll['Spanish'] = ll['Spanish'] + (letter_counts[ch] * np.log2(psp[ord(ch) - 97]/1000))

    # print results
    print ('Log-likelihoods (in bits)')
    for z in ll.keys():
        print (z + " Log-likelihood: " + str(ll[z]))
    ilang = max(ll, key = ll.get)
    print ('The most likely language of %s is %s' %(sentence, str(ilang)))

    
    




