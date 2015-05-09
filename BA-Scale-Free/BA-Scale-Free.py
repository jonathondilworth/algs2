# import the relevant libraries
import networkx as nx
import matplotlib.pyplot as plt
import random
import pylab


# FUNCTION DECLARATIONS

# our own fancy function for producing a random value to implement stochastic-ism
def rand(): # produces a random value between 0.0 and 1.0
	random_number = random.randint(0,10)
	f_rand = float(random_number)
	d_rand = f_rand * 0.1
	return d_rand

def rand_float():
	return random.random()

# return a random integer between two values
def rand_int(x,y):
	return random.randint(x,y)


# make a call to this function to calculate the preferential bias for a single node
def calculate_preferential_bias_on_node(network, node):
	return (float((nx.degree(network,node) + 1)) / (float(sum(nx.degree(network).values()) + nx.number_of_nodes(network))))
	# the reason why we're adding the number of nodes to the summation, is because its easier than individually adding
	# one to every entry in the dictionary, and then summing it


# make a call to this function to update the networks preferential bias
def calculate_preferential_bias_on_network(net):
	# create a dictionary with all of the update values of preferential bias
	updated_bias = dict()
	# run through each node in the network and calculate its new preferential bias
	for node in range(0, nx.number_of_nodes(net)):
		# add to dict
		updated_bias[node] = calculate_preferential_bias_on_node(net, node)

	# now we have a dictionary full of updated bias values, set them to the network
	nx.set_node_attributes(net, 'pb', updated_bias)


# this function does exactly the same thing as the one above, but disregards the newest node
# because this node doesn't effect the bias until its connections have been formed
def calculate_preferential_bias_on_network_except_newest_node(net):
	updated_bias = dict()
	for node in range(0, nx.number_of_nodes(net) - 1):
		updated_bias[node] = calculate_preferential_bias_on_node(net, node)

	nx.set_node_attributes(net, 'pb', updated_bias)
	

# call this function to add some number of initial nodes to the network
def add_initial_nodes(net, number_of_nodes_to_be_added):
	# add every node with an initial preferential bias of zero
	for x in range(0, number_of_nodes_to_be_added):
		net.add_node(nx.number_of_nodes(net), pb=0)

	# now that all the nodes have been added, we can calculate the initial preferential bias
	calculate_preferential_bias_on_network(net)


def add_new_node(net, m):
	# add a new node with an initial preferential bias of zero.
	new_node_id = nx.number_of_nodes(net)
	net.add_node(new_node_id, pb=0)
	# work out who to connect it to.. We have to do this M times!!!
	for edge_iteration in range (0, m):
		# Exactly the same as the proportional roulette wheel
		# generate our initial probability value
		p = rand_float()
		# initialise our roulette wheel
		roulette_wheel = 0.0
		# add the preferential bias for every node in the network up until we reach the
		# probability value (summation of all preferential bias equals 1.0)
		for node in range(0, nx.number_of_nodes(net) - 1): # - 1 because we don't want to self-connect
			roulette_wheel += nx.get_node_attributes(net, 'pb')[node]
			if p < roulette_wheel: # don't need to check if edge already exists, because networkx is clever!
				net.add_edge(new_node_id, node)
				# now we have a new edge, we have a new preferential bias
				#calculate_preferential_bias_on_network_except_newest_node(net)
				break

# START OF PROGRAMME

# initial number of nodes (n_0)
n_initial = 2

# time step (total iterations, or nodes to be added to the network)
t = 15

# number of edges to be added to each new node (with preferential bias)
m = 2

# our graph
g = nx.Graph()

# start with n_initial
add_initial_nodes(g, n_initial)

# for every timestep t, add a new node with preferential bias
for timestep in range (0, t):
	add_new_node(g, m)
	calculate_preferential_bias_on_network(g)

# output the global clustering co-efficient
print(sum(nx.clustering(g).values()) / nx.number_of_nodes(g))

# lets draw this lovely thing!
nx.draw(g, pos=nx.spring_layout(g))
plt.show()