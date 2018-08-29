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
	apmassey = []
	for i in allvoterdata:
		for ii in i:
			if ii not in apmassey:
				apmassey.append(ii)
	top25 = []
	for i in apmassey:
		rating = 0
		for voter in allvoterdata:
			for iidx,ii in enumerate(voter):
				if ii==i:
					rating += max(0,25-iidx)
		top25.append([i, rating])

	unsorted = True
	while unsorted:
		unsorted = False
		for i in range(0,len(top25)-1):
			if top25[i][1]<top25[i+1][1]:
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
	goodteams = unbiasedRank(week)
	allranks.append(goodteams)

print goodteams

istr = 'aprank'
for i in goodteams:
	istr += ','+i[0]+','+str(i[1])

f = open('aprank.txt','w')
f.write(istr+'\n')
f.close()












