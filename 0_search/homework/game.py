#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Time    : 2024/3/30 20:46
# @Author  : Sepine Tam
# @File    : game.py
# @IDE     : PyCharm
def add_from_position(position, player):
    state = State()
    state.state[position[0]][position[1]] = player
    return state


class State:
    def __init__(self):
        self.state = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def __repr__(self):
        row_strings = [" | ".join(cell if cell else " " for cell in row) for row in self.state]
        board_representation = "\n—————————\n".join(row_strings)
        board_representation += "\n"
        return board_representation

    def add(self, action):
        for i in range(len(action.state)):
            for j in range(len(action.state[i])):
                if action.state[i][j] == "O" or action.state[i][j] == "X":
                    self.state[i][j] = action.state[i][j]
        return self.state


def Result(s: State, a: State) -> State:
    """
    state after action A taken in state S
    :param s: 当前的状态
    :param a: 要下的位置
    :return: 在action后的state
    """
    for i in range(len(a.state)):
        for j in range(len(a.state[i])):
            if a.state[i][j] == "X" or a.state[i][j] == "O":
                s.state[i][j] = a.state[i][j]
    return s


def Player(s):
    """
    which player to remove in state S
    :param s: 当前的state
    :return: 在状态S下，该谁下棋了
    """
    number = 0
    for i in range(len(s.state)):
        for j in range(len(s.state[i])):
            if s.state[i][j] == "X":
                number += 1
    if number % 2 == 1:
        return "O"
    else:
        return "X"


def Actions(s: State) -> [State]:
    """
    legal to move in state S
    :param s:
    :return:
    """
    positions = []
    player = Player(s)
    for i in range(len(s.state)):
        for j in range(len(s.state[i])):
            if s.state[i][j] != "X" and s.state[i][j] != "O":
                positions.append([i, j, s.state[i][j]])
    return_s = []
    for position in positions:
        a_i = add_from_position([position[0], position[1]], player=player)
        return_s.append(a_i)
    return return_s


def winner(s: State) -> str:
    # 检查行和列
    for i in range(3):
        if s.state[i][0] == s.state[i][1] == s.state[i][2] != "":
            return s.state[i][0]
        if s.state[0][i] == s.state[1][i] == s.state[2][i] != "":
            return s.state[0][i]

    # 检查对角线
    if s.state[0][0] == s.state[1][1] == s.state[2][2] != "":
        return s.state[0][0]
    if s.state[0][2] == s.state[1][1] == s.state[2][0] != "":
        return s.state[0][2]

    return "No"


def is_full(s: State) -> bool:
    for row in s.state:
        for cell in row:
            if cell == "":
                return False
    return True


def Terminal(s: State) -> bool:
    """
    check if state S is a terminal state
    :param s: 当前状态
    :return: 游戏是否结束
    """
    if is_full(s):
        return True
    else:
        if winner(s) == "X" or winner(s) == "O":
            return True
        else:
            return False


def Utility(s: State) -> int:
    """
    final numerical value for terminal state S
    :param s: 当前的状态
    :return: 当前状态下谁获胜了，如果"X"获胜返回1，"O"获胜返回-1，平局返回0
    """
    win_player = winner(s)
    if win_player == "X":
        return 1
    elif win_player == "O":
        return -1
    else:
        return 0


# def Result(s: State, a: State):
#     """
#     state after action A taken in state S
#     :param s:
#     :param a:
#     :return:
#     """
#     state = s.add(a)
#     return state


class Game():
    # def __init__(self):
    #     self.state = [
    #         [[], [], []],
    #         [[], [], []],
    #         [[], [], []]
    #     ]

    def Terminal(self, s):
        """
        check if state S is a terminal state
        :param s:
        :return:
        """
        pass

    def Utility(self, s):
        """
        final numerical value for terminal state S
        :param s:
        :return:
        """
        pass


s = State()
a = add_from_position([0, 1], "X")
n = Result(s, a)
# print(a.__repr__() == n.__repr__())
# print(n)
aa = (Actions(n))
print(winner(a))
# for aaa in aa:
#     print(aaa)
