
# from __future__ import division
# import commands
# import os
# import sys
import numpy
from numpy import array, zeros
import math
from math import exp as math_exp, log as math_log
# from operator import itemgetter
# import cPickle
# import matplotlib
# import matplotlib.pyplot as plt
# import scipy.stats as stats

# python /home/mbsmith/repos/GenTools/util.py

# to plot discriminating otus on itol use: beagle --> /home/mbsmith/alm/atr/src/tree.py

########################        Declare Input Files        ########################
genomes2domains = '/home/mbsmith/fxn/maps/genomes2domains.map'
genomes2orfs = '/home/mbsmith/fxn/maps/genomes2orfs.map'
orf2annotation_in = '/home/mbsmith/fxn/maps/orf2annotation.map'
genome_dict = '/home/mbsmith/fxn/maps/old2newgenome.map'


########################    Initialize Data Objects        ########################    
genomes = []
genome2domain = {}


########################    Define Genome Sub-routines    ########################

def log_txt_file(infile,outfile,base = 10):
    d = file2dict(infile)
    #pseudocount by columns:
    for k1 in d:
        for k2 in d[k1]:
            try:
                f = float(d[k1][k2])
            except ValueError:
                print 'error', d[k1][k2]        
            
    for k1 in d:
        for k2 in d[k1]:
            print float(d[k1][k2])
            d[k1][k2] = math.log(float(d[k1][k2]),base)
    label = 'base_' + str(base)
    print_uneven_2D_matrix(d, outfile, label)
    return()

def prune(otu_list,in_tree,pruned_tree):
    import dendropy
    if in_tree == 'default':
        in_tree = '/home/mbsmith/alm/atr/tree/tree.newick'
    tree = dendropy.Tree.get_from_path(in_tree, 'newick')
    tree.retain_taxa_with_labels(otu_list)
    tree.write_to_path(pruned_tree, 'newick')

def prune_with(otu_list,in_tree,pruned_tree):
    import dendropy
    if in_tree == 'default':
        in_tree = '/home/mbsmith/alm/atr/tree/tree.newick'
    tree = dendropy.Tree.get_from_path(in_tree, 'newick')
    tree.prune_taxa_with_labels(otu_list)
    tree.write_to_path(pruned_tree, 'newick')

def discriminating_otu(samples1,samples2,otu2sample2frac,otu2lin,sample1_label,sample2_label,p_cut,out_file):
    import scipy.stats as stats
    import numpy as np
    otu_list = []
    out = open(out_file, 'w')
    for otu in otu2sample2frac:
        s1 = [] #list of fracs from sample 1
        s2 = []
        for sample in otu2sample2frac[otu]:
            if sample in samples1:
                s1.append(otu2sample2frac[otu][sample])
            if sample in samples2:
                s2.append(otu2sample2frac[otu][sample])
        if not s1 == s2:
            u, p = stats.mannwhitneyu(s1,s2)
            if p < p_cut:
                lin = otu2lin[otu]
                s1mean= np.mean(s1)
                s2mean= np.mean(s2)
                if s1mean >= s2mean:
                    first_label = sample1_label
                    second_label = sample2_label
                else:
                    first_label = sample2_label
                    second_label = sample1_label
                header_line = '%s\t%s\tp = %s\n%s\n' % (first_label, otu, p, lin)
                out.write(header_line)
                out_line = '%s mean: %s\n%s mean: %s\n\n' % (sample1_label, s1mean, sample2_label, s2mean)
                out.write(out_line)
                otu_list.append(otu)
    return(otu_list)

                
         
def matrix2dict_lins(matrix):
    #assumes matrix is txt file with 1st row and 1st column as labels
    #col is first key, row is second key
    #last col has lineages
    delimiter = '\t'
    dict = {}
    otu2lin = {}
    with open(matrix, 'r') as f:
        fields = f.readline().rstrip().split(delimiter)
        corner = fields[0] #label in upper corner
        col_labels = fields[1:-1]
    for col in col_labels:
        dict[col] = {}
    
    for line in open(matrix, 'r'):
        if not line.startswith(corner):
            fields = line.rstrip().split(delimiter)
            row_label = fields[0]
            values = fields[1:-1]
            lin = fields[-1]
            otu2lin[row_label] = lin
            for i in range(0,len(values)):
                col = col_labels[i]
                value = float(values[i])
                dict[col][row_label] = value
    return(dict,otu2lin)     


def matrix2dict_transpose(matrix):
    #assumes matrix is txt file with 1st row and 1st column as labels
    #col is first key, row is second key
    delimiter = '\t'
    dict = {}
    with open(matrix, 'r') as f:
        first_line = f.readline()
        fields = first_line.rstrip().split(delimiter)
        corner = fields[0] #label in upper corner
        col_labels = fields[1:]
    for col in col_labels:
        dict[col] = {}
    
    for line in open(matrix, 'r'):
        if line != first_line:
            fields = line.rstrip().split(delimiter)
            row_label = fields[0]
            values = fields[1:]
            for i in range(0,len(values)):
                col = col_labels[i]
                try:
                    value = float(values[i])
                except ValueError:
                    value = values[i]
                dict[col][row_label] = value
    return transpose_dictionary(dict)

def matrix2dict(matrix):
    #assumes matrix is txt file with 1st row and 1st column as labels
    #col is first key, row is second key
    delimiter = '\t'
    dict = {}
    with open(matrix, 'r') as f:
        first_line = f.readline()
        fields = first_line.rstrip().split(delimiter)
        corner = fields[0] #label in upper corner
        col_labels = fields[1:]
    for col in col_labels:
        dict[col] = {}
    
    for line in open(matrix, 'r'):
        if line != first_line:
            fields = line.rstrip().split(delimiter)
            row_label = fields[0]
            values = fields[1:]
            for i in range(0,len(values)):
                col = col_labels[i]
                try:
                    value = float(values[i])
                except ValueError:
                    value = values[i]
                dict[col][row_label] = value
    return(dict)


def plot_regression(x,y,xlabel,ylabel,title,out,return_slope = False,ylim=False,xlim=False,tick_size=15,label_size=25,define_xticks=False,define_yticks=False):
    #scatter plot
    import matplotlib.pylab as plt
    import numpy as np
    dims = [0.2,0.2,0.6,0.6]
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    x = np.array(x)
    y = np.array(y)
    fig = plt.figure()
    ax = plt.axes(dims)
    fit, residuals, rank, singular_values, rcond = np.polyfit(x,y,1,full=True)
    r = sum([d*d for d in residuals])
    r = sum(residuals)
    fit_fn = np.poly1d(fit) # fit_fn is now a function which takes in x and returns an estimate for y
    ax.plot(x,y,'o',color='#4198D9',alpha=0.5,markersize=12)
    ax.tick_params(axis='both', which='major', labelsize=tick_size)
    if define_xticks != False:
        ax.xaxis.set_ticks(define_xticks)
        locs,labels = plt.xticks()
        plt.xticks(locs, map(lambda x: "%g" % x, locs))
    if define_yticks != False:
        ax.yaxis.set_ticks(define_yticks)
        locs,labels = plt.yticks()
        plt.yticks(locs, map(lambda x: "%g" % x, locs))
                
    x_extremes = [min(x),max(x)]
    y_extremes = fit_fn(x_extremes)
    ax.plot(x_extremes, y_extremes, 'k--',linewidth=4.0,alpha = 0.4)
    slope = float(y_extremes[1] - y_extremes[0]) / float(x_extremes[1] - x_extremes[0])
    if return_slope:
        title = title + '\nSlope = %s' % slope
    ax.set_xlabel(xlabel,fontsize=label_size)
    ax.set_ylabel(ylabel,fontsize=label_size)
    ax.set_title(title)
    ax.set_frame_on(False)
    #plt.gca().axison = False
    if ylim != False:
        plt.ylim(ylim)
    if xlim != False:
        plt.xlim(xlim)
    plt.savefig(out)
    if return_slope:
        return(slope)
    plt.close("all")

