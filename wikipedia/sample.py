infile = open("data/wiki-Talk.txt", "r")
outfile2 = open("data/wiki-Talk_2.txt", "w+")
outfile4 = open("data/wiki-Talk_4.txt", "w+")
outfile10 = open("data/wiki-Talk_10.txt", "w+")
outfile100 = open("data/wiki-Talk_100.txt", "w+")
outfile1000 = open("data/wiki-Talk_1000.txt", "w+")
outfile10000 = open("data/wiki-Talk_10000.txt", "w+")

i = 0
for line in infile:
	if (i % 2 == 0):
		outfile2.write(line)
	if (i % 4 == 0):
		outfile4.write(line)
	if (i % 10 == 0):
		outfile10.write(line)
	if (i % 100 == 0):
		outfile100.write(line)
	if (i % 1000 == 0):
		outfile1000.write(line)
	if (i % 10000 == 0):
		outfile10000.write(line)
	i = i+1
	