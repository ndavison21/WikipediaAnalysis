import pylab as plt

hist_1 = dict()
with open("data/separation_10000_parallel.txt", "r") as f_1:
	for line in f_1.readlines():
		key, num, prob = (line.rstrip('\n')).split(' ')
		hist_1[int(key)] = float(prob)

mean = 0
hist_2 = dict()
with open("data/separation_100000.txt", "r") as f_2:
	for line in f_2.readlines():
		key, num, prob = (line.rstrip('\n')).split(' ')
		hist_2[int(key)] = float(prob)
		mean += int(key) * float(prob)

print mean

print "Drawing Path Length Distributions"
plt.figure()
plt.grid(True)
plt.plot(hist_1.keys(), hist_1.values(), 'ro-')
plt.plot(hist_2.keys(), hist_2.values(), 'gx-')
plt.legend(['10,000 Samples', '100,000 Samples'])
plt.xlabel('Path Length')
plt.ylabel('Proportion')
plt.xlim([0, 20])
plt.savefig('results/path_length_distribution.pdf')
plt.close()
