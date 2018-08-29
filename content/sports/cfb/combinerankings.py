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


def addtodata(typedata,typei):
	for i in allteams:
		for ii in range(0,len(typedata)):
			if ii%2 == 1:
				if typedata[ii]==i[0]:
					i[typei] = (ii+1)/2

apconvert = [["ACC","boston-college",103],["ACC","clemson",228],["ACC","duke",150],["ACC","florida-state",52],["ACC","georgia-tech",59],["ACC","louisville",97],["ACC","miami-fl",2390],["ACC","north-carolina",153],["ACC","north-carolina-state",152],["ACC","pittsburgh",221],["ACC","syracuse",183],["ACC","virginia",258],["ACC","virginia-tech",259],["ACC","wake-forest",154],["Big 12","baylor",239],["Big 12","iowa-state",66],["Big 12","kansas",2305],["Big 12","kansas-state",2306],["Big 12","oklahoma",201],["Big 12","oklahoma-state",197],["Big 12","tcu",2628],["Big 12","texas",251],["Big 12","texas-tech",2641],["Big 12","west-virginia",277],["Big Ten","illinois",356],["Big Ten","indiana",84],["Big Ten","iowa",2294],["Big Ten","maryland",120],["Big Ten","michigan",130],["Big Ten","michigan-state",127],["Big Ten","minnesota",135],["Big Ten","nebraska",158],["Big Ten","northwestern",77],["Big Ten","ohio-state",194],["Big Ten","penn-state",213],["Big Ten","purdue",2509],["Big Ten","rutgers",164],["Big Ten","wisconsin",275],["Conf USA","fiu",2229],["Conf USA","florida-atlantic",2226],["Conf USA","louisiana-tech",2348],["Conf USA","marshall",276],["Conf USA","middle-tennessee",2393],["Conf USA","north-texas",249],["Conf USA","old-dominion",295],["Conf USA","rice",242],["Conf USA","southern-miss",2572],["Conf USA","utep",2638],["Conf USA","utsa",2636],["Conf USA","western-kentucky",98],["Independent","army",349],["Independent","brigham-young",252],["Independent","charlotte",2429],["Independent","notre-dame",87],["Independent","ua-birmingham",5],["Mid-American","akron",2006],["Mid-American","ball-state",2050],["Mid-American","bowling-green",189],["Mid-American","buffalo",2084],["Mid-American","central-michigan",2117],["Mid-American","eastern-michigan",2199],["Mid-American","kent-state",2309],["Mid-American","massachusetts",113],["Mid-American","miami-ohio",193],["Mid-American","northern-illinois",2459],["Mid-American","ohio",195],["Mid-American","toledo",2649],["Mid-American","western-michigan",2711],["M. West","air-force",2005],["M. West","boise-state",68],["M. West","colorado-state",36],["M. West","fresno-state",278],["M. West","hawaii",62],["M. West","nevada",2440],["M. West","new-mexico",167],["M. West","san-diego-state",21],["M. West","san-jose-state",23],["M. West","unlv",2439],["M. West","utah-state",328],["M. West","wyoming",2751],["Pac-12","arizona",12],["Pac-12","arizona-state",9],["Pac-12","california",25],["Pac-12","colorado",38],["Pac-12","oregon",2483],["Pac-12","oregon-state",204],["Pac-12","stanford",24],["Pac-12","ucla",26],["Pac-12","usc",30],["Pac-12","utah",254],["Pac-12","washington",264],["Pac-12","washington-state",265],["SEC","alabama",333],["SEC","arkansas",8],["SEC","auburn",2],["SEC","florida",57],["SEC","georgia",61],["SEC","kentucky",96],["SEC","lsu",99],["SEC","mississippi",145],["SEC","mississippi-state",344],["SEC","missouri",142],["SEC","south-carolina",2579],["SEC","tennessee",2633],["SEC","texas-am",245],["SEC","vanderbilt",238],["Sun Belt","appalachian-state",2026],["Sun Belt","arkansas-state",2032],["Sun Belt","coastal-carolina",324],["Sun Belt","georgia-southern",290],["Sun Belt","georgia-state",2247],["Sun Belt","idaho",70],["Sun Belt","louisiana-lafayette",309],["Sun Belt","louisiana-monroe",2433],["Sun Belt","new-mexico-state",166],["Sun Belt","south-alabama",6],["Sun Belt","texas-state",326],["Sun Belt","troy",2653],["American","cincinnati",2132],["American","connecticut",41],["American","east-carolina",151],["American","houston",248],["American","memphis",235],["American","navy",2426],["American","southern-methodist",2567],["American","south-florida",58],["American","temple",218],["American","tulane",2655],["American","tulsa",202],["American","ucf",2116]]
apmassey = [["ACC","boston-college",783],["ACC","clemson",1603],["ACC","duke",2265],["ACC","florida-state",2666],["ACC","georgia-tech",2911],["ACC","louisville",4224],["ACC","miami-fl",4719],["ACC","north-carolina",5492],["ACC","north-carolina-state",5511],["ACC","pittsburgh",6236],["ACC","syracuse",7729],["ACC","virginia",8432],["ACC","virginia-tech",8459],["ACC","wake-forest",8508],["Big 12","baylor",557],["Big 12","iowa-state",3554],["Big 12","kansas",3717],["Big 12","kansas-state",3731],["Big 12","oklahoma",5886],["Big 12","oklahoma-state",5912],["Big 12","tcu",7878],["Big 12","texas",7840],["Big 12","texas-tech",7918],["Big 12","west-virginia",8716],["Big Ten","illinois",3425],["Big Ten","indiana",3484],["Big Ten","iowa",3540],["Big Ten","maryland",4474],["Big Ten","michigan",4741],["Big Ten","michigan-state",4757],["Big Ten","minnesota",4858],["Big Ten","nebraska",5279],["Big Ten","northwestern",5704],["Big Ten","ohio-state",5850],["Big Ten","penn-state",6114],["Big Ten","purdue",6393],["Big Ten","rutgers",6696],["Big Ten","wisconsin",9031],["Conf USA","fiu",2652],["Conf USA","florida-atlantic",2638],["Conf USA","louisiana-tech",4218],["Conf USA","marshall",4436],["Conf USA","middle-tennessee",4785],["Conf USA","north-texas",5584],["Conf USA","old-dominion",5925],["Conf USA","rice",6535],["Conf USA","southern-miss",7365],["Conf USA","utep",7933],["Conf USA","utsa",7900],["Conf USA","western-kentucky",8761],["Independent","army",356],["Independent","brigham-young",891],["Independent","charlotte",8156],["Independent","notre-dame",5749],["Independent","ua-birmingham",87],["Mid-American","akron",66],["Mid-American","ball-state",501],["Mid-American","bowling-green",821],["Mid-American","buffalo",979],["Mid-American","central-michigan",1404],["Mid-American","eastern-michigan",2353],["Mid-American","kent-state",3771],["Mid-American","massachusetts",4548],["Mid-American","miami-ohio",4725],["Mid-American","northern-illinois",5634],["Mid-American","ohio",5825],["Mid-American","toledo",7978],["Mid-American","western-michigan",8767],["M. West","air-force",55],["M. West","boise-state",771],["M. West","colorado-state",1753],["M. West","fresno-state",2776],["M. West","hawaii",3197],["M. West","nevada",5316],["M. West","new-mexico",5371],["M. West","san-diego-state",7002],["M. West","san-jose-state",7024],["M. West","unlv",5323],["M. West","utah-state",8325],["M. West","wyoming",9162],["Pac-12","arizona",294],["Pac-12","arizona-state",304],["Pac-12","california",1098],["Pac-12","colorado",1715],["Pac-12","oregon",5961],["Pac-12","oregon-state",5970],["Pac-12","stanford",7582],["Pac-12","ucla",8141],["Pac-12","usc",8251],["Pac-12","utah",8315],["Pac-12","washington",8551],["Pac-12","washington-state",8588],["SEC","alabama",74],["SEC","arkansas",316],["SEC","auburn",402],["SEC","florida",2625],["SEC","georgia",2881],["SEC","kentucky",3781],["SEC","lsu",4206],["SEC","mississippi",4920],["SEC","mississippi-state",4936],["SEC","missouri",4948],["SEC","south-carolina",7242],["SEC","tennessee",7801],["SEC","texas-am",7848],["SEC","vanderbilt",8367],["Sun Belt","appalachian-state",275],["Sun Belt","arkansas-state",333],["Sun Belt","coastal-carolina",1637],["Sun Belt","georgia-southern",2899],["Sun Belt","georgia-state",2907],["Sun Belt","idaho",3415],["Sun Belt","louisiana-lafayette",4194],["Sun Belt","louisiana-monroe",4200],["Sun Belt","new-mexico-state",5387],["Sun Belt","south-alabama",7237],["Sun Belt","texas-state",7911],["Sun Belt","troy",8068],["American","cincinnati",1529],["American","connecticut",1872],["American","east-carolina",2292],["American","houston",3347],["American","memphis",4636],["American","navy",5253],["American","southern-methodist",7358],["American","south-florida",7278],["American","temple",7788],["American","tulane",8092],["American","tulsa",8099],["American", "ucf",1380]]
nameconvert = [['boston-college', 'Boston College'], ['clemson', 'Clemson'], ['duke', 'Duke'], ['florida-state', 'Florida State'], ['georgia-tech', 'Georgia Tech'], ['louisville', 'Louisville'], ['miami-fl', 'Miami (FL)'], ['north-carolina', 'North Carolina'], ['north-carolina-state', 'North Carolina State'], ['pittsburgh', 'Pittsburgh'], ['syracuse', 'Syracuse'], ['virginia', 'Virginia'], ['virginia-tech', 'Virginia Tech'], ['wake-forest', 'Wake Forest'], ['baylor', 'Baylor'], ['iowa-state', 'Iowa State'], ['kansas', 'Kansas'], ['kansas-state', 'Kansas State'], ['oklahoma', 'Oklahoma'], ['oklahoma-state', 'Oklahoma State'], ['tcu', 'TCU'], ['texas', 'Texas'], ['texas-tech', 'Texas Tech'], ['west-virginia', 'West Virginia'], ['illinois', 'Illinois'], ['indiana', 'Indiana'], ['iowa', 'Iowa'], ['maryland', 'Maryland'], ['michigan', 'Michigan'], ['michigan-state', 'Michigan State'], ['minnesota', 'Minnesota'], ['nebraska', 'Nebraska'], ['northwestern', 'Northwestern'], ['ohio-state', 'Ohio State'], ['penn-state', 'Penn State'], ['purdue', 'Purdue'], ['rutgers', 'Rutgers'], ['wisconsin', 'Wisconsin'], ['fiu', 'FIU'], ['florida-atlantic', 'Florida Atlantic'], ['louisiana-tech', 'Louisiana Tech'], ['marshall', 'Marshall'], ['middle-tennessee', 'Middle Tennessee'], ['north-texas', 'North Texas'], ['old-dominion', 'Old Dominion'], ['rice', 'Rice'], ['southern-miss', 'Southern Miss'], ['utep', 'UTEP'], ['utsa', 'UTSA'], ['western-kentucky', 'Western Kentucky'], ['army', 'Army'], ['ua-birmingham', 'UA-Birmingham'], ['brigham-young', 'Brigham Young'], ['charlotte', 'Charlotte'], ['notre-dame', 'Notre Dame'], ['akron', 'Akron'], ['ball-state', 'Ball State'], ['bowling-green', 'Bowling Green'], ['buffalo', 'Buffalo'], ['central-michigan', 'Central Michigan'], ['eastern-michigan', 'Eastern Michigan'], ['kent-state', 'Kent State'], ['massachusetts', 'Massachusetts'], ['miami-ohio', 'Miami (Ohio)'], ['northern-illinois', 'Northern Illinois'], ['ohio', 'Ohio'], ['toledo', 'Toledo'], ['western-michigan', 'Western Michigan'], ['air-force', 'Air Force'], ['boise-state', 'Boise State'], ['colorado-state', 'Colorado State'], ['fresno-state', 'Fresno State'], ['hawaii', 'Hawaii'], ['nevada', 'Nevada'], ['new-mexico', 'New Mexico'], ['san-diego-state', 'San Diego State'], ['san-jose-state', 'San Jose State'], ['unlv', 'UNLV'], ['utah-state', 'Utah State'], ['wyoming', 'Wyoming'], ['arizona', 'Arizona'], ['arizona-state', 'Arizona State'], ['california', 'California'], ['colorado', 'Colorado'], ['oregon', 'Oregon'], ['oregon-state', 'Oregon State'], ['stanford', 'Stanford'], ['ucla', 'UCLA'], ['usc', 'USC'], ['utah', 'Utah'], ['washington', 'Washington'], ['washington-state', 'Washington State'], ['alabama', 'Alabama'], ['arkansas', 'Arkansas'], ['auburn', 'Auburn'], ['florida', 'Florida'], ['georgia', 'Georgia'], ['kentucky', 'Kentucky'], ['lsu', 'LSU'], ['mississippi', 'Mississippi'], ['mississippi-state', 'Mississippi State'], ['missouri', 'Missouri'], ['south-carolina', 'South Carolina'], ['tennessee', 'Tennessee'], ['texas-am', 'Texas A&amp;M'], ['vanderbilt', 'Vanderbilt'], ['appalachian-state', 'Appalachian State'], ['arkansas-state', 'Arkansas State'], ['coastal-carolina', 'Coastal Carolina'], ['georgia-southern', 'Georgia Southern'], ['georgia-state', 'Georgia State'], ['idaho', 'Idaho'], ['louisiana-lafayette', 'Louisiana-Lafayette'], ['new-mexico-state', 'New Mexico State'], ['louisiana-monroe', 'Louisiana-Monroe'], ['south-alabama', 'South Alabama'], ['texas-state', 'Texas State'], ['troy', 'Troy'], ['cincinnati', 'Cincinnati'], ['connecticut', 'Connecticut'], ['east-carolina', 'East Carolina'], ['houston', 'Houston'], ['navy', 'Navy'], ['memphis', 'Memphis'], ['southern-methodist', 'Southern Methodist'], ['south-florida', 'South Florida'], ['tulane', 'Tulane'], ['temple', 'Temple'], ['tulsa', 'Tulsa'], ['ucf', 'UCF'], ['north-dakota-state', 'North Dakota State'], ['alabama', 'Alabama'], ['penn-state', 'Penn State'], ['georgia', 'Georgia'], ['tcu', 'TCU'], ['wisconsin', 'Wisconsin'], ['ohio-state', 'Ohio State'], ['clemson', 'Clemson'], ['miami-fl', 'Miami (FL)'], ['notre-dame', 'Notre Dame'], ['oklahoma', 'Oklahoma']]

