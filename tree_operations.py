"""This file contains functions for working with syntax trees"""

from nltk.tree import *
from itertools import permutations, product

permutedTrees = []


def permutate(originalTree: ParentedTree, subTrees: list[ParentedTree], limit: int):
    """This function makes all possible permutations of child NP nodes of subtrees in given subTrees list
       and adds permuted trees to permutedTrees global variable

       arguments:
       originalTree: ParentedTree - tree to make permutations in
       subtrees: list[ParentedTree] - list of subtrees, where NP nodes can be permuted
       limit: int - maximum permuted trees to be returned in response

       Function returns nothing
    """
    defaultPosition = []  # this variable contains treepositions of NP nodes in originalTree

    # here we fill defaultPosition variable with separate lists of NP treepositions for each subtree
    for subtree in subTrees:
        curSubtreeNPpositions = []
        for child in subtree:
            if child.label() == "NP":
                curSubtreeNPpositions.append(child.treeposition())
        defaultPosition.append(curSubtreeNPpositions)

    # here we fill eachSubtreePermutation list with lists of all possible permutations of NP nodes treepositions in
    # each subtree
    eachSubtreePermutationsList = []
    for j in range(len(defaultPosition)):
        eachSubtreePermutationsList.append(list(permutations(defaultPosition[j])))

    # this variable stores generator of all possible new, unique NP nodes treepositions
    allPossiblePermutations = product(*eachSubtreePermutationsList)

    next(allPossiblePermutations)  # skipping the default position of nodes(originalTree)

    # There we create trees with permutations
    while True:

        if len(permutedTrees) >= limit:
            break

        try:
            nextPermutation = next(allPossiblePermutations)
        except StopIteration:
            break

        newPermutedTree = ParentedTree.fromstring(str(originalTree))  # new tree should be a copy of original tree

        for j in range(len(nextPermutation)):
            for i in range(len(nextPermutation[j])):
                # here we use fromstring method because inserted
                # subtree shouldn't have parents, so we need to create
                # copy of subtree without parents
                newPermutedTree[defaultPosition[j][i]] = ParentedTree.fromstring(
                    str(originalTree[nextPermutation[j][i]]))
        permutedTrees.append(newPermutedTree)


def check_np_node(tree: ParentedTree):
    """This function checks whether given tree meets the conditions for permutation of child nodes

        arguments:
        tree: ParentedTree - tree to be checked

        returns:
        True/False - does tree meet the conditions
    """
    npChildCounter = 0  # this variable counts how many child NP nodes in current NP node
    if len(tree) > 1:
        for NPchild in tree:
            if NPchild.label() == "NP" and ((NPchild.right_sibling() and (NPchild.right_sibling().label() == ","
                                                                          or NPchild.right_sibling().label() == "CC"))
                                            or (NPchild.left_sibling() and (NPchild.left_sibling().label() == ","
                                                                            or NPchild.left_sibling().label() == "CC"))):
                npChildCounter += 1
    return npChildCounter >= 2


def rephrase(tree: str, limit: int):
    """This function takes tree as string and proceed it to further handling

        arguments:
        tree: string - syntax tree as string
        limit: int - maximum permuted trees to be returned in response

        returns:
        permutedTrees: list[str] - list with all possible permuted trees(up to limit)
    """
    ptree = ParentedTree.fromstring(tree)
    subtreesToChange = []
    for subtree in ptree.subtrees():
        if subtree.label() == "NP" and check_np_node(subtree):
            subtreesToChange.append(subtree)
    permutate(ptree, subtreesToChange, limit)
    return list(map(lambda item: str(item), permutedTrees))