def plot_lines(xs,ys,labels,xlabel,ylabel,title,out):
    #scatter plot
    import matplotlib.pylab as plt
    from mpl_toolkits.axes_grid.axislines import Subplot
    import numpy as np
    
    fig = plt.figure()
    ax = Subplot(fig, 111)
    fig.add_subplot(ax)
    for i in range(0,len(xs)):
        #assumes labels, xs and ys are all lists of same length
        ax.plot(xs[i],ys[i],'o-',label=labels[i],alpha=0.5,linewidth=8)

    plt.xlabel(xlabel,size='x-large')
    plt.ylabel(ylabel,size='x-large')
    ax.set_title(title,size='xx-large')
    plt.legend(loc='upper right',fontsize=14,frameon=False)
    ax.axis["right"].set_visible(False)
    ax.axis["top"].set_visible(False)
    
    ymax = max(max(ys))
    if ymax > 0:
        ymax = ymax * 1.05
    else:
        ymax = ymax * 0.95
    ymin = min(min(ys))
    ylim = (ymin,ymax)
    plt.ylim(ylim)
    plt.savefig(out)
    plt.close("all")

def plot_scatter(x,y,xlabel,ylabel,title,out):
    #scatter plot
    import matplotlib.pylab as plt
    import numpy as np
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    x = np.array(x)
    y = np.array(y)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x,y,'bo',alpha=1.0)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    #plt.gca().axison = False
    plt.savefig(out)
    plt.close("all")

def plot_multi_scatter(xs,ys,labels,xlabel,ylabel,title,out,colors = [],size = 50,define_xticks=False,define_yticks=False,type='png',legend=True):
    
    #scatter plot
    from matplotlib.backends.backend_pdf import PdfPages
    import matplotlib.pylab as plt
    import numpy as np
    if colors == []:
        colors = plt.rcParams['axes.color_cycle']*(int(1+len(labels)/float(7)))
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(0,len(labels)):
        x = np.array(xs[i])
        y = np.array(ys[i])
        ax.scatter(x,y,c = colors[i], s=size,label=labels[i],alpha=0.7)
    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_xlabel(xlabel,fontsize=25)
    ax.set_ylabel(ylabel,fontsize=25)
    ax.set_title(title)
    if define_xticks != False:
        ax.xaxis.set_ticks(define_xticks)
        locs,labels = plt.xticks()
        plt.xticks(locs, map(lambda x: "%g" % x, locs))
    if define_yticks != False:
        ax.yaxis.set_ticks(define_yticks)
        locs,labels = plt.yticks()
        plt.yticks(locs, map(lambda x: "%g" % x, locs))
    
    if legend:
        plt.legend(scatterpoints=1,frameon=False,fontsize=15)
    #plt.gca().axison = False
    ax.set_frame_on(False)
    if type == 'pdf':
        pp = PdfPages(out)
        pp.savefig(fig)
        pp.close()
    else:
        plt.savefig(out)
    plt.close("all")


def plot_histograms(lists,labels,title,ylabel = '',xlabel = '',out = '',bins = 50,normed=1):
    fig = plt.figure()
    plt.hist(lists, bins, label=labels, normed=normed, histtype='bar')
    plt.legend(frameon=False)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.savefig(out)
    plt.close("all")

def plot_2dhist(x,y,xlabel,ylabel,title,out):
    #scatter plot
    dims = [min(x),max(x),min(y),max(y)]
    dims = [a*1.05 for a in dims] #so points are not cut off
    import matplotlib.pylab as plt
    import numpy as np
    from matplotlib.colors import LogNorm
    x = np.array(x)
    y = np.array(y)
    plt.subplot(111)
    plt.hexbin(x,y,cmap='jet',mincnt=1,bins='log')
    plt.axis(dims)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    cb = plt.colorbar(aspect=60)
    cb.set_label('log10(counts)')
    plt.savefig(out)
    plt.close("all")

def box_plot(lists,labels,title,ylabel,color = 'b',out = '',pvals=True, rotation='horizontal',ylim = False):
    #lists is a list of distributions 
    
    matplotlib.rcParams['lines.linewidth'] = 3
    matplotlib.rcParams['lines.markeredgewidth'] = 2
    fig = plt.figure()
    if pvals:
        x = 0.25
        y = 0.08
        delta = y/len(lists)
        for i in range(0,len(lists)):
            for j in range(i+1,len(lists)):
                dist1 = lists[i]
                dist2 = lists[j]
                label1 = labels[i]
                label2 = labels[j]
                u,p = stats.mannwhitneyu(dist1,dist2)
                s = label1 + ' vs. ' + label2 + ' p = %.3e' % p
                fig.text(x,y,s)
                y -= delta
        dims = [0.1,0.2,0.8,0.7]
    else:
        dims = [0.1,0.1,0.8,0.8]        
    ax = plt.axes(dims,frameon=False)
    if ylim != False:
        ax.set_ylim(ylim)  
    ax.set_title(title)
    tick_locs = range(1,len(lists)+1)
    bp = ax.boxplot(lists,patch_artist=True)
    plt.xticks(tick_locs, labels, rotation=rotation)
    ax.set_ylabel(ylabel)

    for box in bp['boxes']:
        # change outline color
        box.set( color='#7570b3', linewidth=5)
        # change fill color
        box.set( facecolor = '#1b9e77' )
    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=5)

    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=5)

    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=5)

    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5,markersize=10)
    
        
    if out != '':
        fig.savefig(out)
   
def bar_plot(lists,labels,title,ylabel,out = '',yerr = False,significance = [],ylim=False,legend_string='',colors='#FF0000'):
    #lists is a list of distributions
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.stats as stats
    fig = plt.figure()
    dims = [0.1,0.3,0.8,0.6]
    box = plt.axes(dims,frameon=False)
    box.set_title(title)
    ind = range(1,len(lists)+1)
    if type(lists[0]) == list:
        heights = [np.mean(l) for l in lists]
    else:
        heights = lists
    width = 0.8
    if yerr:
        yerr_neg = np.zeros(len(lists))
        yerr_pos = [stats.sem(l) for l in lists]
        yerrs = [yerr_neg,yerr_pos]
        rects = box.bar(ind,heights,width=width, bottom = 0, yerr=yerrs,color = 'k', ecolor='gray')
    else:
        rects = box.bar(ind,heights,width=width, bottom = 0,alpha = 0.8,color='#4198D9')        
    if significance != []:
        for i in range(0,len(rects)):
            sig = significance[i]
            rect = rects[i]
            if sig < 0.0001:
                box.plot(rect.get_x()+rect.get_width()/2.0,(rect.get_height()+(max(heights)*0.025)),'ko',alpha = 0.6)
            elif sig < 0.01:
                box.plot(rect.get_x()+rect.get_width()/2.0,(rect.get_height()+(max(heights)*0.025)),'wo')
    tick_locs = [x + width/2.0 for x in ind]
    plt.xticks(tick_locs, labels,rotation='vertical',size='small')
    box.set_ylabel(ylabel,fontsize=24)
    box.tick_params(axis='both', which='major', labelsize=15)
    if legend_string != '':
        props = dict(boxstyle='round', facecolor='white', alpha=0.0,linewidth=2)
        box.text(0.025,0.95,legend_string,transform=box.transAxes, fontsize=14,verticalalignment='top', bbox=props)
    if ylim != False:
        plt.ylim(ylim)
    if out != '':
        fig.savefig(out)

