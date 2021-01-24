from os import listdir
textFile = open("ko_questions_words.txt","a")

countries = ['한국','일본','중국','미국','영국','프랑스','베트남']
currencies = ['원','엔','위안','달러','유로','유로','동']
#provinces = ['경기도','강원도','충청도','전라도','경상도']
#cities = []
men = ['남자','남성','아저씨','아빠','오빠','손자','형제','형','삼촌','큰아버지']
women = ['여자','여성','아줌마','엄마','언니','손녀','자매','누나','이모','고모']
animals = ['개','소','닭']
young_animals = ['강아지','송아지','병아리']
nouns = ['사람','개','나무','종이']
unit = ['명','마리','그루','장']
nouns2 = ['앞','대형','위','오른']
antonyms = ['뒤','소형','아래','왼']

sectionTitle = ['countries & currencies', 'men & women', 'animals and their young','noun antonyms','unit bound nouns']
textFile.write(": "+sectionTitle[1]+"\n")
len = len(men);
for i in range(len):
    for j in range(len):
        text = men[i]+" "+women[i]+" "+men[(j+1)%len]+" "+women[(j+1)%len]+"\n"
        if i!=(j+1)%len :
            textFile.write(text)
textFile.close()
