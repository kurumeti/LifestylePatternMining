# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:26:06 2015

@author: wu34
"""
import matplotlib.pyplot as plt
import extractDietAct 
import preprocessDiary
import buildItemFreqTXTFile
import buildTypeFreqTXTFile
import visDietActPattern
import buildSimilarityTableExcel
import visSimilarityDistribution
import visSimilarityMat

plt.close('all')
plt.clf()

# extract diet and activity information from excel
extractDietAct.extractDietAct()

# preprocessing include: tokenization, word removal, spell checking, lemmatization
preprocessDiary.preprocessDiary()

# build the diet/activity index with Item frequency in txt files 
buildItemFreqTXTFile.buildItemFreqTXTFile()

# build diet/activity type frequency in txt file 
buildTypeFreqTXTFile.buildTypeFreqTXTFile()

# data visualization (pie chart) for diet/activity pattern 
visDietActPattern.visDietActPattern()

# build excel table for the similarity between two users 
# the parameter is to set the similarity measurement method, the default is TFIDFCosin
# numberOfSameWord,jaccard,novelJaccard,TFIDFCosin,TFIDFEclud,TFCosin,TFEclud
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'jaccard')
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'novelJaccard')
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'TFCosin')
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'TFEclud')
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'TFIDFCosin')
buildSimilarityTableExcel.buildSimilarityTableExcel(sim = 'TFIDFEclud')


# visualization of similarity distribution (histogram)
# the parameter is to set the similarity measurement method, the default is TFIDFCosin
# numberOfSameWord,jaccard,novelJaccard,TFIDFCosin,TFIDFEclud,TFCosin,TFEclud
visSimilarityDistribution.plotSimilarityDistribution('jaccard')
visSimilarityDistribution.plotSimilarityDistribution('novelJaccard')
visSimilarityDistribution.plotSimilarityDistribution('TFCosin')
visSimilarityDistribution.plotSimilarityDistribution('TFEclud')
visSimilarityDistribution.plotSimilarityDistribution('TFIDFCosin')
visSimilarityDistribution.plotSimilarityDistribution('TFIDFEclud')


# visualization of similarity matrix 
# the parameter is to set the similarity measurement method, the default is TFIDFCosin
# numberOfSameWord,jaccard,novelJaccard,TFIDFCosin,TFIDFEclud,TFCosin,TFEclud
visSimilarityMat.plotSimilarityMatrix('jaccard')
visSimilarityMat.plotSimilarityMatrix('novelJaccard')
visSimilarityMat.plotSimilarityMatrix('TFCosin')
visSimilarityMat.plotSimilarityMatrix('TFEclud')
visSimilarityMat.plotSimilarityMatrix('TFIDFCosin')
visSimilarityMat.plotSimilarityMatrix('TFIDFEclud')

