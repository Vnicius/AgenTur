class Vertice(object):
  
  def __init__(self, chave, h_de_n):
    self._chave = chave
    self._h_de_n = h_de_n
    self._f_de_n = None
    self._arestas_adj = []

  @property
  def chave(self):
    return self._chave

  @property
  def h_de_n(self):
    return self._h_de_n

  @property
  def f_de_n(self):
    return self._f_de_n

  @property
  def arestas_adj(self):
    return self._arestas_adj

  @f_de_n.setter
  def f_de_n(self, f_de_n):
    self._f_de_n = f_de_n

  def add_aresta_adj(self, aresta):
    self._arestas_adj.append(aresta)