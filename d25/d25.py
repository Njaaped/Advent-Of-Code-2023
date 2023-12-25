import networkx as nx
from math import prod


class G:
  def __init__(self) -> None:
    self.g = {}



def solve_part_1(s):
  G  = nx.Graph()
  for line in s.strip().split('\n'):
    a,bs = line.split(': ')
    for b in bs.split():
      G.add_edge(a,b)
  G.remove_edges_from(nx.minimum_edge_cut(G))
  return prod(len(c) for c in nx.connected_components(G))


print(solve_part_1(open('input.txt','r').read()))