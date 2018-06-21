class mapeamentoDireto(Cache):
  def __init__(self, linhas, palavras_linhas, poli):
    super().__init__(linhas, palavras_linhas)
    self.q_tag = 0
    self.idx = 0
    self.politica = poli
  
  #def calcula(self, adress)
    

  def insert(self):
    if linha[self.idx].bit and self.politica == 2:
      self.Memoria += 1
    linha[self.idx].tag = q_tag
    self.Memoria += 1

  def writeback(self, adress):
    if self.look(adress):
      linha[self.idx].bit = True


  def writethrough(self, adress):
    if self.look(adress):
      self.Memoria += 1

  def look(self, adress):
    self.calcula(adress)
    if linha[self.idx].tag == q_tag:
      self.ThumbsUp += 1
      return True
    else:
      self.ThumbsDown += 1
      self.insert()
      return False

  def loadInstrucao(self, adress):
    self.look(adress)
  
  def loadData(self, adress):
    self.look(adress)
  
  def storeData(self, adress):
    if self.politica == 1: #1 to writethrough n 2 to writeback
      self.writethrough(adress)
    else:
      self.writeback(adress)

  def modifyData(self, adress):
    self.look(adress)
    if self.politica == 1: #1 - writethrough e 2 - writeback
      self.writethrough(adress)
    else:
      self.writeback(adress)







