# Functions
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
