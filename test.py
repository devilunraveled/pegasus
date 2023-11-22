import time
import numpy as np

from evaluation import rougeScores
from dataLoader import DataLoader
from Pegasus import GetSummary
import sys
sys.path.append('..')


#Loading the datasets through the custom dataloader.
datasetLoader = DataLoader(datasetName='arxiv')
arxivTest = datasetLoader.getData('../Datasets/', split='test')
datasetLoader.datasetName = 'pubmed'
pubmedTest = datasetLoader.getData('../Datasets/', split='test')

### For a low scale testing
### pick only the first 1000 rows from the dataframes

# arxiv_test = arxiv_test[:10]
# pubmed_test = pubmed_test[:100]

# creating 'Gold Summary' column
def mapping(row):
    row['Gold Summary'] = ''.join(row['abstract_text'])
    return row

arxivTest = arxivTest.apply(mapping, axis=1)
pubmedTest = pubmedTest.apply(mapping, axis=1)

# generating summaries
def generateSummary(row):
    article = ''.join(row['article_text'])
    summary = GetSummary(article)[0]
    row['Generated Summary'] = summary
    print(f"Generated summary for {row['article_id']}.")
    return row

startTime = time.time()
arxivTest = arxivTest.apply(generateSummary, axis=1)
print('Time taken for arxiv: ', time.time() - startTime)


startTime = time.time()
pubmedTest = pubmedTest.apply(generateSummary, axis=1)
print('Time taken for pubmed: ', time.time() - startTime)


arxivTest, rougeScoresArxiv = rougeScores(arxivTest)
pubmedTest, rougeScoresPubmed = rougeScores(pubmedTest)

# printing the results
print('arxiv')
print('rouge1: ', np.mean([ score.fmeasure for score in rougeScoresArxiv['rouge1'] ]))
print('rouge2: ', np.mean([ score.fmeasure for score in rougeScoresArxiv['rouge2'] ]))
print('rougeL: ', np.mean([ score.fmeasure for score in rougeScoresArxiv['rougeL'] ]))
print('BertScore : ', np.mean( [score for score in rougeScoresArxiv['bertScore']]))


print('pubmed')
print('rouge1: ', np.mean([ score.fmeasure for score in rougeScoresPubmed['rouge1'] ]))
print('rouge2: ', np.mean([ score.fmeasure for score in rougeScoresPubmed['rouge2'] ]))
print('rougeL: ', np.mean([ score.fmeasure for score in rougeScoresPubmed['rougeL'] ]))
print('BertScore : ', np.mean( [score for score in rougeScoresPubmed['bertScore']]))

# saving the results
arxivTest.to_csv('arxiv_test_pegasus.csv')
pubmedTest.to_csv('pubmed_test_pegasus.csv')
