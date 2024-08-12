#!/usr/bin/env python3
import collections
import pickle

def getdb():
    try:
        with open('seedmap.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        pass
    return {}

db = getdb()
sdb = collections.OrderedDict(sorted(db.items()))
totals = {}
for key, value in sdb.items():
    if value not in totals:
        totals[value] = 1
    else:
        totals[value] += 1
print("total seeds: "+str(len(sdb)))
print(totals)
