import urllib.request
from bs4 import BeautifulSoup
from decimal import Decimal

def KDAFinder():
	player = input("Player?\n")
	url = f"https://liquipedia.net/valorant/{player}/Matches"
	try:
		page = urllib.request.urlopen(url)
	except:
		print("not found!\n")
		KDAFinder()
	soup = BeautifulSoup(page, "lxml")
	all_tables = soup.find_all("table")
	right_table=soup.find("table")

	K = 0
	D = 0
	A = 0
	R = 0
	matches = 0

	for row in right_table.findAll('tr')[1:]:
		matches += 1
		cells=row.findAll('td')
		try:
			K += float(cells[7].find(text=True))
		except:
			print("A match has missing values!")
		try:
			D += float(cells[8].find(text=True))
		except:
			pass
		try:
			A += float(cells[9].find(text=True))
		except:
			pass

	kda = Decimal((K + A)/D)
	roundedkda = round(kda, 2)

	print()
	print(f"Kills: {K}")
	print(f"Deaths: {D}")
	print(f"Assists: {A}")
	print(f"Matches scraped: {matches}")
	print(f"KDA Ratio: {roundedkda}")
	print()
	KDAFinder()

KDAFinder()
