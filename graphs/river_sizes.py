# O(wh) | O(wh)
def riverSizes(matrix):

    n, m = len(matrix), len(matrix[0])

    visited_nodes = set(
        ((float("-inf"), float("inf")), (float("inf"), float("-inf")))
    )

    all_counts = []
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited_nodes and matrix[i][j] == 1:
                idx_stack = [(i, j)]
                counter = 0
                while len(idx_stack) > 0:

                    idx = idx_stack.pop()
                    visited_nodes.add(idx)

                    children_nodes = get_unvisited_children(idx, matrix, visited_nodes)

                    for child in children_nodes:
                        visited_nodes.add(child)

                    idx_stack = idx_stack + children_nodes

                    counter += 1

                all_counts.append(counter)

    return all_counts

def get_unvisited_children(idx, matrix, visited_nodes):

    n, m = len(matrix), len(matrix[0])

    all_nodes = [
        (max(min(idx[0]-0, n-1), 0), max(min(idx[1]+1, m-1), 0)),
        (max(min(idx[0]+1, n-1), 0), max(min(idx[1]+0, m-1), 0)),
        (max(min(idx[0]-0, n-1), 0), max(min(idx[1]-1, m-1), 0)),
        (max(min(idx[0]-1, n-1), 0), max(min(idx[1]+0, m-1), 0)),
    ]

    filter_edge_nodes = list(filter(lambda node: node!=idx, all_nodes))
    filter_visited_nodes = list(filter(lambda node: node not in visited_nodes, filter_edge_nodes))
    filter_zero_nodes = list(filter(lambda node: matrix[node[0]][node[1]], filter_visited_nodes))


    return filter_zero_nodes

if __name__ == "__main__":

    matrix = [
        [0, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 0, 1, 1],
    ]
    # matrix = [
    #     [0, 1],
    #     [1, 1],
    # ]
    ans = riverSizes(matrix)
    print(ans)