def multi_bar_plot(lists,labels,types,title,ylabel,color_dict = {}, out = '',xlabel=''):
    #lists is a list of lists
    #first dimension contains types (e.g. algorithm to perform classification)
    #second dimension contains examples (e.g. target to be predicted)
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.stats as stats

    
    colors = ['r','b','g','o','k']  
    fig = plt.figure()
    dims = [0.1,0.3,0.8,0.6]
    box = plt.axes(dims)
    box.set_frame_on(False)
    box.set_title(title)
    ind = range(1,len(labels)+1)
    width = 0.8/len(types)
    legend_objects = []
    for i in range(0,len(types)):
        heights = lists[i]
        indices = [index+(width*i) for index in ind]
        if color_dict != {}:
            c = color_dict[types[i]]
        else:
            c = colors[i%5]
        rects = box.bar(indices,heights,width=width, color = c, bottom = 0)
        legend_objects.append(rects[0])    
    tick_locs = [x + width/2.0 for x in ind]
    plt.xticks(tick_locs, labels,rotation='horizontal',size='small')
    box.set_ylabel(ylabel)
    box.set_xlabel(xlabel)
    plt.legend(legend_objects,types,frameon=False)
    if out != '':
        fig.savefig(out)


def nonzero(values):
    minimum = 1
    for v in values:
        v = float(v)
        if v > 0 and v < minimum:
            minimum = v
    return(minimum)

def replace_nonzeros(list):
    minimum = nonzero(list)
    for i in range(len(list)):
        if float(list[i]) < minimum:
            list[i] = minimum
        else:
            list[i] = float(list[i])
    return(list)

def remove_dual_nonzeros(list1,list2):
    new1 = []
    new2 = []
    #lists must be same length
    #removes all items with non-zero values
    for i in range(0,len(list1)):
        if float(list1[i]) != 0 and float(list2[i]) != 0:
            new1.append(list1[i])
            new2.append(list2[i])
    return(new1,new2)

def sort_lists(lists):
    #return lists sorted by items in 1st column in list
    tuples = []
    for i in range(0,len(lists[0])): #for each item
        t = ()
        for j in range(0,len(lists)): #for each list
            t += lists[j][i],
        tuples.append(t)
    tuples.sort()
    sorted = []
    for i in range(0,len(lists)):
        sorted.append([])
    for t in tuples:
        for i in range(0,len(t)):
            item = t[i]
            sorted[i].append(item)
    return(sorted)
    
    
        
def float_it(dict):
    #takes a dict of dicts
    for k1 in dict:
        for k2 in dict[k1]:
            try:
                dict[k1][k2] = float(dict[k1][k2])
            except ValueError:
                pass
    return(dict)

def standardize_matrix(matrix,out = ''):
    #return a matrix as a z-score dictionary (standardizing by columns)
    import numpy as np
    d = matrix2dict(matrix)
    d = float_it(d)
    zs = {}
    for col in d:
        zs[col] = {}
        floats = [v for v in d[col].values() if type(v) is float]
        mean = np.mean(floats)
        std = np.std(floats)
        for row in d[col]:
            v = d[col][row]
            try:
                z = (v - mean) / float(std)
            except TypeError:
                z = v
            zs[col][row] = z
    if out != '':
        print_uneven_2D_matrix(zs, out, 'Standardized')
    return(zs)

def normalize_dict(dict,normalize_1st_or_2nd):
    normal = {}
    if normalize_1st_or_2nd == 1:
        #normalize the dictionary relative to its first dimension
        for key1 in dict:
            #determine the total for each key 
            total = 0
            for key2 in dict[key1]:
                total += dict[key1][key2]
            
            #compute and store normalized values for each key
            normal[key1] = {}
            for key2 in dict[key1]:
                normal[key1][key2] = float(dict[key1][key2]) / float(total)
    
    elif normalize_1st_or_2nd == 2:
        #normalize the dictionary relative to its second dimension
        
        #determine the total for each 2nd dimension key
        key2_tots = {}
        for key1 in dict:
            for key2 in dict[key1]:
                try:
                    key2_tots[key2] += dict[key1][key2]
                except KeyError:
                    key2_tots[key2] = dict[key1][key2]
        #compute and store the normalized values
        for key1 in dict:
            normal[key1] = {}
            for key2 in dict[key1]:
                normal[key1][key2] = float(dict[key1][key2]) / float(key2_tots[key2])
    else:
        print 'normalization error, must pick 1 or 2 as the dimension to normalize by'
    return(normal) 

def filter_otu_table(dict,min_samples,min_counts):
    sample_list = dict.keys()
    filtered = {}
    for sample in dict:
        filtered[sample] = {}
    for otu in dict[sample_list[0]]:
        counts = 0
        samples = 0
        for sample in sample_list:
            val = dict[sample][otu]
            counts += val
            if val > 0:
                samples += 1
        if counts >= min_counts and samples >= min_samples:
            #add to filtered dict
            for sample in sample_list:
                filtered[sample][otu] = dict[sample][otu]
    return(filtered)

def filtered_otu_table(count_file,min_counts,tax=True):
    #assumes first row has samples, all other rows are otus
    #assumes first element in sample column ignored
    #rows are OTUS, columns are samples
    #assumes no taxonomic data after the otu file
    
    
    f = open(count_file,'r')
    first = f.readline()
    if tax:
        samples = first.rstrip().split('\t')[1:-1]
    else:
        samples = first.rstrip().split('\t')[1:]
    tots = numpy.zeros(len(samples))
    for line in open(count_file,'r'):
        if line != first:
            if tax:
                fields = line.rstrip().split('\t')[1:-1]
                ints = [int(float(i)) for i in fields]
                tots += ints # get the total number of reads for each sample
            else:
                fields = line.rstrip().split('\t')[1:]
                ints = [int(float(i)) for i in fields]
                tots += ints # get the total number of reads for each sample
                
    filtered_samples = []
    for i in range(0,len(samples)):
        s = samples[i]
        t = tots[i]
        if t > min_counts:
            filtered_samples.append(s)
    frac_dict = {}
    for i in range(0,len(filtered_samples)):
        frac_dict[filtered_samples[i]] = {}
    for line in open(count_file,'r'):
        if line != first:
            if tax: 
                fields = line.rstrip().split('\t')[1:-1]
            else:
                fields = line.rstrip().split('\t')[1:]                
            otu = line.rstrip().split('\t')[0]
            ints = [int(float(i)) for i in fields]
            fracs = ints/tots
            for i in range(0,len(samples)):
                s = samples[i]
                if s in filtered_samples:            
                    frac_dict[s][otu] = fracs[i]
    return(frac_dict)

