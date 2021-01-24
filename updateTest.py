from gensim.models.fasttext import FastText as FT_gensim
from gensim.test.utils import datapath
import numpy as np
#from gensim.models.fasttext import FastText, load_facebook_vectors 이 부분 잘 살펴보면 update할 수 있을 지도

cap_path = datapath('/Users/hanjaewon/폴더모음/학교생활/졸업과제/fasttextTest/model_report')
model = FT_gensim.load(cap_path)
corpus_file = datapath('/Users/hanjaewon/폴더모음/학교생활/졸업과제/fasttextTest/new.txt')
#model.build_vocab(sentences=common_texts)
#model.build_vocab(sentences=text)
#model.train(sentences=text, total_examples=len(text), epochs=model.epochs)
print('채스가 vocab안에 있는가?')
print('채스' in model.wv.vocab)
print(model.corpus_count)
#print('채스의 vector는?')
#print(model.wv.__getitem__('채스'))
model.build_vocab(corpus_file=corpus_file, update=True)
model.train(
    corpus_file=corpus_file, epochs=model.epochs,
    total_examples=model.corpus_count, total_words=model.corpus_total_words
)
print('----------업데이트 이후----------')
print('채스가 vocab안에 있는가?')
print('채스' in model.wv.vocab)
print(model.corpus_count)
#print('채스의 vector는?')
#print(model.wv.__getitem__('채스'))

#old_vector = np.copy(model.wv['computation'])
#new_sentences = [
#     ['computer', 'aided', 'design'],
#     ['computer', 'science'],
#     ['computational', 'complexity'],
#     ['military', 'supercomputer'],
#     ['central', 'processing', 'unit'],
#     ['onboard', 'car', 'computer'],
#]
#model.build_vocab(new_sentences, update=True)
#model.train(new_sentences, total_examples=len(new_sentences), epochs=model.epochs)
#new_vector = np.copy(model.wv['computation'])
#
#print(np.allclose(old_vector, new_vector))
#print('computation' in model.wv.vocab)
#print('computation' in model.wv)
