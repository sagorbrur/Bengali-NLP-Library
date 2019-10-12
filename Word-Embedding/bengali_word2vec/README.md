# Bengali Word2Vec Generator

# Dependencies

* Python 2
* Gensim

# Steps

* Rename your text file into .txt to .seg
* Run the below command

```
$python train_word2vec.py input_file.txt.seg wiki.bn.text.model output_file.vector

```
Here `wiki.bn.text.model` is a pretrain bengali word2vec model on wikidata

To create `wiki.bn.text.model` follow this [instruction](https://github.com/sagorbrur/Bengali-NLP-Library/tree/master/Word-Embedding/bengali_word2vec/creating_wiki_model)

