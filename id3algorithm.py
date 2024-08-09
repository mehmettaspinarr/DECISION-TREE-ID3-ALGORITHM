import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import copy
import networkx as nx


dataset = pd.read_csv('tennis.csv')
X = dataset.iloc[:, 1:].values
# print(X)
attribute = ['havaDurumu', 'sicaklik', 'nem', 'ruzgar']


class Node(object):
    def __init__(self):
        self.value = None
        self.decision = None
        self.childs = None


def findEntropy(data, rows):
    """
    Calculate the entropy of a subset of data.
    
    Parameters:
    - data: The dataset
    - rows: Indices of rows to consider
    
    Returns:
    - entropy: The entropy of the subset
    - ans: The class label if entropy is 0
    """
    Evet = 0
    Hayir = 0
    ans = -1
    idx = len(data[0]) - 1
    entropy = 0
    for i in rows:
        if data[i][idx] == 'Evet':
            Evet = Evet + 1
        else:
            Hayir = Hayir + 1

    x = Evet/(Evet+Hayir)
    y = Hayir/(Evet+Hayir)
    if x != 0 and y != 0:
        entropy = -1 * (x*math.log2(x) + y*math.log2(y))
    if x == 1:
        ans = 1
    if y == 1:
        ans = 0
    return entropy, ans


def findMaxGain(data, rows, columns):
    """
    Find the attribute with the maximum information gain.
    
    Parameters:
    - data: The dataset
    - rows: Indices of rows to consider
    - columns: Indices of attributes to consider
    
    Returns:
    - maxGain: The maximum information gain
    - retidx: The index of the attribute with maximum gain
    - ans: The class label if entropy is 0
    """
    maxGain = 0
    retidx = -1
    entropy, ans = findEntropy(data, rows)
    if entropy == 0:
       
        return maxGain, retidx, ans

    for j in columns:
        mydict = {}
        idx = j
        for i in rows: 
            key = data[i][idx]
            if key not in mydict:
                mydict[key] = 1
            else:
                mydict[key] = mydict[key] + 1
        gain = entropy


        for key in mydict:
            Evet = 0
            Hayir = 0
            for k in rows:
                if data[k][j] == key:
                    if data[k][-1] == 'Evet':
                        Evet = Evet + 1
                    else:
                        Hayir = Hayir + 1
            x = Evet/(Evet+Hayir)
            y = Hayir/(Evet+Hayir)
            if x != 0 and y != 0:
                gain += (mydict[key] * (x*math.log2(x) + y*math.log2(y)))/14
        
        if gain > maxGain:
            maxGain = gain
            retidx = j

    return maxGain, retidx, ans


def buildTree(data, rows, columns):

    """
    Build the decision tree recursively.
    
    Parameters:
    - data: The dataset
    - rows: Indices of rows to consider
    - columns: Indices of attributes to consider
    
    Returns:
    - root: The root node of the decision tree
    """

    maxGain, idx, ans = findMaxGain(X, rows, columns)
    root = Node()
    root.childs = []
    
    if maxGain == 0:
        if ans == 1:
            root.value = 'Evet'
        else:
            root.value = 'Hayir'
        return root

    root.value = attribute[idx]
    mydict = {}
    for i in rows:
        key = data[i][idx]
        if key not in mydict:
            mydict[key] = 1
        else:
            mydict[key] += 1

    newcolumns = copy.deepcopy(columns)
    newcolumns.remove(idx)
    for key in mydict:
        newrows = []
        for i in rows:
            if data[i][idx] == key:
                newrows.append(i)
        temp = buildTree(data, newrows, newcolumns)
        temp.decision = key
        root.childs.append(temp)
    return root


 
def plot_tree(root):
    """
    Plot the decision tree using matplotlib.
    
    Parameters:
    - root: The root node of the decision tree
    """


    def plot_node(node, x, y, dx, dy, level=0):
        if not node.childs:
            plt.text(x, y, node.value, ha='center', va='center', bbox=dict(boxstyle='round', fc='lightblue'))
            return

        plt.text(x, y, node.value, ha='center', va='center', bbox=dict(boxstyle='round', fc='lightgreen'))

        n_children = len(node.childs)
        width = 2 ** (3 - level) * 0.05  
        for i, child in enumerate(node.childs):
            next_x = x - width/2 + width*i/(n_children-1) if n_children > 1 else x
            next_y = y - dy
            plt.annotate('', xy=(next_x, next_y), xytext=(x, y),
                         arrowprops=dict(arrowstyle='->'))
            plt.text((x + next_x)/2, (y + next_y)/2, child.decision,
                     ha='center', va='center')
            plot_node(child, next_x, next_y, dx/2, dy, level+1)

    plt.figure(figsize=(20, 10))
    plot_node(root, 0.5, 1, 1, 0.2)
    plt.xlim(0, 1)
    plt.ylim(0, 1.1)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def calculate():
    rows = [i for i in range(0, 14)]
    columns = [i for i in range(0, 4)]
    root = buildTree(X, rows, columns)
    root.decision = 'Basla'
    plot_tree(root)


calculate()