def filter_otu_table_pseudo_count(dict,min_samples,min_counts,detection_limit):
    sample_list = dict.keys()
    filtered = {}
    for sample in dict:
        filtered[sample] = {}
    for otu in dict[sample_list[0]]:
        counts = 0
        samples = 0
        for sample in sample_list:
            val = dict[sample][otu]
            counts += val
            if val > 0:
                samples += 1
        if counts >= min_counts and samples >= min_samples:
            #add to filtered dict
            for sample in sample_list:
                if dict[sample][otu] > 0:
                    filtered[sample][otu] = dict[sample][otu] + detection_limit
                else:
                    filtered[sample][otu] = detection_limit
    return(filtered)

def reformat_fst(in_file):
    #takes a fasta file that is formatted with newlines in the seqs and removes the newlines
    out = open((in_file + '.edit'), 'w')
    first = True
    for line in open(in_file, 'r'):
        if line.startswith('>'):
            if first == True:
                seq = ''
                header = line
                first = False
            else:
                out.write(header)
                out.write((seq + '\n'))
                header = line
                seq = ''
        else:
            seq += line.rstrip()
    
    out.write(header)
    out.write((seq + '\n'))
    out.close()
    os.system(('mv ' + in_file + '.edit ' + in_file))        
    
def chisq_from_contingency(observedTuples):
    import scipy.stats as stats
    if len(observedTuples) == 0: return None
    for row in observedTuples:
        if len(row) != len(observedTuples[0]): return None
    
    rowSums = []
    for row in observedTuples:
        rowSums.append(float(sum(row)))
        columnSums = []
        for i in range(len(observedTuples[0])):
            columnSum = 0.0
            for row in observedTuples:
                columnSum += row[i]
            columnSums.append(float(columnSum))
    
    grandTotal = float(sum(rowSums))
    observedTestStatistic = 0.0
    
    for i in range(len(observedTuples)):
        for j in range(len(row)):
            expectedValue = (rowSums[i]/grandTotal)*(columnSums[j]/grandTotal)*grandTotal
            observedValue = float(observedTuples[i][j])
            observedTestStatistic += ((observedValue - expectedValue)**2) / expectedValue
    degreesFreedom = (len(columnSums) - 1) * (len(rowSums) - 1)
    return stats.chisqprob(observedTestStatistic, degreesFreedom)    

def overlap(x,y,u,v):

    # get min/max coords
    a = min(x,y)
    b = max(x,y)
    c = min(u,v)
    d = max(u,v)

    # now enumerate cases

    # case 1: a-----b
    #            c------d
    # then: overlap = b-c
    if a <= c and c <= b and b<=d:
        return b-c+1

    # case 2:      a-----b
    #           c-----d
    # then: overlap = d-a
    elif c<=a and a<=d and d<=b:
        return d-a+1

    # case 3:
    #        a---b
    #     c---------d
    # then: overlap = b-a
    elif c<=a and b<=d:
        return b-a+1

    # case 4:
    #     a--------b
    #        c--d
    # then: overlap = d-c
    elif a<=c and d<=b:
        return d-c+1

    # case 5: no overlap
    else:
        return 0

def overlap_bool(x,y,u,v):
    x = int(x)
    y = int(y)
    u = int(u)
    v = int(v) 
    
    # get min/max coords
    a = min(x,y)
    b = max(x,y)
    c = min(u,v)
    d = max(u,v)
    # now enumerate cases

    # case 1: a-----b
    #            c------d
    # then: overlap = b-c
    if a <= c and c <= b and b<=d:
        return True

    # case 2:      a-----b
    #           c-----d
    # then: overlap = d-a
    elif c<=a and a<=d and d<=b:
        return True

    # case 3:
    #        a---b
    #     c---------d
    # then: overlap = b-a
    elif c<=a and b<=d:
        return True

    # case 4:
    #     a--------b
    #        c--d
    # then: overlap = d-c
    elif a<=c and d<=b:
        return True

    # case 5: no overlap
    else:
        return False

def overlap_bool_coords(c1,c2):
    
    
    
    # get min/max coords
    a = int(min(c1))
    b = int(max(c1))
    c = int(min(c2))
    d = int(max(c2))

    # now enumerate cases

    # case 1: a-----b
    #            c------d
    # then: overlap = b-c
    if a <= c and c <= b and b<=d:
        return True

    # case 2:      a-----b
    #           c-----d
    # then: overlap = d-a
    elif c<=a and a<=d and d<=b:
        return True

    # case 3:
    #        a---b
    #     c---------d
    # then: overlap = b-a
    elif c<=a and b<=d:
        return True

    # case 4:
    #     a--------b
    #        c--d
    # then: overlap = d-c
    elif a<=c and d<=b:
        return True

    # case 5: no overlap
    else:
        return False

def fromPickle(file):
    handle = open(file, 'r')
    data = cPickle.load(handle)
    handle.close()
    return(data)

def parse_metadata(label,file):

    genome2metadata = {}
    header = open(file).readline().rstrip('\n').split('\t')
    j = header.index(label)
    for line in open(file):
        if line.startswith('\t'):
            continue
        line = line.rstrip('\n').split('\t')
        genome_i = line[0]
        meta_i = line[j]
        genome2metadata[genome_i] = meta_i
    return genome2metadata

def file2dict(file):
    #assumes the file is a symmetric 2-d array starting with a tab in top left corner
    dict = {}
    header = open(file).readline().rstrip('\n').split('\t')[1:]
    for h in header:
        dict[h] = {}
    for line in open(file):
        if line.startswith('\t'):
            continue
        header2 = line.rstrip('\n').split('\t')[0]
        fields = line.rstrip('\n').split('\t')[1:]
        for i in range(0,len(fields)):
            dict[header[i]][header2] = fields[i]  
    return(dict)

def psuedo_count(list):
    for i in list:
        if i == 0:
            i = 1e-50
    return(list)

def log(x):
    if x < 1e-10:
        return 0.0
    else:
        return math_log(x)

def kl_divergence(p, q):
    #source: https://bitbucket.org/timv/python-extras/src/184a4680fa34/maths/maths.py
    """ Compute KL divergence of two vectors, K(p || q).
    NOTE: If any value in q is 0.0 then the KL-divergence is infinite.
    """
    log_of_2 = math.log(2)
    assert len(p) == len(q)
    kl = sum(p[i] * log(p[i] / q[i]) for i in xrange(len(p)) if p[i] != 0.0)
    return kl / log_of_2

def weighted_kl_divergence(p, q, w):
    #w is a weight vector that indicates the relative weight to place on each item in p and q
    #source: https://bitbucket.org/timv/python-extras/src/184a4680fa34/maths/maths.py
    """ Compute KL divergence of two vectors, K(p || q).
    NOTE: If any value in q is 0.0 then the KL-divergence is infinite.
    """
    log_of_2 = math.log(2)
    assert len(p) == len(q)
    kl = 0
    for i in xrange(len(p)):
        if p[i] != 0.0:
            s = w[i] * p[i] * log(p[i] / q[i])
            #print s
            kl += s
    return kl / log_of_2

