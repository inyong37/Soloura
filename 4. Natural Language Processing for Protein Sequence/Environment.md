# Functions & Packages
### ZIP [Korean Blog](https://wikidocs.net/32#zip)
#### Example
```
>>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]

>>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
```
### from pyfasta import Fasta [Github](https://github.com/brentp/pyfasta/)
#### Example
```
>>> from pyfasta import Fasta
>>> f = Fasta('tests/data/three_chrs.fasta')
>>> sorted(f.keys())
['chr1', 'chr2', 'chr3']

>>> f['chr1']
NpyFastaRecord(0..80)
```

### 'has_key' and 'in' [stackoverflow](https://stackoverflow.com/questions/1323410/should-i-use-has-key-or-in-on-python-dicts)
'has_key' is for python 2.x and 'in' is for python 3.x.
#### Example 'has_key'
```
def convert_amino_to_binary(amino):
    if not AMINO_ACID_BINARY_TABLE.has_key(amino):
        return None
    return AMINO_ACID_BINARY_TABLE[amino]
```
#### Example 'in'
```
def Convert_Protein_to_Binary(Protein):
    if not Protein in Protein_Binary_Table:
        return None
    return Protein_Binary_Table[Protein]
```
### TQDM [Github](https://github.com/tqdm/tqdm)

### NLTK(The Natural Language Toolkit) [pip](https://pypi.org/project/nltk/)
Python 2.7, 3.4, 3.5, 3.6, or 3.7.
```
pip install nltk
```
### KoNLPy [Reference](http://konlpy.org/ko/v0.4.3/)
KoNLPy is a Python package for Korean natural language processing.

### How to deal with varying input size [ai.stackexchange](https://ai.stackexchange.com/questions/2008/how-can-neural-networks-deal-with-varying-input-sizes)

### Word2Vec [Korean Blog](https://shuuki4.wordpress.com/2016/01/27/word2vec-%EA%B4%80%EB%A0%A8-%EC%9D%B4%EB%A1%A0-%EC%A0%95%EB%A6%AC/)
[Code with detailed explaination, Korean](https://pythonkim.tistory.com/93)
[Code with Keras, Korean](https://byeongkijeong.github.io/Word2vec-from-scratch-using-keras/)
[Code with Tensorflow, Korean](https://github.com/golbin/TensorFlow-Tutorials/blob/master/04%20-%20Neural%20Network%20Basic/03%20-%20Word2Vec.py)
