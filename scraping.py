import urllib.request
from bs4 import BeautifulSoup
from decimal import Decimal

def KDAFinder():
	player = input("Player?\n")
	url = f"https://liquipedia.net/valorant/{player}/Matches"
	try:
		urllib.request.urlopen(url)
	except:
		print("not found!\n")
		KDAFinder()
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, "lxml")
	all_tables = soup.find_all("table")
	right_table=soup.find("table")

	K=[]
	D=[]
	A=[]
	R=[]
	matches = 0

	for row in right_table.findAll('tr')[1:]:
		matches += 1
		cells=row.findAll('td')
		try:
			K.append(float(cells[7].find(text=True)))
		except:
			print("A match has missing values!")
		try:
			D.append(float(cells[8].find(text=True)))
		except:
			pass
		try:
			A.append(float(cells[9].find(text=True)))
		except:
			pass
	kills = sum(K)
	deaths = sum(D)
	assists = sum(A)

	kda = Decimal((((kills) + (assists))/deaths))
	roundedkda = round(kda, 2)

	print()
	print(f"Kills: {kills}")
	print(f"Deaths: {deaths}")
	print(f"Assists: {assists}")
	print(f"Matches scraped: {matches}")
	print(f"KDA Ratio: {roundedkda}")
	print()
	KDAFinder()

KDAFinder()