def jensen_shannon_from_dict(p, q):
    """ 
    p = {'species': count}, q = {'species': count}
    Returns the Jensen-Shannon divergence from two dictionaries of distributions mapped to the same keys
    note, this function normalizes all counts to fractions for you"""
    pkeys = p.keys()
    qkeys = q.keys()
    pkeys.sort()
    qkeys.sort()
    if pkeys != qkeys:
        print 'keys do not map onto each other perfectly in util.jensen_shannon_from_dict'
    else:
        qsum = sum(q.values())
        psum = sum(p.values())
        qnew = []
        pnew = []
        for k in pkeys:
            qnew.append(q[k]/qsum)
            pnew.append(p[k]/psum)
        p = pnew
        q = qnew
        jsd = jensen_shannon_divergence(p, q, True)
        return(jsd)

def jensen_shannon_from_dict_weighted(p,q,w_in):
    pkeys = p.keys()
    qkeys = q.keys()
    pkeys.sort()
    qkeys.sort()
    if len(w_in)/float(len(pkeys)) < 0.10:
        print 'less than 10% of features have weights assigned'
    w = {}
    for key in qkeys:
        try:
            w[key] = float(w_in[key])
        except KeyError: #there was no weight for this key
            w[key] = 0
       
    if pkeys != qkeys:
        print 'keys do not map onto each other perfectly in util.jensen_shannon_from_dict'
    else:
        qsum = sum(q.values())
        psum = sum(p.values())
        qnew = []
        pnew = []
        wnew = []
        for k in pkeys:
            qnew.append(q[k]/qsum)
            pnew.append(p[k]/psum)
            wnew.append(w[k])
        p = pnew
        q = qnew
        w = wnew
        jsd = jensen_shannon_divergence_weighted(p, q, w, True)
        return(jsd)

def jensen_shannon_divergence(p, q, psuedo_count_true):
    """ Returns the Jensen-Shannon divergence.
    distributions must be normalized to fractions!!!! """
    if psuedo_count_true == True:
        p = psuedo_count(p)
        q = psuedo_count(q)
    
    assert len(p) == len(q)
    average = zeros(len(p))
    for i in xrange(len(p)):
        average[i] += (p[i] + q[i]) / 2.0
    return ((kl_divergence(p, average) + kl_divergence(q, average)) / 2.0)

def jensen_shannon_divergence_weighted(p, q, w, psuedo_count_true):
    """ Returns the Jensen-Shannon divergence.
    distributions must be normalized to fractions!!!! """
    if psuedo_count_true == True:
        p = psuedo_count(p)
        q = psuedo_count(q)
    
    assert len(p) == len(q)
    average = zeros(len(p))
    for i in xrange(len(p)):
        average[i] += (p[i] + q[i]) / 2.0
    return ((weighted_kl_divergence(p, average, w) + weighted_kl_divergence(q, average, w)) / 2.0)


def otus2jsd(otu_file,jsd_pickle, lins = False):
    if lins:
        dict, lins = get_fractions_and_lins(otu_file)
    else:
        dict = matrix2dict(otu_file)
    #assumes matrix is txt file with 1st row and 1st column as labels
    #col is first key, row is second key
    #assumes samples are col labels (use transpose if this is not the case)
    
    jsd_dict = {}
    for s1 in dict:
        jsd_dict[s1] = {}
        for s2 in dict:
            if s1 == s2:
                jsd = 0
            else:
                jsd = jensen_shannon_from_dict(dict[s1], dict[s2])
            jsd_dict[s1][s2] = jsd
    out = open(jsd_pickle, 'w')
    cPickle.dump(jsd_dict,out)
    out.close()
    if lins:
        return(lins,jsd_dict)
    else:
        return(jsd_dict)


def otus2jsd_weighted(otu_file,jsd_pickle,weight_dict):
    dict = matrix2dict(otu_file)
    #assumes matrix is txt file with 1st row and 1st column as labels
    #col is first key, row is second key
    #assumes samples are col labels (use transpose if this is not the case)
    #weight dict is a dictionary of weights to apply to an item in the vector (ie feature importance)
    #if no weight supplied, will weight a feature to zero
    
    jsd_dict = {}
    for s1 in dict:
        jsd_dict[s1] = {}
        for s2 in dict:
            if s1 == s2:
                jsd = 0
            else:
                jsd = jensen_shannon_from_dict_weighted(dict[s1], dict[s2],weight_dict)
            jsd_dict[s1][s2] = jsd
    out = open(jsd_pickle, 'w')
    cPickle.dump(jsd_dict,out)
    out.close()
    return(jsd_dict)


def within_vs_btw(dict,gp1,gp2):
    #gp1 and gp2 are lists of samples in each group
    #dict must be a 2D dictionary where the items (samples) in gp1 and gp2 are keys
    
    #within gp1
    gp1_dlist = []
    for i in range(0,len(gp1)):
        for j in range(i+1,len(gp1)):
            d = dict[gp1[i]][gp1[j]]
            gp1_dlist.append(d)
    
    #within gp2
    gp2_dlist = []
    for i in range(0,len(gp2)):
        for j in range(i+1,len(gp2)):
            d = dict[gp2[i]][gp2[j]]
            gp2_dlist.append(d)
    
    #btw_groups
    btw_dlist = []
    for s1 in gp1:
        for s2 in gp2:
            d = dict[s1][s2]
            btw_dlist.append(d)
    return(gp1_dlist,gp2_dlist,btw_dlist)
    
def chao1(data):
    ones = 0
    twos = 0
    non_zero = 0
    for num in data:
        num = int(num)
        if num > 0:
            non_zero += 1
        if num == 1:
            ones += 1
        if num == 2:
            twos += 1
    observed = non_zero
    top = ones * (ones -1)
    bot = 2 * (twos + 1)
    inferred = top / float(bot)
    total = observed + inferred
    return(total)        

def sdi(data):
    """ Given a hash { 'species': count } , returns the SDI Shannon Diversity Index
    
    >>> sdi({'a': 10, 'b': 20, 'c': 30,})
    1.0114042647073518"""
    
    from math import log as ln
    
    def p(n, N):
        """ Relative abundance """
        if n == 0 or n == 'NA':
            return 0
        else:
            return (float(n)/N) * ln(float(n)/N)
            
    N = sum([float(d) for d in data.values() if d != 'NA'])
    div = -sum(p(n, N) for n in data.values())
    return(div)

def simpson_list(data):
    """ Given a list [count,count,count] , returns the Simpson Diversity Index
    
    >>> simpson_list([10,20,30])
    1.0114042647073518"""
        
    def p(n, N):
        """ Relative abundance """
        if n == 0:
            return 0
        else:
            return (float(n)/N)**2
    try:       
        N = sum(data)
    except TypeError:
        data = [float(x) for x in data]
        N = sum(data)
    return sum(p(n, N) for n in data if n > 0)


def sdi_list(data):
    """ Given a list [count,count,count] , returns the SDI Shannon Diversity Index
    
    >>> sdi_list([10,20,30])
    1.0114042647073518"""
    
    from math import log as ln
    
    def p(n, N):
        """ Relative abundance """
        if n == 0:
            return 0
        else:
            return (float(n)/N) * ln(float(n)/N)
    try:       
        N = sum(data)
    except TypeError:
        data = [float(x) for x in data]
        N = sum(data)
    return -sum(p(n, N) for n in data if n > 0)


def make_dir(dir):
    if not os.path.exists(dir):
        os.system('mkdir %s' % dir)
    return(dir)

