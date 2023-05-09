class radio():
#abstração
    cor = str
    faixa= str
    vol_max= 100
    vol_min= 0
    def _init_(self):
        self.cor=input("cor do Rádio?  :")
        self.faixa=(input("qual música?:"))
        self.vol=int(input("vol :"))
print("-"*25)

print("radio1 :")
r1=radio()
print(f"radio1 cor: {r1.cor}")
print(f"radio1 faixa : {r1.canal}")
if r1.vol>=40:
    print("Volume máximo")
    print("radio1 vol.max: 40")
else:
  print(f"radio1 volume : {r1.vol}")

print("-"*25)