aprank = readcsv('aprank.txt')[0]
allteams = []
for i in range(0,len(aprank)):
	if i%2 == 1:
		allteams.append([aprank[i],(i+1)/2,26,26,26,26])
bordadata = readcsv('borda.txt')[0]
addtodata(bordadata,2)
addtodata(readcsv('condorcet.txt')[0],3)
addtodata(readcsv('fptp.txt')[0],4)
addtodata(readcsv('irv.txt')[0],5)
istr = 'teams: ['
for i in range(0,25):
	istr += '{'
	istr += '"rank":'
	if allteams[i][1] < 26:
		istr += str(allteams[i][1])+','
	else:
		istr += 'NR,'
		
	istr += '"borda":'
	if allteams[i][2] < 26:
		istr += str(allteams[i][2])+','
	else:
		istr += 'NR,'
	istr += '"condorcet":'
	if allteams[i][3] < 26:
		istr += str(allteams[i][3])+','
	else:
		istr += 'NR,'
	istr += '"fptp":'
	if allteams[i][4] < 26:
		istr += str(allteams[i][4])+','
	else:
		istr += 'NR,'
	istr += '"irv":'
	if allteams[i][5] < 26:
		istr += str(allteams[i][5])+','
	else:
		istr += 'NR,'
	istr += '"conference":"'
	for ii in apconvert:
		if ii[1]==allteams[i][0]:
			istr += str(ii[0])+'",'
			break
	istr += '"school":"'
	for ii in nameconvert:
		if ii[0]==allteams[i][0]:
			istr += str(ii[1])+'"},'
			break
print istr+']'













