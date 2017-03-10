import pylab as plt

path_sum = 0
mean = 0
hist_num = dict()
path_mean = 0

with open("data/separation_full.txt", "r") as f:
    for line in f.readlines():
        key, num = (line.rstrip('\n')).split(' ')
        hist_num[int(key)] = int(num)
        path_mean += int(key) * int(num)
        path_sum += int(num)

path_mean = float(path_mean) / path_sum
hist_prop = dict()

with open ("results/separation.txt", "w+") as fp:
    fp.write("Number of Paths: {}\n".format(path_sum))
    fp.write("Mean Path Length: {}\n".format(path_mean))


    fp.write("\nProportions\n")
    for path in hist_num.keys():
        hist_prop[path] = float(hist_num[path])/path_sum
        fp.write("{} {}\n".format(path, float(hist_num[path])/path_sum))

    path_90 = 0.9*path_sum
    sum_path = 0

    for i in range(0, 14):
        if sum_path + hist_num[i] < path_90:
            sum_path += hist_num[i]
        else:

            di = float(path_90 - sum_path) / (hist_num[i-1] - hist_num[i])
            print i
            print di
            fp.write("\nEffective Diameter: {}\n\n".format(i - 1 + di))
            break


    path_proportion = 0
    for i in range(0,14):
        path_proportion += hist_num[i]
        fp.write("Proportion of Paths {} or shorter {}\n".format(i, float(path_proportion)/path_sum))

print "Drawing Path Length Distribution"
plt.figure()
plt.grid(True)
plt.plot(hist_prop.keys(), hist_prop.values(), 'ro-')
plt.xlabel('Path Length')
plt.ylabel('Proportion')
plt.xlim([0, max(hist_prop.keys())])
plt.savefig('results/figures/path_length_distribution.pdf')
plt.close()
