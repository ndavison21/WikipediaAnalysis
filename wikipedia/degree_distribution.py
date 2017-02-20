# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:50:49 2017

@author: Nathanael
"""
print "Importing Libraries"

import networkx as nx
import pylab as plt
import numpy as np
from scipy import optimize

print "Reading in Graph."
g = nx.read_edgelist('data/wiki-Talk.txt', create_using=nx.DiGraph(), nodetype=int)
print "Graph Imported, analysing and plotting node degrees."

N, K = g.order(), g.size()
avg_deg = float(K) / N
# 
# print "Nodes: ", N
# print "Edges: ", K
# print "Average Degree: ", avg_deg

in_degrees = g.in_degree()
in_values = sorted(set(in_degrees.values()))
in_hist = [in_degrees.values().count(x) for x in in_values]

out_degrees = g.out_degree()
out_values = sorted(set(out_degrees.values()))
out_hist = [out_degrees.values().count(x) for x in out_values]
max_degree = max(max(in_values), max(out_values))

print "Drawing Degree Distributions (log scale)"
plt.figure()
plt.grid(True)
plt.loglog(in_values, in_hist, 'ro-')
plt.loglog(out_values, out_hist, 'bv-')
plt.legend(['In-Degree', 'Out-Degree'])
plt.xlabel('Degree')
plt.ylabel('Number of Nodes')
plt.title('Wikipedia Talk Network')
plt.xlim([0, max_degree])
plt.savefig('results/log_degree_distribution.pdf')
plt.close()

powerlaw = lambda x, amp, index: amp * (x**index)

log_in_values = np.log10(in_values[1:])
log_in_hist = np.log10(in_hist[1:])
log_out_values = np.log10(out_values[1:])
log_out_hist = np.log10(out_hist[1:])


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

print "Drawing Degree Distributions (log scale with line to fit)"
plt.figure()
plt.grid(True)
plt.loglog(in_values, powerlaw(in_values, in_amp, in_index),'r-')
plt.loglog(out_values, powerlaw(out_values, out_amp, out_index),'b-')
plt.loglog(in_values, in_hist, 'ro')
plt.loglog(out_values, out_hist, 'bo')
plt.legend(['In-Degree', 'Out-Degree'])
plt.xlabel('Degree')
plt.ylabel('Number of Nodes')
plt.title('Degree Distribution in Wikipedia Talk Network')
plt.xlim([0, max_degree])
plt.savefig('results/fit_log_degree_distribution.pdf')
plt.close()

print "We Done Here."
