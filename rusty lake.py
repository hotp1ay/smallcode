def next_step(game_map, start_point, direction):
    start_point[0] += direction[0]
    start_point[1] += direction[1]
    if start_point[0] >= len(game_map) or start_point[0] < 0 or start_point[1] >= len(game_map[0]) or start_point[1] < 0:
        return "None"
    while game_map[start_point[0]][start_point[1]] == 0:
        start_point[0] += direction[0]
        start_point[1] += direction[1]
        if start_point[0] >= len(game_map) or start_point[0] < 0 or start_point[1] >= len(game_map[0]) or start_point[1] < 0:
            return "None"
    return start_point


def permutation(directions):  # 递归函数，返回所有排列情况
    if len(directions) == 1:
        return [directions]
    else:
        orders = []
        for d, direction in enumerate(directions):
            results = permutation(directions[:d] + directions[d + 1:])  # 取出列表中的一个数，递归剩下的数
            for result in results:
                orders.append([direction] + result)
        return orders


def play(game_map, start_point, end_point, directions):
    orders = permutation(directions)
    for order in orders:
        tmp_point = [i for i in start_point]  # 虫子位置
        for direction in order:
            tmp_point = next_step(game_map, tmp_point, direction)  # 计算虫子位置
            if tmp_point == "None":
                break
        if tmp_point == end_point:
            return order
    print("No solution")


game_map = [[1, 0, 0, 1, 1, 1, 1, 1, 1, 1], \
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
            [0, 0, 1, 1, 0, 1, 1, 1, 0, 1], \
            [0, 1, 1, 0, 1, 1, 1, 1, 0, 1], \
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1]]  # 洞的位置为1，没洞的位置为0
start_point = [0, 0]
end_point = [0, 9]
directions = [[1, 0], [1, 0], [0, 1], [0, 1], [-1, 1], [1, 1], [-1, 0]]  # 每个瓜子指向的位置，向下向右为[+1, +1]
