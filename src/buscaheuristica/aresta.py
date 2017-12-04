class Aresta(object):

  def __init__(self, v_destino, distancia, cor, custo_trafego):
    self._distancia = distancia
    self._v_destino = v_destino
    self._cor = cor
    self._custo_trafego = custo_trafego
  
  @property
  def distancia(self):
    return self._distancia

  @property
  def custo_trafego(self):
    return self._custo_trafego

  @property
  def v_destino(self):
    return self._v_destino

  @property
  def cor(self):
    return self._cor