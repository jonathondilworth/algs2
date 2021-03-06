# Advanced Algorithms 2 : COMP36212

This repo is where I am going to be pushing some general implementations of models from the advanced algorithms two module to. Also decided I am going to be slapping some general notes in this README file.

## Currently contains: (will eventually get round to changing this to an index)
 * An implementation for the generation of the ER Random, complex network model.
 * Some notes about structural properties of:
 	* ER-Random Networks.
 * Hopefully I won't forget to add more here when I actually commit other code.. (I am only human!)

## Things you will need to know about (I think):
 * Average Path Length (size)
 * Global Clustering Coefficient (density)
 * Degree Distribution (connectivity)
 * Topological Characteristics:
 	* Centrality (Degree, Closeness, Betweenness)
 	* Mixing Patterns
 * Classification & properties of different network models:
 	* ER-Random
 	* Small World:
 		* Watts-Strogatz
 		* Newman-Watts
 	* Scale Free:
 		* Barabási and Albert (BA) Model
 		* BA Variant: Rewiring
 		* BA Variant: Competition

## ER-Random Complex Networks

Check out the ER-Random folder in the Repo.

### Structural Properties of ER-Random Network Graphs:
 * AVG Node Degree: < k > = 2M / N = p(N - 1) ~= pN.
 * AVG Path Length: L ~ ln(N) / ln(< k >).
 	* L increases logarithmically with the size of the network (Small World Property)
 	* ln(N) grows much slower than N (see plot How ln(N) varies as N increases.png in repo) -> a very large sized usually has a relatively small L. Additional reasoning: The numerator for L is growing very slowly and the denominator for L is decreasing, therefore L is increasing as N is increasing. **Therefore as more nodes are added to the network, the average path length is decreasing.**
 * Clustering Co-Efficient: C = p ~= <k> / N << 1.
 * Node Degree Distribution follows a Poisson distribution. (Need to think about this one a little more..)
 * ER Random graphs are not small world networks, even though they exhibit a small L. This is because they generally **do not have a large clustering co-efficient**, it is fairly small and C ~ p, which makes sense if you take a look at the figureOne in the repo.
 * ER Random graphs have a small clustering coefficient (this is a distinguishing characteristic).

Its also important to note that these types of graphs have an **emergent feature**, in this case, you generally see the appearance of cycles or a [giant component](http://en.wikipedia.org/wiki/Giant_component "wiki link") at some threshold value of p.

## Small World Networks

Check out the Small-World-Network folder in the Repo.

Small world networks are more like real world networks, two distinguishing characteristics of small world networks are as follows:
 * Short AVG path length.
 * High clustering coefficient.

And there exist two primary models that we need to know about (for the exam anyway):
 * [Watts-Strogatz Model](http://en.wikipedia.org/wiki/Watts_and_Strogatz_model "wiki link")
 * Newman-Watts variant of the Watts-Strogatz Model.

### Watts-Strogatz Small World Algorithm
 1. Initialise a regular nearest-neighbour coupled network of N nodes arranged in a ring, in which each node i is symmetrically connected to its nearest neighbours i ± 1, i ± 2, ..., i ± K/2 with K an even integer (being the number of adjacent nodes to i). The number of links is NK/2.
 2. Randomisation: Randomly rewire each link of the network with probability p:
 	a. For every node i (i = 1,...,N), each link connected to a clockwise (or counter-clockwise) neighbour of i is rewired to a randomly chosen node (from anywhere in the network) with a probability of p.
 	b. The link will be preserved with a probability 1 - p.

Implementation!


## More info to be found at:
 * [My Personal Website](http://jonathondilworth.me/ "My Site")
 * [My Blog](http://jonathondilworth.blogspot.com "Blog")

# References
 * Eva Navarro Lopez (2015), Advanced Algorithms 2 Lecture Slides, University of Manchester.
 * Alain Barrat, Marc Barthelemy, Alessando Vespignani (2008), Dynamical Processes on Complex Networks, Cambridge University Press.
