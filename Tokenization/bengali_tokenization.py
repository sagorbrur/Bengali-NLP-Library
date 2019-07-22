# bengali tokenization using nltk. It's not perfect but works good.

from nltk.tokenize import word_tokenize
import re
from string import punctuation

sentence = "১.২ টাকা নিয়ে রাস্তায় নামলাম। রাজপণ্ডিত হব মনে আশা করে। সপ্তশ্লোক ভেটিলাম রাজা গৌড়েশ্বরে। শত কষ্টে রাজা একদিন হারিয়ে গেলেন কে ফেরাবে তাকে! শত চেষ্টাতেও রাণী তাকে ফেরাতে পারলেন না।"
input_text = re.sub(r'[ঃ।]', ' ', sentence)

tokens = word_tokenize(input_text)



new_token = []
for tk in tokens:
    if tk not in punctuation:
        new_token.append(tk)
        
print(new_token)

"""
['১.২', 'টাকা', 'নিয়ে', 'রাস্তায়', 'নামলাম', 'রাজপণ্ডিত', 'হব', 'মনে', 'আশা', 'করে', 'সপ্তশ্লোক', 
'ভেটিলাম', 'রাজা', 'গৌড়েশ্বরে', 'শত', 'কষ্টে', 'রাজা',
'একদিন', 'হারিয়ে', 'গেলেন', 'কে', 'ফেরাবে', 'তাকে', 'শত',
'চেষ্টাতেও', 'রাণী', 'তাকে', 'ফেরাতে', 'পারলেন', 'না']
"""
