# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 15:15:33 2015

@author: wu34
"""
from nltk import wordpunct_tokenize
import dietType
import actType
import buildTypeIndex
import dietActInfoRetrv

available_list = ['039','044','045','048','049','050','051','052','053','054','056','057','058','059','060','061','063','064','065','066','067','068','069','070','071','072','073','074','075']

#create diet type frequency txt file for every user 
def buildSingleDietTypeFreqFile():
	
	for subjectID in available_list:
		f_diet = open('diet/dietTypeFreq/dietType_frequency_'+subjectID+'.txt','w')
		singleDietType_dict = buildTypeIndex.build_single_diet_index(subjectID)

		for key in singleDietType_dict:
			f_diet.write("%-25s%-10s"%(key,singleDietType_dict[key]))
			f_diet.write('\n')

		f_diet.close()

#create activity type frequency txt file for every user 
def buildSingleActTypeFreqFile():
	
	for subjectID in available_list:
		f_act = open('activity/activityTypeFreq/activityType_frequency_'+subjectID+'.txt','w')
		singleActType_dict = buildTypeIndex.build_single_activity_index(subjectID)

		for key in singleActType_dict:
			f_act.write("%-25s%-10s"%(key,singleActType_dict[key]))
			f_act.write('\n')

		f_act.close()

#create diet type frequency txt file for every user 
def buildDailySingleDietTypeFreqFile():
	
	for subjectID in available_list:
		duration = dietActInfoRetrv.getDuration(subjectID)
		
		for n in range(1,duration+1):
			f_diet = open('diet/dietTypeFreq/dietType_frequency_'+subjectID+'_'+str(n)+'.txt','w')
			singleDietType_dict = buildTypeIndex.build_daily_single_diet_index(subjectID,n)
			for key in singleDietType_dict:
				f_diet.write("%-25s%-10s"%(key,singleDietType_dict[key]))
				f_diet.write('\n')
			f_diet.close()

#create activity type frequency txt file for every user 
def buildDailySingleActTypeFreqFile():
	
	for subjectID in available_list:
		duration = dietActInfoRetrv.getDuration(subjectID)
		
		for n in range(1,duration+1):
			f_act = open('activity/activityTypeFreq/activityType_frequency_'+subjectID+'_'+str(n)+'.txt','w')
			singleActType_dict = buildTypeIndex.build_daily_single_activity_index(subjectID,n)
			for key in singleActType_dict:
				f_act.write("%-25s%-10s"%(key,singleActType_dict[key]))
				f_act.write('\n')
			f_act.close()

# create overall diet type frequency txt file
def buildDietTypeFreqTXTFile():
	dietType_dict = {}
	f_diet = open('diet/dietOverallTypeFreq/all_dietType_frequency.txt','w')
	for line in open('diet/dietOverallItemFreq/all_diet_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[0], type(words[1])
		#words[0]: item
		#words[1]: item frequency
		diettype = dietType.dietType(words[0])
		# print diettype
		temp = int(words[1])
		if diettype != 'others':
			if diettype in dietType_dict:
				dietType_dict[diettype] += temp
				# print dietType_dict[diettype]
				# print type(dietType_dict[diettype])
			else:
				dietType_dict[diettype] = temp
				# print dietType_dict[diettype]
	# print dietType_dict
	for key in dietType_dict:
		f_diet.write("%-25s%-10s"%(key,dietType_dict[key]))
		f_diet.write('\n')
	f_diet.close()

# create overall diet type frequency txt file
def buildActTypeFreqTXTFile():
	actType_dict = {}
	f_act = open('activity/activityOverallTypeFreq/all_activityType_frequency.txt','w')
	for line in open('activity/activityOverallItemFreq/all_activity_frequency.txt','r'):
		line = line.strip('\n')
		words = wordpunct_tokenize(line)
		#print words[0], type(words[1])
		#words[0]: item
		#words[1]: item frequency
		acttype = actType.actType(words[0]) 
		temp = int(words[1])
		if acttype != 'none':
			if acttype in actType_dict:
				actType_dict[acttype] += temp
			else:
				actType_dict[acttype] = temp
	# print actType_dict
	for key in actType_dict:
		f_act.write("%-25s%-10s"%(key,actType_dict[key]))
		f_act.write('\n')
	f_act.close()

def buildTypeFreqTXTFile():
	print 'in buildTypeFreqTXTFile()'
	buildSingleDietTypeFreqFile()
	buildSingleActTypeFreqFile()
	buildDailySingleDietTypeFreqFile()
	buildDailySingleActTypeFreqFile()
	buildDietTypeFreqTXTFile()
	buildActTypeFreqTXTFile()

# buildTypeFreqTXTFile()
