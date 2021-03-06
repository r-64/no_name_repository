from random import *
import numpy
import math

def print_ccdf(x, logscale = False) :
	x = sorted(x)[::-1]
	n = len(x)
	u,v = [(math.log(x[i]) if logscale else x[i], math.log(1.0*(i+1)/n) if logscale else 1.0*(i+1)/n) for i in range(len(x)) if (not logscale) or (x[i] > 0)],[]
	la = 1e10
	for i,j in u :
		if i<la-1e-2 :
			v+=[(i,j)]
			la = i
	print """\\begin{{tikzpicture}}
\\begin{{axis}}[xlabel={0},ylabel={1}]
\\addplot[mark=*,mark size=0.5] coordinates {{ {2} }};
\\end{{axis}}
\\end{{tikzpicture}}""".format(
		"$\\ln x$" if logscale else "$x$",
		"$\\ln \\bar{F}_{\\text{emph}}(x)$" if logscale else "$\\bar{F}_{\\text{emph}}(x)$",
		" ".join(["({0}, {1})".format(a,b) for a,b in v]))

def print_histogram(x) :
	l = math.floor(min(x))
	r = math.ceil(max(x))
	k = 50
	u = (r - l) / k
	s = 0
	y = [0 for i in range(k+1)]
	for i in x :
		z = max(0,min(k-1,int(math.floor((i - l) / u))))
		y[z] += 1

	print """\\begin{{tikzpicture}}
\\begin{{axis}}[ymin={0}, ymax={1}, area style,]
\\addplot+[ybar interval, mark=no] plot coordinates {{ {2} }};
\\end{{axis}}
\\end{{tikzpicture}}
""".format(0, max(y) * 1.05, " ".join(["({0}, {1})".format(l + i * u, y[i]) for i in range(k+1)]))


def classical_clt_(n) :
	"""a sequence of `n` iid Weibull rv with shape parameter 1 and scale parameter 1. """
	s = 0
	for i in range(n) :
		x = numpy.random.weibull(1)
		s += x - 1
	return s / (n**0.5)

def classical_clt(k, n) :
	"""try `k` times and plot"""
	x = []
	for i in range(k) :
		x += [classical_clt_(n)]
	print_histogram(x)
	print """\\caption{Classical CLT\\label{f1}}
\\end{minipage}
\\begin{minipage}[c]{0.49\\textwidth}"""

def generalized_clt_(alpha, n=10000) :
	"""a sequence of `n` iid Pareto rv with shape parameter alpha and x_m=1."""
	s = 0
	mean = alpha / (alpha - 1)
	for i in range(n) :
		x = numpy.random.pareto(alpha) + 1
		s += x - mean
	return s / (n**(1/alpha))

def generalized_clt(alpha, k=1000, n=10000) :
	"""try `k` times and plot as in Ex6.1(b)i,ii,iii"""
	x = []
	for i in range(k) :
		x += [generalized_clt_(alpha, n)]
	print_histogram(x)
	print """\\caption{Generalized CLT\\label{f2}}
\\end{minipage}
\\end{figure}

\\begin{figure}
\\begin{minipage}[c]{0.49\\linewidth}"""

	print_ccdf(x)
	print """\\caption{empirical c.c.d.f.\\label{f3}}
\\end{minipage}
\\begin{minipage}[c]{0.49\\textwidth}"""
	print_ccdf(x, True)
	print """\\caption{empirical c.c.d.f. on a log-log scale.\\label{f4}}
\\end{minipage}
\\end{figure}"""

if __name__ == '__main__' :
	print """\\begin{figure}
\\begin{minipage}[c]{0.49\linewidth}"""
	classical_clt(10000, 10000)# 10000, 10000
	generalized_clt(1.618, 10000, 10000) #