def make_list(dir):
    list = []
    command = 'ls ' + dir
    i = os.popen(command)
    for line in i:
        line = line.rstrip()
        list.append(line)
    return list

def file2list(file):
    #file is seperated by newlines
    list = []
    i = open(file, 'r')
    for line in i:
        item = line.rstrip()
        list.append(item)
    return list

    
def blast_best(report, rank_type, output_type):
    #FIND BEST BLAST HIT BETWEEN SEQUENCE IDENTIFIERS
    #takes in the 
    #parses the report into a two-dimensionsal dictionary
    #the keys are 1) the query ID 2) the subject ID
    #the stored value is given by the output parameter
    #parameters:     1) beagle full location of a blast (m-8) report
    #                2) metric to rank hits by ('evalue', 'length', 'bitscore', 'ID')
    #                3) metric to output ('evalue', 'length', 'bitscore', 'ID')
    
    #initialize the 2-d hash of best hits
    rank_dict = {}
    out_dict = {}
    min_len = 500
    
    i = open(report, 'r')
    for line in i:
        #parse the blast report and save the rank and out values for each entry
        array = line.rstrip().split('\t')
        q = array[0]
        s = array[1]
        id = float(array[2])
        len = int(array[3])
        mismatch = int(array[4])
        gap_opens = int(array[5])
        qb = int(array[6]) #query begin
        qe = int(array[7]) #query end
        sb = int(array[8])
        se = int(array[9])
        eval = array[10]
        bit = int(array[11])
        
        if rank_type == 'evalue':
        #need to take inverse of evalue so that higher values are more desirable for ranking
            if eval == 0:
                rank = 1e308 #special case where e-value is zero
            else:
                rank = 1/float(eval)
        elif rank_type == 'length':
            rank = len
            
        elif rank_type == 'bitscore':
            rank = bit
        
        elif rank_type == 'ID':
            rank = id
        
        else:
            print 'Error, invalid rank parameter'
        
        if output_type == 'evalue':
            out = eval
            
        elif output_type == 'length':
            out = len            
        
        elif output_type == 'bitscore':
            out = bit
        
        elif output_type == 'ID':
            out = id
        
        else:
            print 'Error, invalid output type parameter'
        out = float(out)
        rank = float(rank)
        #find the best 'rank' value and save the best 'out' value for each pair of q and s (query and subject identifiers)        
        if s in rank_dict.keys(): #s exists, see if q needs to be added
            if q in rank_dict[s].keys(): #both s and q exist, need to check value
                value = rank_dict[s][q] 
                if rank > value and len > min_len: #s and q exist and new rank value exceeds best of old
                    rank_dict[s][q] = rank
                    out_dict[s][q] = out
                else: #s and q exist, but old rank value is better than new one so keep the old value
                    pass
            elif len > min_len:  #s exists but q does not, this value is the best by default
                rank_dict[s][q] = rank
                out_dict[s][q] = out
            else:
                pass

        elif len > min_len: # both s and q need to be added, this value is the best by default
            rank_dict[s] = {}
            rank_dict[s][q] = rank
            out_dict[s] = {}
            out_dict[s][q] = out
        else:
            pass
            
    return(out_dict)        

def blast_16s(fasta_location):
    green_genes = '/home/mbsmith/alm/Fiji/predict_hgt/green_genes.fst'
    report = fasta_location + '.greengenes.blastn'
    green_genes1 = '/home/mbsmith/alm/Fiji/predict_hgt/green_genes1.fst'
    report1 = fasta_location + '.greengenes1.blastn'
    green_genes2 = '/home/mbsmith/alm/Fiji/predict_hgt/green_genes2.fst'
    report2 = fasta_location + '.greengenes2.blastn'
    blast_cmd = '/opt/Bio/ncbi/bin/blastall -p blastn -d %s -i %s -o %s -m 8 -e 1e-50' % (green_genes,fasta_location,report)
    usearch_cmd = '/home/csmillie/bin/usearch --db %s --query %s --blast6out %s --evalue 0.00001 --maxaccepts 1 --maxtargets 100 --maxrejects 100 --maxlen 10000000' % (green_genes1,fasta_location,report1)
    #os.system(usearch_cmd)
    usearch_cmd = '/home/csmillie/bin/usearch --db %s --query %s --blast6out %s --evalue 0.00001 --maxaccepts 1 --maxtargets 100 --maxrejects 100 --maxlen 10000000' % (green_genes2,fasta_location,report2)
    #os.system(usearch_cmd)
    cat = 'cat %s %s > %s' % (report1,report2,report)
    os.system(cat)
    rank_type = 'bitscore'
    output_type = 'ID'
    dict = blast_best(report, rank_type, output_type)
    pickled_report = report + '.pickle'
    out = open(pickled_report,'w')
    cPickle.dump(dict,out)
    out.close()
    return(dict)

#dict = blast_best('/home/mbsmith/Fiji/predict_hgt/full_16s.blastn', 'bitscore', 'ID')    

def get_fractions(count_file):
    #assumes first row has samples, all other rows are otus
    #assumes first element in sample column ignored
    #rows are OTUS, columns are samples
    #assumes no taxonomic data after the otu file
    
    f = open(count_file,'r')
    first = f.readline()
    samples = first.rstrip().split('\t')[1:]
    frac_dict = {}
    for i in range(0,len(samples)):
        frac_dict[samples[i]] = {}
    tots = numpy.zeros(len(samples))
    for line in open(count_file,'r'):
        if line != first:
            fields = line.rstrip().split('\t')[1:]
            ints = [int(float(i)) for i in fields]
            tots += ints # get the total number of reads for each sample
    for line in open(count_file,'r'):
        if line != first:
            fields = line.rstrip().split('\t')[1:]
            otu = line.rstrip().split('\t')[0]
            ints = [int(float(i)) for i in fields]
            fracs = ints/tots
            for i in range(0,len(samples)):
                s = samples[i]
                frac_dict[s][otu] = fracs[i]
    return(frac_dict)

def get_fractions_and_lins(count_file):
    #assumes first row has samples, all other rows are otus
    #rows are OTUS, columns are samples
    #assumes first element in sample column ignored
    #assumes taxonomic data in column after the last sample
    
    otu2lin = {}
    f = open(count_file,'r')
    samples = f.readline().split('\t')[1:-1]
    frac_dict = {}
    for i in range(0,len(samples)):
        frac_dict[samples[i]] = {}
    tots = numpy.zeros(len(samples))
    c = 0
    for line in open(count_file,'r'):
        if not line.startswith('#'):
            c += 1
            if c > 2:
                fields = line.rstrip().split('\t')[1:-1]
                ints = [int(float(i)) for i in fields]
                tots += ints # get the total number of reads for each sample
    c = 0
    for line in open(count_file,'r'):
        if not line.startswith('#'):
            c += 1
            if c > 2:
                fields = line.rstrip().split('\t')
                otu = fields.pop(0)
                lin = fields.pop(-1)
                otu2lin[otu] = lin
                ints = [int(float(i)) for i in fields]
                fracs = ints/tots
                for i in range(0,len(samples)):
                    s = samples[i]
                    frac_dict[s][otu] = fracs[i]      
    return(frac_dict,otu2lin)
    
