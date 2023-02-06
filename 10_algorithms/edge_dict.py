# write a list of edges as a dict
# graph = [[0, 1], [0, 2], [0, 3], [1, 0], [1,2], [2, 0], [2, 1], [2, 3], [3,0], [3,2]]  -  list of edges

graph_dict = {
    1: [[0, 1], [0, 2], [0, 3]],
    2: [[1, 0], [1, 2]],
    3: [[2, 0], [2, 1], [2, 3]],
    4: [[3, 0], [3, 2]]
}
for key in graph_dict:
    for i in graph_dict[key]:
        print(i)
