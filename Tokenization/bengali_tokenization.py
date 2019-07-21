# Bengali Tokenization using python and regular expression

import re

sentence = "রাজপণ্ডিত হব মনে আশা করে। সপ্তশ্লোক ভেটিলাম রাজা গৌড়েশ্বরে। শত কষ্টে রাজা একদিন হারিয়ে গেলেন...... কে ফেরাবে তাকে! শত চেষ্টাতেও রাণী তাকে ফেরাতে পারলেন না।"

input_text = re.sub(r'[,.:@#?!&$।]', ' ', sentence)
# print(input_text)
tokens = input_text.split()
print(tokens)
