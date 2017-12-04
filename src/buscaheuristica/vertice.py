class Vertice(object):
  
  def __init__(self, chave, h_de_n, ponto_turistico):
    self._chave = chave
    self._h_de_n = h_de_n
    self._f_de_n = None
    self._arestas_adj = []
    self._ponto_turistico = ponto_turistico

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

  @property
  def ponto_turistico(self):
    return self._ponto_turistico

  @f_de_n.setter
  def f_de_n(self, f_de_n):
    self._f_de_n = f_de_n

  def add_aresta_adj(self, aresta):
    self._arestas_adj.append(aresta)

  def __repr__(self):
    return "\nChave: " + str(self._chave) + "\n" + \
           "h(n): " + str(self._h_de_n) + "\n" + \
           "f(n): " + str(self._f_de_n) + "\n" + \
           "Arestas ADJ: " + str(self._arestas_adj) + "\n" + \
           "Ponto Turístico: " + str(self._ponto_turistico) + "\n"