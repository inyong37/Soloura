# Functions & Packages
#### zip [Reference (Korean)](https://wikidocs.net/32#zip)
##### Example
```
>>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]

>>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
```

#### from pyfasta import Fasta [Reference](https://github.com/brentp/pyfasta/)
##### Example
```
>>> from pyfasta import Fasta
>>> f = Fasta('tests/data/three_chrs.fasta')
>>> sorted(f.keys())
['chr1', 'chr2', 'chr3']

>>> f['chr1']
NpyFastaRecord(0..80)
```

#### 'has_key' and 'in' [Reference (stackoverflow)](https://stackoverflow.com/questions/1323410/should-i-use-has-key-or-in-on-python-dicts)
'has_key' is for python 2.x and 'in' is for python 3.x.
##### Example 'has_key'
```
def convert_amino_to_binary(amino):
    if not AMINO_ACID_BINARY_TABLE.has_key(amino):
        return None
    return AMINO_ACID_BINARY_TABLE[amino]
```
##### Example 'in'
```
def Convert_Protein_to_Binary(Protein):
    if not Protein in Protein_Binary_Table:
        return None
    return Protein_Binary_Table[Protein]
```
#### tqdm [Reference (Source)](https://github.com/tqdm/tqdm)

#### nltk [pip](https://pypi.org/project/nltk/)
```
pip install nltk
```
