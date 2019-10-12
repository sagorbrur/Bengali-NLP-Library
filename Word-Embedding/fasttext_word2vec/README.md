# Fasttext Bengali(Converting bengali text into vector)

# Dependencies

* Python 2.7

# Installing Fasttext

```
$ git clone https://github.com/facebookresearch/fastText.git
$ cd fastText
$ make
```

## Testing

```py
python
>>> import fastText
>>>
```

# Pre-train Model Download

* [Bengali .bin Model](https://fasttext.cc/docs/en/crawl-vectors.html)
* [Bengali .vec File](https://fasttext.cc/docs/en/crawl-vectors.html)

# Training 

```$ ./fasttext skipgram -input data.txt -output model```

# Obtaining word vectors

Print word vectors for a text file `queries.txt` containing words.

```$ ./fasttext print-word-vectors model.bin < queries.txt```

