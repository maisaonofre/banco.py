class conta:
  def __init__(self, titular, saldo, senha):
    self.titular = titular
    self.saldo = saldo
    self.senha = senha

def saque (self, valor):
  if self.saldo >= valor: 
    self.saldo-=valor
  else:
    print("Saldo insuficiente")

#instanciar objeto
conta1 = Conta("Maisa",1000,"12345")

conta1.saque(100)
