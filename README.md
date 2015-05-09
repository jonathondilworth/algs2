# Advanced Algorithms 2 : COMP36212

This repo is where I am going to be pushing some general implementations of models from the advanced algorithms two module to. Also decided I am going to be slapping some general notes in this README file.

## Currently contains:
 * An implementation for the generation of the ER Random, complex network model.
 * Some notes about structural properties of:
 	* ER-Random Networks.
 * Hopefully I won't forget to add more here when I actually commit other code.. (I am only human!)

### Structural Properties of ER-Random Network Graphs:
 * AVG Node Degree: < k > = 2M / N = p(N - 1) ~= pN.
 * AVG Path Length: L ~ ln(N) / ln(< k >).
 	* L increases logarithmically with the size of the network (Small World Property)
 	* ln(N) grows much slower than N -> a very large sized usually has a relatively small L. Additional reasoning: The numerator for L is growing very slowly and the denominator for L is decreasing, therefore L is increasing as N is increasing. **Therefore as more nodes are added to the network, the average path length is decreasing.**
 * Clustering Co-Efficient: C = p ~= <k> / N << 1.
 * Node Degree Distribution follows a Poisson distribution. (Need to think about this one a little more..)
 * ER Random graphs are not small world networks, even though they exhibit a small L. This is because they generally **do not have a large clustering co-efficient**, it is fairly small and C ~ p, which makes sense if you take a look at the figureOne in the repo. This leads to our next point.
 * ER Random graphs have a small clustering coefficient (this is a distinguishing characteristic).


 ## More info to be found at:
 * [My Personal Website](http://jonathondilworth.me/ "My Site")
 * [My Blog](jonathondilworth.blogspot.com "Blog")