def print_normalized_uneven_2D_matrix(dict, out_file, label, normalize_1st_or_2nd):
    #    can have different column and row labels
    #    sub_routine to print a 2D_matrix
    #    dict --> A two-dimensional dictionary.  First dimension will be rows, Second will be columns
    #    out_file --> destination to print to
    #    label --> label for the top corner of file
    
    normal = {}
    if normalize_1st_or_2nd == 1:
        #normalize the dictionary relative to its first dimension
        for key1 in dict:
            #determine the total for each key 
            total = 0
            for key2 in dict[key1]:
                total += dict[key1][key2]
            
            #compute and store normalized values for each key
            normal[key1] = {}
            for key2 in dict[key1]:
                normal[key1][key2] = float(dict[key1][key2]) / float(total)
    
    elif normalize_1st_or_2nd == 2:
        #normalize the dictionary relative to its second dimension
        
        #determine the total for each 2nd dimension key
        key2_tots = {}
        for key1 in dict:
            for key2 in dict[key1]:
                try:
                    key2_tots[key2] += dict[key1][key2]
                except KeyError:
                    key2_tots[key2] = dict[key1][key2]
        #compute and store the normalized values
        for key1 in dict:
            normal[key1] = {}
            for key2 in dict[key1]:
                normal[key1][key2] = float(dict[key1][key2]) / float(key2_tots[key2])
    
    
    else:
        print 'normalization error, must pick 1 or 2 as the dimension to normalize by'
    
    
    
    dict = normal            
    
    out = open(out_file, 'w')
    keys1 = dict.keys()
    keys1.sort()
    keys2 = []
    for key1 in keys1:
        keys2_list = dict[key1].keys()
        keys2.extend(keys2_list)
    keys2_set = set(keys2)
    keys2 = list(keys2_set)
    keys2.sort()            
    topcorner = str(label) + '\t'
    out.write(topcorner)
    
    #write the headers 
    for key1 in keys1:
        header = str(key1) + '\t'
        out.write(header)
    out.write('\n')
    
    #write the body
    for key2 in keys2:
        header = str(key2) + '\t'
        out.write(header)
        for key1 in keys1:
            if key2 in dict[key1]:
                value = dict[key1][key2]
                value = str(value) + '\t'
            else:
                value = '0\t'
            out.write(value)
        out.write('\n')
    out.close()    
    return
    
def print_uneven_2D_matrix(dict, out_file, label):
    #    can have different column and row labels
    #    sub_routine to print a 2D_matrix
    #    dict --> A two-dimensional dictionary.  First dimension will be columns, Second will be rows
    #    out_file --> destination to print to
    #    label --> label for the top corner of file
    
    out = open(out_file, 'w')
    keys1 = dict.keys()
    keys1.sort()
    keys2 = []
    for key1 in keys1:
        keys2_list = dict[key1].keys()
        keys2.extend(keys2_list)
    keys2_set = set(keys2)
    keys2 = list(keys2_set)
    keys2.sort()            
    topcorner = str(label) + '\t'
    out.write(topcorner)
    
    #write the headers 
    for key1 in keys1:
        header = str(key1) + '\t'
        out.write(header)
    out.write('\n')
    
    #write the body
    for key2 in keys2:
        header = str(key2) + '\t'
        out.write(header)
        for key1 in keys1:
            if key2 in dict[key1]:
                value = dict[key1][key2]
                value = str(value) + '\t'
                
            else:
                value = 'NA\t'
            out.write(value)
        out.write('\n')
    out.close()    
    return

    
def dict2matrix(dict):
    # takes in 2-dimensional dictionary and prints out a 2-d array along with column labels and row labels
    # assumes the dictionary is rectangular but not nec. square (ie same labels for each row/column, but columns can be different from rows)
    
    rows = dict.keys()
    cols = dict[dict.keys()[0]].keys()
    
    matrix = zeros((len(rows),len(cols)))
    rc = -1
    for r in dict:
        rc += 1
        cc = -1
        for c in dict[r]:
            cc += 1
            data = dict[r][c]
            matrix[rc][cc] = data
            
    return(matrix,rows,cols)

def distmatrix2njtree_format(jsd,outfile):
    # jsd is a 2 dimensional dictionary with distances between samples
    # prepares data from distance matrix to run on http://www.trex.uqam.ca/index.php?action=trex
    out = open(outfile, 'w')
    keys = jsd.keys()
    out.write(('\t%s\n' % len(keys)))
    
    for s1 in keys:
        line = '%s\t' % s1
        for s2 in keys:
            line += str(jsd[s1][s2])
            line += ' '
        line += '\n'
        out.write(line)
    out.close()
    

def dict2matrix_ordered(dict,list):
    # takes in 2-dimensional dictionary and prints out a 2-d array along with column labels and row labels
    # assumes the dictionary is rectangular but not nec. square (ie same labels for each row/column, but columns can be different from rows)
    # takes a second argument which is a list that the dictionary is ordered by. Assumes list is same for rows/cols.
    
    matrix = zeros((len(list),len(list)))
    rc = -1
    for r in list:
        rc += 1
        cc = -1
        for c in list:
            cc += 1
            data = dict[r][c]
            matrix[rc][cc] = data
            
    return(matrix,list,list)            
            

def print_even_2D_matrix(dict, out_file, label):
    #    must have same labels for rows and columns
    #    sub_routine to print a 2D_matrix
    #    dict --> A two-dimensional dictionary.  First dimension will be rows, Second will be columns
    #    out_file --> destination to print to
    #    label --> label for the top corner of file
    
    out = open(out_file, 'w')
    keys = dict.keys()
    keys.sort()        
    topcorner = str(label) + '\t'
    out.write(topcorner)
    
    #write the headers 
    for key in keys:
        header = str(key) + '\t'
        out.write(header)
    out.write('\n')
    
    #write the body
    for key1 in keys:
        header = str(key1) + '\t'
        out.write(header)
        for key2 in keys:
            if key2 in dict[key1]:
                value = dict[key1][key2]
                value = str(value) + '\t'
            else:
                value = 'NA\t'
            out.write(value)
        out.write('\n')
    out.close()    
    return

def remove_columns(in_file,out_file,removal_list):
    #remove all columns present in removal list
    out = open(out_file, 'w')
    dict = matrix2dict(in_file)
    for key in removal_list:
        try:
            del(dict[key])
        except:
            KeyError
    print_uneven_2D_matrix(dict, out_file, '')

def cat_matrices(out_file,in_files,type):
    #type = 'horizontal' or 'vertical'
    # h = same row headers, new columns
    # v = same column headers, new rows
    # removes either the row or column header for second files
    d = {}
    out = open(out_file,'w')
    for f in in_files:
        d[f] = matrix2dict(f)
    
    if type.startswith('h'):
        
        #get columns and rows
        columns = []
        rows = set([])
        for f in d:
            for k1 in d[f]:
                columns.append(k1)
                for k2 in d[f][k1]:
                    rows.add(k2)
        
        #print header       
        header = ''
        for c in columns:
            header += '\t'
            header += c
        header += '\n'
        out.write(header)
        
        #print lines
        for r in rows:
            line = r
            for f in d:
                for c in d[f]:
                    line += '\t'
                    try:
                        line += str(d[f][c][r])
                    except KeyError:
                        line += 'NA'
            line += '\n'
            out.write(line)
                
    elif type.startswith('v'):
        #get columns and rows
        columns = set([])
        rows = set([])
        for f in d:
            for k1 in d[f]:
                columns.add(k1)
            for k2 in d[f][k1]:
                rows.add(k2)
        columns = list(columns)
        
        #print header       
        header = ''
        for c in columns:
            header += '\t'
            header += c
        header += '\n'
        out.write(header)        
        
        #print lines
        for f in d:
            for r in rows:
                line = r
                for c in columns:
                    line += '\t'
                    try:
                        line += str(d[f][c][r])
                    except KeyError:
                        line += 'NA'
                line += '\n'
                out.write(line)
            
    else:
        print 'invalid type'
                

