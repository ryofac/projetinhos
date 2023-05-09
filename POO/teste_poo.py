
from cpf_utils import *
class Pessoa():
    nome = str
    cpf = str

roberto = Pessoa()

roberto.cpf = '08197150346'
print('O cpf do roberto ', formatar_cpf(roberto.cpf))