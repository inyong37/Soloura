# Changed 'R', 'S', 'T', 'V', 'W', 'Y' to all minus 1.
Protein_Binary_Table = {
    'A': [0, 0, 0, 0, 0],
    'C': [0, 0, 0, 0, 1],
    'D': [0, 0, 0, 1, 0],
    'E': [0, 0, 0, 1, 1],
    'F': [0, 0, 1, 0, 0],
    'G': [0, 0, 1, 0, 1],
    'H': [0, 0, 1, 1, 0],
    'I': [0, 0, 1, 1, 1],
    'K': [0, 1, 0, 0, 0],
    'L': [0, 1, 0, 0, 1],
    'M': [0, 1, 0, 1, 0],
    'N': [0, 1, 0, 1, 1],
    'P': [0, 1, 1, 0, 0],
    'Q': [0, 1, 1, 0, 1],
    'R': [0, 1, 1, 1, 0],
    'S': [0, 1, 1, 1, 1],
    'T': [1, 0, 0, 0, 0],
    'V': [1, 0, 0, 0, 1],
    'W': [1, 0, 0, 1, 0],
    'Y': [1, 0, 0, 1, 1]
}

# Changed 'has_key' to 'in'.
def Convert_Protein_to_Binary(Protein):
    if not Protein in Protein_Binary_Table:
        return None
    return Protein_Binary_Table[Protein]

def Convert_Sequence_to_Vector(Sequence):
    binary_vector = [Convert_Protein_to_Binary(Protein) for Protein in Sequence]
    if None in binary_vector:
        return None
    return binary_vector

from gensim.models import word2vec
from pyfasta import Fasta
from tqdm import tqdm
import sys

def Split_NGram(Sequence, N):
    a, b, c = zip(*[iter(Sequence)] * N), zip(*[iter(Sequence[1:])] * N), zip(*[iter(Sequence[2:])] * N)
    str_ngrams = []
    for ngrams in [a, b, c]:
        x = []
        for ngram in ngrams:
            x.append("".join(ngram))
        str_ngrams.append(x)
    return str_ngrams

def Generate_Corpus_File(Fasta_File_Name, N, Corpus_File_Name):
    file = open(Corpus_File_Name, "w")
    fasta = Fasta(Fasta_File_Name)
    for record_id in tqdm(fasta.keys(), desc='Corpus Generation Progress'):
        r = fasta[record_id]
        sequence = str(r)
        ngram_patterns = Split_NGram(Sequence=sequence, N=n)
        for ngram_pattern in ngram_patterns:
            file.write(" ".join(ngram_pattern) + "\n")
    file.close()

def Load_ProtVec(Model_File_Name):
    return word2vec.Word2Vec.load(Model_File_Name)

class ProtVec(word2vec.Word2Vec):

    def __init__(self, Fasta_File_Name=None, Corpus=None, N=3, Size=100, Corpus_File_Name="Corpus.txt", SG=1, Window=25, Min_Count=1, Workers=3):
        self.N = N
        self.Size = Size
        self.Fast_File_Name = Fasta_File_Name

        if Corpus is None and Fasta_File_Name is None:
            raise Exception("Either Fasta_File_Name or Corpus is needed!")

        if Fasta_File_Name is not None:
            print("Generate corpus file from fasta file...")
            Generate_Corpus_File(Fasta_File_Name=Fasta_File_Name, N=N, Corpus_File_Name=Corpus_File_Name)
            corpus = word2vec.Text8Corpus(Corpus_File_Name)

        word2vec.Word2Vec.__init__(self, corpus, size=Size, sg=SG, window=Window, min_count=Min_Count, workers=Workers)

    def To_Vectors(self, Sequence):
        ngram_patterns = Split_NGram(Sequence, self.N)
        protvecs = []
        for ngrams in ngram_patterns:
            ngrams_vecs = []
            for ngram in ngrams:
                try:
                    ngrams_vecs.append(self[ngram])
                except:
                    raise Exception("Model has never trained this n-gram: " + ngram)
            protvecs.append(sum(ngrams_vecs))
        return protvecs