def transpose_dictionary(dict):
    transposed = {}
    for k1 in dict:
        for k2 in dict[k1]:
            if k2 not in transposed:
                transposed[k2] = {}
    
    for k1 in dict:
        for k2 in dict[k1]:
            transposed[k2][k1] = dict[k1][k2]
    return(transposed)
     


def transpose(in_file, out_file):
    #    Takes in a N x M matrix and transposes the columns and rows
    #    Example:
    #    Input:
    #            col1    col2
    #    row1    val1    val2
    #    row2    val3    val4
    #
    #    Output:
    #            row1    row2
    #    col1    val1    val3
    #    col2    val2    val4
    dict1 = {}
    dict2 = {}
    rows = []
    start = True
    for line in open(in_file, 'r'):
        if start == True:
            start = False
            fields = line.rstrip().split('\t')
            label = fields.pop(0)
            columns = fields
            
        else:
            fields = line.rstrip().split('\t')
            row_head = fields.pop(0)
            rows.append(row_head)
            values = fields
            dict1[row_head] = {}
            count = 0
            for col_head in columns:
                dict1[row_head][col_head] = values[count]
                count += 1
    for col_head in columns:
        dict2[col_head] = {}
        for row_head in rows:
            value = dict1[row_head][col_head]
            dict2[col_head][row_head] = value
            
    print_uneven_2D_matrix(dict1, out_file, label)


def nw(seqs):
    # seqs is a list of strings with two strings equal to the sequences being aligned. returns similarity.
    # Var names from Wikipedia pseudocode
    d = -5 # Gap penalty
    A = seqs[0] # First sequence to be compared
    B = seqs[1] # Second ""
    I = range(len(seqs[0])) # To help iterate (Pythonic)
    J = range(len(seqs[1])) # ""
    F = [[0 for i in seqs[1]] for j in seqs[0]] # Fill a 2D array with zeroes
    # Similarity matrix from Wikipedia:
    S = \
    {'A': {'A': 10, 'G': -1, 'C': -3, 'T': -4},
     'G': {'A': -1, 'G':  7, 'C': -5, 'T': -3},
     'C': {'A': -3, 'G': -5, 'C':  9, 'T':  0},
     'T': {'A': -4, 'G': -3, 'C':  0, 'T':  8}}
    
    # Initialization
    for i in I:
        F[i][0] = d * i
    for j in J:
        F[0][j] = d * j
        
    # Scoring
    for i in I[1:]:
        for j in J[1:]:
            Match = F[i-1][j-1] + S[A[i]][B[j]]
            Delete = F[i-1][j] + d
            Insert = F[i][j-1] + d
            F[i][j] = max(Match, Insert, Delete)
    
    # Traceback
    AlignmentA = ""
    AlignmentB = ""
    i = len(seqs[0]) - 1
    j = len(seqs[1]) - 1
    
    while (i > 0 and j > 0):
        Score = F[i][j]
        ScoreDiag = F[i - 1][j - 1]
        ScoreUp = F[i][j - 1]
        ScoreLeft = F[i - 1][j]
        if (Score == ScoreDiag + S[A[i]][B[j]]):
            AlignmentA = A[i] + AlignmentA
            AlignmentB = B[j] + AlignmentB
            i -= 1
            j -= 1
        elif (Score == ScoreLeft + d):
            AlignmentA = A[i] + AlignmentA
            AlignmentB = "-" + AlignmentB
            i -= 1
        elif (Score == ScoreUp + d):
            AlignmentA = "-" + AlignmentA
            AlignmentB = B[j] + AlignmentB
            j -= 1
        else:
            print("algorithm error?")
    while (i > 0):
        AlignmentA = A[i] + AlignmentA
        AlignmentB = "-" + AlignmentB
        i -= 1
    while (j > 0):
        AlignmentA = "-" + AlignmentA
        AlignmentB = B[j] + AlignmentB
        j -= 1
    
    # Similarity
    lenA = len(AlignmentA)
    lenB = len(AlignmentB)
    sim1 = ""
    sim2 = ""
    len0 = 0
    k = 0
    total = 0
    similarity = 0.0
    
    if (lenA > lenB):
        sim1 = AlignmentA
        sim2 = AlignmentB
        len0 = lenA
    else:
        sim1 = AlignmentB
        sim2 = AlignmentA
        len0 = lenB
    while (k < len0):
        if sim1[k] == sim2[k]:
            total += 1
        k += 1
    total = float(total)   
    similarity = total / len0 * 100
    return(similarity)

def get_gps2dist(gps_coord_list):
    #approximation: http://www.johndcook.com/python_longitude_latitude.html

    lat1, long1, lat2, long2 = gps_coord_list
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0

    if lat1 == lat2 and long1 == long2:
        return 0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1) * degrees_to_radians
    phi2 = (90.0 - lat2) * degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
    km = arc * 6373 # (multiply by radius of earth)
    #return distance in kilometers 
    return km

def get_taxonomic_level(level,latin):
    #level values: 'k','p','c','o','f','g'
    #latin is an RDP string
    split_value = level + '__'
    try:
        taxon = latin.split(split_value)[1].split(';')[0]
    except IndexError:
        taxon = 'NA'
        #index error because this taxon doesn't have a group defined for this level of taxonomic resolution
        #e.g.: no 'class' defined for '241676~EU135313.1~tallgrass~prarie~soil~clone~FFCH16204~k__Bacteria;~p__SC3;~otu_4073'
    return(taxon)

def get_lowest_taxonomic_level(latin):
    #level values: 'k','p','c','o','f','g'
    #latin is an RDP string
    #example: k__Bacteria;p__Firmicutes;c__Clostridia;o__Clostridiales;f__Lachnospiraceae;g__;s__
    split_value = '__'
    taxon = ''
    while taxon == '':
        try:
            split_latin = latin.split(split_value)
            taxon = split_latin.pop().split(';')[0]
            level = split_latin.pop().split(';')[1]
            latin = split_value.join(split_latin)
            
        except IndexError:
            taxon = 'NA'
            level = 'NA'
            #index error because this taxon doesn't have a group defined for this level of taxonomic resolution
            #e.g.: no 'class' defined for '241676~EU135313.1~tallgrass~prarie~soil~clone~FFCH16204~k__Bacteria;~p__SC3;~otu_4073'
        if level == 'k':
            break
    return(taxon,level)        

def get_taxonomies(i,o):
    cmd = 'python /home/csmillie/bin/assign_taxonomy.py -i %s -r /home/mbsmith/alm-polz/db/gg_otus_4feb2011/rep_set/gg_97_otus_4feb2011.fasta -t /home/mbsmith/alm-polz/db/gg_otus_4feb2011/taxonomies/greengenes_tax_rdp_train.txt -o %s -c 0.75' % (i,o)
    os.system(cmd)