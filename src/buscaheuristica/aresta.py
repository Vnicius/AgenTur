class Aresta(object):

  def __init__(self, v_destino, distancia):
    self._distancia = distancia
    self._v_destino = v_destino
  
  @property
  def distancia(self):
    return self._distancia

  @property
  def v_destino(self):
    return self._v_destino
