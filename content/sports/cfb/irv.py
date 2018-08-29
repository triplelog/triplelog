import time

import random
import csv
import math


def writecsv(parr, filen):
		with open(filen, 'wb') as csvfile:
				spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
				for i in range(0,len(parr)):
						try:
								spamwriter.writerow(parr[i])
						except:
								print parr[i], i


def readcsv(filen):
		allgamesa  =[]
		with open(filen, 'rb') as csvfile:
				spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
				for row in spamreader:
						allgamesa.append(row)
		return allgamesa



def getvotes(burl):
	allvotes = [[],[],[],[],[],[],[],[],[],[]]
	res = requests.get(burl)
	doc = html.fromstring(res.content)
	voteTable = doc.xpath("//tbody//td")
	for idx,vote in enumerate(voteTable):
		if idx%13>=3:
			allvotes[idx%13-3].append(vote.text_content())
	return allvotes

def unbiasedRank(my_week):
	allvoters = []
	allvotes = readcsv('week16test.csv')
	for i in allvotes:
		allvoters.append(i[0])


	allvoterdata = []
	for voter in allvoters:
		for ii in allvotes:
			if ii[0]==voter:
				voterranks = ii[1:]
				allranks = voterranks
		allvoterdata.append(allranks)

	top25 = []
	for i in apmassey:
		rating = 0
		for voter in allvoterdata:
			for iidx,ii in enumerate(voter):
				if ii==i[1]:
					rating += max(0,25-iidx)
		top25.append([i[1], rating, rating,0])

	unsorted = True
	while unsorted:
		unsorted = False
		for i in range(0,len(top25)-1):
			if top25[i][2]<top25[i+1][2]:
				holdit = top25[i]
				top25[i]=top25[i+1]
				top25[i+1]=holdit
				unsorted = True
	return top25

import sys
#this_week = int(sys.argv[1])
this_week = 1

allranks = []
for week in range(1,this_week+1):
	#allvotes = getvotes('https://bbwaa.com/17-nl-'+award+'-ballots/')
	#writecsv(allvotes,'nlmvp17.csv')
	goodteams = []
	for iiiiii in range(0,25):
		rawvotes = readcsv('week16test.csv')
		allvotes = []
		for i in range(0,25):
			allvotes.append([])
		for i in rawvotes:
			if len(i)>25:
				for ii in range(0,25):
					allvotes[ii].append(i[ii+1])


		orderedvotes = []
		for ii in range(0,len(allvotes[0])):
			orderedvotes.append([])
		for i in range(0,len(allvotes)):
			for ii in range(0,len(allvotes[0])):
				orderedvotes[ii].append(allvotes[i][ii])
		allvotes = orderedvotes


		
		allteams = []
		for i in allvotes:
			for ii in i:
				if ii not in allteams:
					allteams.append(ii)

		for i in goodteams:
				allteams.remove(i[0])
				for ii in range(0,len(allvotes)):
					for iii in range(0,len(allvotes[ii])):
						if allvotes[ii][iii]==i[0]:
							allvotes[ii].remove(allvotes[ii][iii])
							break
				
		anyoneleft = True
		while anyoneleft:
			allwp = []
			for idx,i in enumerate(allteams):
				myfirst = 0
				totalvotes = 0
				for ii in allvotes:
					if len(ii) > 0:
						totalvotes += 1
						if ii[0] == i:
							myfirst += 1
				allwp.append([i, myfirst])
				if myfirst > totalvotes/2:
					print "winner", i, myfirst, totalvotes
					goodteams.append([i,0])
					anyoneleft = False
			if anyoneleft and len(allteams) == 2:
				print "tie", allteams
				goodteams.append([allteams[0],0])
				goodteams.append([allteams[1],1])
				anyoneleft = False
			if anyoneleft:
				minwp = len(allvotes)
				minindex = []
				for idx,i in enumerate(allwp):
					if i[1]>0:
						print i[0], i[1]
					if i[1]<minwp:
						minwp = i[1]
						minindex = [i[0]]
					elif i[1]==minwp:
						minindex.append(i[0])
				if len(minindex)==len(allteams):
					for idx,i in enumerate(minindex):
						goodteams.append([i,idx])
					anyoneleft = False
				for i in minindex:
					allteams.remove(i)
					for ii in range(0,len(allvotes)):
						for iii in range(0,len(allvotes[ii])):
							if allvotes[ii][iii]==i:
								allvotes[ii].remove(allvotes[ii][iii])
								break

	allranks.append(goodteams)

print goodteams

istr = 'irv'
for i in goodteams:
	istr += ','+i[0]+','+str(i[1])

f = open('irv.txt','w')
f.write(istr+'\n')
f.close()












