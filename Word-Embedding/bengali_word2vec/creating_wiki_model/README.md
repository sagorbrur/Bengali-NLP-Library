# Creating bengali word2vec model from wiki dump data

# Dependencies
* python 2.7(for training)
* python 3(for wikidata process)


# Downloading

* [Bengali Wiki Dump](https://dumps.wikimedia.org/bnwiki/latest/bnwiki-latest-pages-articles.xml.bz2)

# Processing Wiki-Data(python 3)

```python wiki_dump.py bnwiki-latest-pages-articles.xml.bz2 wiki.bn.text```

# Training(python 2)

* Rename `wiki.bn.text` to `wiki.bn.text.seg`
* run ```python train_word2vec_model.py wiki.bn.text.seg wiki.bn.text.model wiki.bn.text.vector```

