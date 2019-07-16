from io import open
from HyperDoc2Vec import *
import numpy

import logging

def test():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    dataset='mag'
    train_file='./input/mag_training_data.txt'
    model_file='./models/magcsenglish_window20.model'
    documents=TaggedLineHyperDocument(train_file, False)
    model = HyperDoc2Vec(documents,iter=5, workers=8, anchor_iter=100, anchor_window=20, anchor_negative=1000, anchor_alpha=0.025, size=300)
    model.save(model_file)

    model=HyperDoc2Vec.load(model_file)
    print(model)

if __name__ == '__main__':
	test()