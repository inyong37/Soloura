import pandas as pd
from gensim.models import Word2Vec

values = [
['ARTVVLITGCSSGIGLHLAVRLASDPSQSFKVYATLRDLKTQGRLWEAARALACPPGSLETLQLDVRDSKSVAAARERVTLTALRAPKPTLRYFTTERFLPLLRMRLDDPSGSNYVTAMHREVFGDVPA',1 ],
['MAPAEILNGKEISAQIRARLKNQVTQLKEQVPGFTPRLAILQVGNRDDSNLYINVKLKAAEEIGIKATHIKLPRTTTESEVPDDKKPNGRKVVGDVAYDEAKERASFITPVPGGVGPMTVAMLMQSTVESAKRFLEKFKPG', 1],
['ASRLLLNNGAKMPILGLGTWKSPPGQVTEAVKVAIDVGYRHIDCAHVYQNENEVGVAIQEKLREQVVKREELFIVSKLWCNKTTAQVLIRFPMQRNLVVIPKSVTPERIAENFKVFDFELSSQDMTTLLSYNRNWRVSALLSCTSHKDYPFHEEF', 1],
['ASRLLLNNGAKMPILGLGTWKSPPGQVTEAVKVAIDVGYRHIDCAHVYQNENEVGVAIQEKLREQVVKREELFIVSKLWCNKTTAQVLIRFPMQRNLVVIPKSVTPERIAENFKVFDFELSSQDMTTLLSYNRNWRVCALLSCTSHKDYPFHEEF', 1]
]
columns = ['sequence', 'enzyme']
df = pd.DataFrame(values, columns=columns)
print(df)

result = [['here', 'are', 'two', 'reasons', 'companies', 'fail', 'they', 'only', 'do', 'more', 'of', 'the', 'same', 'or', 'they', 'only', 'do', 'what', 's', 'new'], ['to', 'me', 'the', 'real', 'real', 'solution', 'to', 'quality', 'growth', 'is', 'figuring', 'out', 'the', 'balance', 'between', 'two', 'activities', 'exploration', 'and', 'exploitation'], ['both', 'are', 'necessary', 'but', 'it', 'can', 'be', 'too', 'much', 'of', 'a', 'good', 'thing'], ['consider', 'facit'], ['i', 'm', 'actually', 'old', 'enough', 'to', 'remember', 'them'], ['facit', 'was', 'a', 'fantastic', 'company'], ['they', 'were', 'born', 'deep', 'in', 'the', 'swedish', 'forest', 'and', 'they', 'made', 'the', 'best', 'mechanical', 'calculators', 'in', 'the', 'world'], ['everybody', 'used', 'them'], ['and', 'what', 'did', 'facit', 'do', 'when', 'the', 'electronic', 'calculator', 'came', 'along'], ['they', 'continued', 'doing', 'exactly', 'the', 'same']]


ez = [
['A', 'R', 'T', 'V', 'V', 'L', 'I', 'T', 'G', 'C', 'S', 'S', 'G', 'I', 'G', 'L', 'H', 'L', 'A', 'V', 'R', 'L', 'A', 'S', 'D', 'P', 'S', 'Q', 'S', 'F', 'K', 'V', 'Y', 'A', 'T', 'L', 'R', 'D', 'L', 'K', 'T', 'Q', 'G', 'R', 'L', 'W', 'E', 'A', 'A', 'R', 'A', 'L', 'A', 'C', 'P', 'P', 'G', 'S', 'L', 'E', 'T', 'L', 'Q', 'L', 'D', 'V', 'R', 'D', 'S', 'K', 'S', 'V', 'A', 'A', 'A', 'R', 'E', 'R', 'V', 'T', 'L', 'T', 'A', 'L', 'R', 'A', 'P', 'K', 'P', 'T', 'L', 'R', 'Y', 'F', 'T', 'T', 'E', 'R', 'F', 'L', 'P', 'L', 'L', 'R', 'M', 'R', 'L', 'D', 'D', 'P', 'S', 'G', 'S', 'N', 'Y', 'V', 'T', 'A', 'M', 'H', 'R', 'E', 'V', 'F', 'G', 'D', 'V', 'P', 'A', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['M', 'A', 'P', 'A', 'E', 'I', 'L', 'N', 'G', 'K', 'E', 'I', 'S', 'A', 'Q', 'I', 'R', 'A', 'R', 'L', 'K', 'N', 'Q', 'V', 'T', 'Q', 'L', 'K', 'E', 'Q', 'V', 'P', 'G', 'F', 'T', 'P', 'R', 'L', 'A', 'I', 'L', 'Q', 'V', 'G', 'N', 'R', 'D', 'D', 'S', 'N', 'L', 'Y', 'I', 'N', 'V', 'K', 'L', 'K', 'A', 'A', 'E', 'E', 'I', 'G', 'I', 'K', 'A', 'T', 'H', 'I', 'K', 'L', 'P', 'R', 'T', 'T', 'T', 'E', 'S', 'E', 'V', 'P', 'D', 'D', 'K', 'K', 'P', 'N', 'G', 'R', 'K', 'V', 'V', 'G', 'D', 'V', 'A', 'Y', 'D', 'E', 'A', 'K', 'E', 'R', 'A', 'S', 'F', 'I', 'T', 'P', 'V', 'P', 'G', 'G', 'V', 'G', 'P', 'M', 'T', 'V', 'A', 'M', 'L', 'M', 'Q', 'S', 'T', 'V', 'E', 'S', 'A', 'K', 'R', 'F', 'L', 'E', 'K', 'F', 'K', 'P', 'G', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
['A', 'S', 'R', 'L', 'L', 'L', 'N', 'N', 'G', 'A', 'K', 'M', 'P', 'I', 'L', 'G', 'L', 'G', 'T', 'W', 'K', 'S', 'P', 'P', 'G', 'Q', 'V', 'T', 'E', 'A', 'V', 'K', 'V', 'A', 'I', 'D', 'V', 'G', 'Y', 'R', 'H', 'I', 'D', 'C', 'A', 'H', 'V', 'Y', 'Q', 'N', 'E', 'N', 'E', 'V', 'G', 'V', 'A', 'I', 'Q', 'E', 'K', 'L', 'R', 'E', 'Q', 'V', 'V', 'K', 'R', 'E', 'E', 'L', 'F', 'I', 'V', 'S', 'K', 'L', 'W', 'C', 'N', 'K', 'T', 'T', 'A', 'Q', 'V', 'L', 'I', 'R', 'F', 'P', 'M', 'Q', 'R', 'N', 'L', 'V', 'V', 'I', 'P', 'K', 'S', 'V', 'T', 'P', 'E', 'R', 'I', 'A', 'E', 'N', 'F', 'K', 'V', 'F', 'D', 'F', 'E', 'L', 'S', 'S', 'Q', 'D', 'M', 'T', 'T', 'L', 'L', 'S', 'Y', 'N', 'R', 'N', 'W', 'R', 'V', 'S', 'A', 'L', 'L', 'S', 'C', 'T', 'S', 'H', 'K', 'D', 'Y', 'P', 'F', 'H', 'E', 'E', 'F', 'X', 'X', 'X', 'X', 'X']
]

model = Word2Vec(sentences=ez, size=100, window=5, min_count=5, workers=4, sg=0)
a = model.wv.most_similar('A')
print(a)
