from gensim.models.fasttext import FastText as FT_gensim
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import os

corpus_file = datapath('/Users/hanjaewon/폴더모음/학교생활/졸업과제/fasttextTest/merged.txt')
model = FT_gensim(size=64)
model.build_vocab(corpus_file=corpus_file)

model.train(
    corpus_file=corpus_file, epochs=model.epochs,
    total_examples=model.corpus_count, total_words=model.corpus_total_words
)

model.save("model3")
