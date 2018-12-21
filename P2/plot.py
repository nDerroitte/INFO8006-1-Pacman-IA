import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 22})

plt.figure(figsize=(12, 10))
plt.xlabel("Dumby Ghost agent")
plt.ylabel("Total computation time (s)")


nb_maps = 1
nb_algo = 3
run_times = np.array([1.197932481765747, 0.0951237678527832,0.012291908264160156])
scores = [526,526,526]
nodes = [9051,750,79]

bar_width = .01
bar_positions = np.arange(nb_maps)*bar_width*(nb_algo+1)

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, run_times[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["minimax","alphabeta","hminimax"],loc = 1)
plt.savefig("fig/dumbyTime.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Dumby Ghost agent")
plt.ylabel("Score")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, scores[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["minimax","alphabeta","hminimax"],loc = 1)
plt.savefig("fig/dumbyScores.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Dumby Ghost agent")
plt.ylabel("Number of explored nodes")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, nodes[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["minimax","alphabeta","hminimax"],loc = 1)
plt.savefig("fig/dumbyNodes.png")


print("Dumby Done!")


run_times = np.array([1.5028619766235352,  0.09778356552124023,  0.016309022903442383])
scores = [526,526,526]
nodes = [9051,750,79]

bar_width = .01
bar_positions = np.arange(nb_maps)*bar_width*(nb_algo+1)

plt.figure(figsize=(12, 10))
plt.xlabel("Greedy Ghost agent")
plt.ylabel("Total computation time (s)")
for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, run_times[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["minimax","alphabeta","hminimax"],loc = 1)
plt.savefig("fig/greedyTime.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Greedy Ghost agent")
plt.ylabel("Score")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, scores[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["minimax","alphabeta","hminimax"],loc = 1)
plt.savefig("fig/greedyScores.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Greedy Ghost agent")
plt.ylabel("Number of explored nodes")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, nodes[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["minimax","alphabeta","hminimax"],loc = 1)
plt.savefig("fig/greedyNodes.png")

print("Greedy Done!")

run_times = np.array([1.4899754524230957,0.08797073364257812,0.01856088638305664])
scores = [526,526,526]
nodes = [9051,750,79]

bar_width = .01
bar_positions = np.arange(nb_maps)*bar_width*(nb_algo+1)

plt.figure(figsize=(12, 10))
plt.xlabel("Smarty Ghost agent")
plt.ylabel("Total computation time (s)")
for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, run_times[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["minimax","alphabeta","hminimax"],loc = 1)
plt.savefig("fig/smartyTime.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Smarty Ghost agent")
plt.ylabel("Score")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, scores[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["minimax","alphabeta","hminimax"],loc = 1)
plt.savefig("fig/smartyScore.png")

plt.figure(figsize=(12, 10))
plt.xlabel("Smarty Ghost agent")
plt.ylabel("Number of explored nodes")

for i in range(nb_algo):
    plt.bar(bar_positions+bar_width*i, nodes[i], width=bar_width/2)
plt.xticks(bar_positions+(nb_algo-1)/2*bar_width, [""])
plt.legend(["minimax","alphabeta","hminimax"],loc = 1)
plt.savefig("fig/smartyNodes.png")


print("Smarty done!")
"""
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
