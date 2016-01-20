# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:24:53 2015

@author: wu34
"""

#build the diet index for single user
def build_single_diet_index(subjectID):
	index = {}
	for line in open('dietProcessed/processed_diet_'+subjectID+'.txt'):
		# print 'line in processed_diet_'+subjectID+'.txt'
		# print line
		line = line.split('[')[1].split(']')[0].split(',')
		for word in line: 
			word = word.strip(' ')
			# print word
			if word in index:
				index[word] += 1
			else:
				index[word] = 1
	return index

#build the activity index for single user
def build_single_activity_index(subjectID):
	index = {}
	for line in open('activityProcessed/processed_activity_'+subjectID+'.txt'):
		# print 'line in processed_activity_'+subjectID+'.txt'
		# print line
		line = line.split('[')[1].split(']')[0].split(',')
		for word in line: 
			word = word.strip(' ')
			# print word
			if word in index:
				index[word] += 1
			else:
				index[word] = 1
	return index

#build the diet index for all users
def build_all_diet_index(available_list):
	index = {}
	for subjectID in available_list:
		small_index = build_single_diet_index(subjectID)
		for key in small_index:
			if key in index:
				index[key] += small_index[key]
			else:
				index[key] = small_index[key]
	return index

#build the activity index for all users
def build_all_activity_index(available_list):
	index = {}
	for subjectID in available_list:
		small_index = build_single_activity_index(subjectID)
		for key in small_index:
			if key in index:
				index[key] += small_index[key]
			else:
				index[key] = small_index[key]
	return index

#index = build_single_diet_index('075')
#print index
# index = build_single_activity_index(75)
# print index