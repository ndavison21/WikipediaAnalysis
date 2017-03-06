print "Importing Libraries"

import networkx as nx
import numpy as np
from scipy import optimize
import sys

def get_top_keys(dictionary, top):
    min_node = -1
    min_value = sys.maxint
    top = dict()
    for (n, b) in dictionary.iteritems():
        if len(top) < 20:
            top[n] = b
            if b < min_value:
                min_node = n
                min_value = b
        elif b > min_value:
            del top[min_node]
            top[n] = b
            min_value = sys.maxint
            for (m, c) in top.iteritems():
                if c < min_value:
                    min_node = m
                    min_value = c

    items = sorted(top.iteritems(), key=lambda (k,v): (v,k), reverse=True)

    return items

print "Reading in Graph."
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported, analysing and plotting node degrees."

in_degrees = g.in_degree()
in_values = sorted(set(in_degrees.values()))
in_hist = [in_degrees.values().count(x) for x in in_values]

out_degrees = g.out_degree()
out_values = sorted(set(out_degrees.values()))
out_hist = [out_degrees.values().count(x) for x in out_values]
max_degree = max(max(in_values), max(out_values))


powerlaw = lambda x, amp, index: amp * (x**index)

in_values[0] = 1
out_values[0] = 1
log_in_values = np.log10(in_values)
log_in_hist = np.log10(in_hist)
log_out_values = np.log10(out_values)
log_out_hist = np.log10(out_hist)


fitfunc = lambda p, x: p[0] + p[1] * x
errfunc = lambda p, x, y: (y - fitfunc(p, x))
                               
pinit = [1.0, -1.0]
in_fit = optimize.leastsq(errfunc, pinit,
                       args=(log_in_values, log_in_hist), full_output=1)
out_fit = optimize.leastsq(errfunc, pinit,
                       args=(log_out_values, log_out_hist), full_output=1)

in_pfinal = in_fit[0]
in_covar = in_fit[1]
out_pfinal = out_fit[0]
out_covar = out_fit[1]

in_index = in_pfinal[1]
in_amp = 10.0**in_pfinal[0]
out_index = out_pfinal[1]
out_amp = 10.0**out_pfinal[0]


i = 0
for v in in_values:
  if v >= 1000:
      break
  i = i + 1

o = 0
for v in out_values:
  if v >= 1000:
      break
  o = o + 1

pinit = [1.0, -1.0]
in_fit_1000 = optimize.leastsq(errfunc, pinit,
                       args=(log_in_values[:i], log_in_hist[:i]), full_output=1)
out_fit_1000 = optimize.leastsq(errfunc, pinit,
                       args=(log_out_values[:o], log_out_hist[:o]), full_output=1)

in_pfinal_1000 = in_fit_1000[0]
in_covar_1000 = in_fit_1000[1]
out_pfinal_1000 = out_fit_1000[0]
out_covar_1000 = out_fit_1000[1]

in_index_1000 = in_pfinal_1000[1]
in_amp_1000 = 10.0**in_pfinal_1000[0]
out_index_1000 = out_pfinal_1000[1]
out_amp_1000 = 10.0**out_pfinal_1000[0]


with open("results/degree_analysis.txt", "w+") as file:
    file.write("Power Law Characterisitcs\n")
    file.write("in_index {}\n".format(in_index))
    file.write("in_amp {}\n".format(in_amp))

    file.write("out_index {}\n".format(out_index))
    file.write("out_amp {}\n".format(out_amp))

    file.write("Nodes with in-degree of 0: {}\n".format(in_hist[0]))
    file.write("Nodes with out-degree of 0: {}\n".format(out_hist[0]))

    file.write("\nPower Law Characterisitcs up to 1,000\n")
    file.write("in_index_1000 {}\n".format(in_index_1000))
    file.write("in_amp_1000 {}\n".format(in_amp_1000))

    file.write("out_index_1000 {}\n".format(out_index_1000))
    file.write("out_amp_1000 {}\n".format(out_amp_1000))


    print "Getting top 20 Nodes"

    file.write("\nTop 20 Nodes by In-degree\n")
    file.write("Node, In-Degree, Out-Degree\n")
    for n,p in get_top_keys(in_degrees, 20):
      file.write("{} {} {}\n".format(n, p, out_degrees[n]))

    file.write("\nTop 20 Nodes by Out-degree\n")
    file.write("Node, Out-Degree, In-Degree\n")
    for n,p in get_top_keys(out_degrees, 20):
      file.write("{} {} {}\n".format(n, p, in_degrees[n]))


print "Drawing Degree Distributions (log scale with line to fit)"
plt.figure()
plt.grid(True)
plt.loglog(in_values, powerlaw(in_values, in_amp, in_index),'r-')
plt.loglog(in_values, in_hist, 'ro')
plt.xlabel('In-Degree')
plt.ylabel('Number of Nodes')
plt.xlim([0, max_degree])
plt.savefig('results/fit_log_in-degree_distribution.pdf')
plt.close()

plt.figure()
plt.grid(True)
plt.loglog(out_values, powerlaw(out_values, out_amp, out_index),'b-')
plt.loglog(out_values, out_hist, 'bo')
plt.xlabel('Out-Degree')
plt.ylabel('Number of Nodes')
plt.xlim([0, max_degree])
plt.savefig('results/fit_log_out-degree_distribution.pdf')
plt.close()

print "Drawing Degree Distributions (log scale with line to fit up to 1000)"
plt.figure()
plt.grid(True)
plt.loglog(in_values, powerlaw(in_values, in_amp_1000, in_index_1000),'r-')
plt.loglog(in_values, in_hist, 'ro')
plt.xlabel('In-Degree')
plt.ylabel('Number of Nodes')
plt.xlim([0, max_degree])
plt.savefig('results/fit_1000_log_in-degree_distribution.pdf')
plt.close()

plt.figure()
plt.grid(True)
plt.loglog(out_values, powerlaw(out_values, out_amp_1000, out_index_1000),'b-')
plt.loglog(out_values, out_hist, 'bo')
plt.xlabel('Out-Degree')
plt.ylabel('Number of Nodes')
plt.xlim([0, max_degree])
plt.savefig('results/fit_1000_log_out-degree_distribution.pdf')
plt.close()

print "We Done Here."
