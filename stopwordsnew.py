#!/usr/bin/env python

"""
A filter that remove stopwords.
"""

import fileinput


def process(line):
    """For each line of input, replace stopwords with " "."""
    stopwords=[" a "," able ", " about ", " across ", " after ", " all ", " almost ", " also ", " am ", " among ", " an ", " and ", " any ", " are ", " as ", " at ", " be ", " because ", " been ", " but ", " by ", " can ", " cannot ", " could ", " dear ", " did ", " do ", " does ", " either ", " else ", " ever ", " every ", " for ", " from ", " get ", " got ", " had ", " has ", " have ", " he ", " her ", " hers ", " him ", " his ", " how ", " however ", " i ", " if ", " in ", " into ", " is ", " it ", " its ", " just ", " least ", " let ", " like ", " likely ", " may ", " me ", " might ", " most ", " must ", " my ", " neither ", " no ", " nor ", " not ", " of ", " off ", " often ", " on ", " only ", " or ", " other ", " our ", " own ", " rather ", " said ", " say ", " says ", " she ", " should ", " since ", " so ", " some ", " than ", " that ", " the ", " their ", " them ", " then ", " there ", " these ", " they ", " this ", " tis ", " to ", " too ", " twas ", " us ", " wants ", " was ", " we ", " were ", " what ", " when ", " where ", " which ", " while ", " who ", " whom ", " why ", " will ", " with ", " would ", " yet ", " you ", " your "]
    line=line.lower()
    line=line.strip()
    line=" "+line+" "
    for i in stopwords:
	line = line.replace(i," ")
	i = i.strip()
	i1 = " "+i+","
	i2 = " "+i+"."
	i3 = " "+i+":"
	i4 = " "+i+";"
        i5 = " "+i+'"'
        i6 = '"'+i+" "
	line = line.replace(i1," ")
	line = line.replace(i2," ")
	line = line.replace(i3," ")
	line = line.replace(i4," ")
        line = line.replace(i5," ")
        line = line.replace(i6," ")
    print(line)


for line in fileinput.input():
    process(line)
