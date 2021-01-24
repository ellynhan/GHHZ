from gensim.models.fasttext import FastText as FT_gensim
from gensim.test.utils import datapath

#from gensim.models.fasttext import FastText, load_facebook_vectors 이 부분 잘 살펴보면 update할 수 있을 지도

cap_path = datapath('/Users/hanjaewon/폴더모음/학교생활/졸업과제/fasttextTest/model3')
model = FT_gensim.load(cap_path)
#
#arr = ['한국','서울','일본','도쿄','미국','영어','원','엔','달러','남자','여자','남성','여성','개','강아지','소','송아지','고양이','사과','병아리','범','호랑이','앞','뒤','대형','소형','사람','명','마리','밥','진지','병','나','저','아버지','아비','주다']
#
#
##for word in arr:
##    print(word+": "+str(word in model.wv.vocab))
#
#
##print('서울이 vocab안에 있는가?')
##print('서울' in model.wv.vocab)
##print("서울과 유사도가 높은 단어:")
##for v in model.wv.most_similar("서울"):
##    print(v)
#
#
#print(model.wv.__getitem__('한국')-model.wv.__getitem__('서울'))
#print(model.wv.__getitem__('일본')-model.wv.__getitem__('도쿄'))
#print(model.wv.__getitem__('한국')-model.wv.__getitem__('원'))
#print(model.wv.__getitem__('일본')-model.wv.__getitem__('엔'))
#print(model.wv.__getitem__('남자')-model.wv.__getitem__('남성'))
#print(model.wv.__getitem__('여자')-model.wv.__getitem__('여성'))
#print(model.wv.__getitem__('개')-model.wv.__getitem__('강아지'))
#print(model.wv.__getitem__('소')-model.wv.__getitem__('송아지'))

print(model.wv.vocab)


