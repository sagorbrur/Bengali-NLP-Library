# Dependencies
# pip install wiki-dump-reader
# pip install tqdm

from wiki_dump_reader import Cleaner, iterate
from tqdm import tqdm
import re

cleaner = Cleaner()
output = open('bn_wiki.txt', 'w')
for title, text in tqdm(iterate('bnwiki-latest-pages-articles.xml')):
    text = cleaner.clean_text(text)
    cleaned_text, _ = cleaner.build_links(text)
    cleaned_text = re.sub(r'[A-Za-z]', '', cleaned_text)
#     print(cleaned_text)
    output.write(cleaned_text+"\n")
    
output.close()
