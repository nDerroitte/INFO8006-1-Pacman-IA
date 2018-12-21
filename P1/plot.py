import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 22})

plt.figure(figsize=(12, 10))
plt.xlabel("Small layout")
plt.ylabel("Total computation time (s)")


nb_maps = 1
nb_algo = 4
run_times = np.array([0.002290010452270508,0.0019309520721435547,0.002358675003051758,0.002918720245361328])
scores = [502,502,502,502]
nodes = [15,15,15,15]

bar_width = .01
bar_positions = np.arange(nb_maps)*bar_width*(nb_algo+1)

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, run_times[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["DFS","BFS","UCS","ASTAR"],loc = 1)
plt.savefig("fig/smallTime.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Small layout")
plt.ylabel("Score")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, scores[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["DFS","BFS","UCS","ASTAR"],loc = 1)
plt.savefig("fig/smallScores.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Small layout")
plt.ylabel("Number of explored nodes")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, nodes[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["DFS","BFS","UCS","ASTAR"],loc = 1)
plt.savefig("fig/smallNodes.png")


print("Small Done!")


run_times = np.array([0.08799529075622559,13.314135313034058, 6.6768388748168945,  7.80908989906311])
scores = [344,570,570,570]
nodes = [364,16688,12547,12098]

bar_width = .01
bar_positions = np.arange(nb_maps)*bar_width*(nb_algo+1)

plt.figure(figsize=(12, 10))
plt.xlabel("Medium layout")
plt.ylabel("Total computation time (s)")
for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, run_times[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["DFS","BFS","UCS","ASTAR"],loc = 1)
plt.savefig("fig/mediumTime.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Medium layout")
plt.ylabel("Score")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, scores[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["DFS","BFS","UCS","ASTAR"],loc = 1)
plt.savefig("fig/mediumScores.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Medium layout")
plt.ylabel("Number of explored nodes")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, nodes[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["DFS","BFS","UCS","ASTAR"],loc = 1)
plt.savefig("fig/mediumNodes.png")

print("Medium Done!")

run_times = np.array([ 0.2357783317565918,0.9902598857879639,  0.9783751964569092,  0.9297177791595459])
scores = [306,434,434,434]
nodes = [525,1966,1908,1231]

bar_width = .01
bar_positions = np.arange(nb_maps)*bar_width*(nb_algo+1)

plt.figure(figsize=(12, 10))
plt.xlabel("Large layout")
plt.ylabel("Total computation time (s)")
for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, run_times[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["DFS","BFS","UCS","ASTAR"],loc = 1)
plt.savefig("fig/largeTime.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Large layout")
plt.ylabel("Score")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, scores[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["DFS","BFS","UCS","ASTAR"],loc = 1)
plt.savefig("fig/largeScores.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Large layout")
plt.ylabel("Number of explored nodes")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, nodes[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["DFS","BFS","UCS","ASTAR"],loc = 1)
plt.savefig("fig/largeNodes.png")


print("Large done!")

run_times = np.array([0.03412127494812012,13.314135313034058])
scores = [562,570]
nodes = [132,16688]
nb_algo = 2
plt.figure(figsize=(12, 10))
plt.xlabel("Medium layout")
plt.ylabel("Number of explored nodes")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, nodes[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["BFS*","BFS"],loc = 1)
plt.savefig("fig/BFS3.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Medium layout")
plt.ylabel("Scores")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, scores[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["BFS*","BFS"],loc = 1)
plt.savefig("fig/BFS2.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Medium layout")
plt.ylabel("Computation time")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, run_times[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["BFS*","BFS"],loc = 1)
plt.savefig("fig/BFS1.png")
print("BFS comp done!")


run_times = np.array([ 4.399914503097534,7.80908989906311])
scores = [570,570]
nodes = [7740,12098]
nb_algo = 2
plt.figure(figsize=(12, 10))
plt.xlabel("Medium layout")
plt.ylabel("Number of explored nodes")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, nodes[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["a*","a* modified"],loc = 1)
plt.savefig("fig/astar3.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Medium layout")
plt.ylabel("Scores")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, scores[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["a*","a* modified"],loc = 1)
plt.savefig("fig/astar2.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Medium layout")
plt.ylabel("Computation time")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, run_times[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["a*","a* modified"],loc = 1)
plt.savefig("fig/astar1.png")
print("A* comp done!")


"""
run_times = np.array([[0.002290010452270508,0.0019309520721435547,0.002358675003051758,0.002918720245361328],[0.08799529075622559,13.314135313034058, 13.461907148361206, 9.34666919708252],[ 0.2357783317565918,0.9902598857879639,  1.0680322647094727, 1.0774049758911133]])
nb_algo = 4
bar_width = .01
bar_positions = np.arange(nb_maps)*bar_width*(nb_algo+1)

plt.figure(figsize=(16, 10))
plt.title("Computation times of different search algorithms for map : large")
plt.xlabel("Large layout")
plt.ylabel("Total computation time (s)")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, run_times[:, i], width=bar_width)

plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, ["Map %d" % i for i in range(nb_maps)])
plt.legend(["DFS","BFS","UCS","ASTAR"],loc = 1)
plt.savefig("fig/TIME.png")
"""
