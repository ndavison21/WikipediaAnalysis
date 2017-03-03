import pylab as plt

path_sum = 0
mean = 0
hist = dict()
hist_num = dict()

with open("data/separation_full.txt", "r") as f:
    for line in f.readlines():
        key, num, prob = (line.rstrip('\n')).split(' ')
        hist[int(key)] = float(prob)
        hist_num[int(key)] = int(num)
        mean += int(key) * float(prob)
        path_sum += int(num)

with open ("results/separation.txt", "w+") as fp:
    fp.write("Number of Paths: {}\n".format(path_sum))
    fp.write("Mean Path Length: {}\n".format(mean))

    path_90 = 0.9*path_sum
    sum_path = path_sum

    for i in range(0, 17):
        if sum_path > path_90:
            sum_path -= hist_num[i]
        else:
            di = float(path_90 - sum_path) / (hist_num[i] - hist_num[i+1])
            fp.write("Effective Diameter: {}\n".format(i + di))
            break


    path_proportion = 0
    for i in range(0,8):
        path_proportion += hist_num[i]
        if i == 4:
            fp.write("Proportion of Paths 4 or shorter {}\n".format(float(path_proportion)/path_sum))
        elif i == 5:
            fp.write("Proportion of Paths 5 or shorter {}\n".format(float(path_proportion)/path_sum))
        elif i == 6:
            fp.write("Proportion of Paths 6 or shorter {}\n".format(float(path_proportion)/path_sum))
        elif i == 7:
            fp.write("Proportion of Paths 7 or shorter {}\n".format(float(path_proportion)/path_sum))



# print "Drawing Path Length Distribution"
# plt.figure()
# plt.grid(True)
# plt.plot(hist.keys(), hist.values(), 'ro-')
# plt.xlabel('Path Length')
# plt.ylabel('Proportion')
# plt.xlim([0, max(hist.keys())])
# plt.savefig('results/path_length_distribution.pdf')
# plt.close()
