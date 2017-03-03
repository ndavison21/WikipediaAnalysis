import pylab as plt

hist_1000 = dict()
with open("results/separation_1000.txt", "r") as f_1000:
	for line in f_1000.readlines()
		key, num, prob = (line.rstrip('\n')).split(' ')
		hist_1000[int(key)] = int(prob)
print hist_1000

hist_3000 = dict()
with open("results/separation_3000.txt", "r") as f_3000:
	for line in f_3000.readlines()
		key, num, prob = (line.rstrip('\n')).split(' ')
		hist_1000[int(key)] = int(prob)

print "Drawing Path Length Distributions"
plt.figure()
plt.grid('True')
plt.plot(hist_1000.keys(), hist_1000.values(), 'rx-')
plt.plot(hist_3000.keys(), hist_3000.values(), 'rx-')
plt.xlabel('Path Length')
plt.ylabel('Proportion')
plt.xlim([0, 10])
plt.savefig('results/path_length_distribution.pdf')
plt.close()
