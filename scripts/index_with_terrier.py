from time import time
import pandas as pd
import numpy as np
import os
import pyterrier as pt
pt.init()

def cast2022_generate():
    file = '/data4/guidorocchietti/treccast_2022/passages/passages.csv'
    with open(file, 'r') as corpusfile:
        corpusfile.read()
        for l in corpusfile:
            docno, passage = l.split("\t")
            yield {'docno' : docno, 'text' : passage}

iter_indexer = pt.IterDictIndexer("./passage_index")
indexref = iter_indexer.index(cast2022_generate(), meta={'docno' : 50, 'text': 4096})