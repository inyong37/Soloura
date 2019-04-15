Amino_Acid_Table = {
    'X': [0, 0, 0, 0, 0],
    'A': [0, 0, 0, 0, 1],
    'C': [0, 0, 0, 1, 0],
    'D': [0, 0, 0, 1, 1],
    'E': [0, 0, 1, 0, 0],
    'F': [0, 0, 1, 0, 1],
    'G': [0, 0, 1, 1, 0],
    'H': [0, 0, 1, 1, 1],
    'I': [0, 1, 0, 0, 0],
    'K': [0, 1, 0, 0, 1],
    'L': [0, 1, 0, 1, 0],
    'M': [0, 1, 0, 1, 1],
    'N': [0, 1, 1, 0, 0],
    'P': [0, 1, 1, 0, 1],
    'Q': [0, 1, 1, 1, 0],
    'R': [0, 1, 1, 1, 1],
    'S': [1, 0, 0, 0, 0],
    'T': [1, 0, 0, 0, 1],
    'V': [1, 0, 0, 1, 0],
    'W': [1, 0, 0, 1, 1],
    'Y': [1, 0, 1, 0, 0]
}

def Convert_Protein_to_Binary(Amino_Acid):
    if not Amino_Acid in Amino_Acid_Table:
        return None
    return Amino_Acid_Table[Amino_Acid]

def Convert_Sequence_to_Vector(Sequence):
    binary_vector = [Convert_Protein_to_Binary(amino_acid) for amino_acid in Sequence]
    if None in binary_vector:
        return None
    return binary_vector

def Split_NGram(sequence):
    amino_acid = zip(*[iter(sequence)])
    str_ngrams = []
    for ngrams in amino_acid:
        str_ngrams.append(''.join(ngrams))
    return str_ngrams

def Amino_Acid_to_Vector(Sequence):
    vector = []
    for i in range(0, len(Sequence)):
        vector[i] = Amino_Acid_Table[Sequence[i]]
    return vector

'''
def Sequences_to_Vectors(Sequences):
    vectors = [[0 for cols in range(m)]]
    for i in range(0, len(Sequences)):
        for j in range(0, len(Sequences[i])):
            vector = Amino_Acid_Table[Sequences[i][j]]
            vectors[i][j] = vectors[i][j].ljust(1, vector)
    return vectors
'''
