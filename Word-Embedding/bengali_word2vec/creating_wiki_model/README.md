# Creating bengali word2vec model from wiki dump data

# Dependencies
* python 2.7(for training)
* python 3(for wikidata process)


# Downloading

* [Bengali Wiki Dump](https://dumps.wikimedia.org/bnwiki/latest/bnwiki-latest-pages-articles.xml.bz2)

# Processing Wiki-Data(python 3)
Follow [**THIS**](https://github.com/sagorbrur/bn_wikiextractor) repo to process wiki bengali data.

# Training(python 2)

* Rename `wiki.bn.text` to `wiki.bn.text.seg`
* run ```python train_word2vec_model.py wiki.bn.text.seg wiki.bn.text.model wiki.bn.text.vector```

