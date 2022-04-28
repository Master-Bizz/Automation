def listing(lista):
   return lista.count(19)==2 and lista.count(8)==3

def validate(lista):
   if len(lista) >= 10:
     raise ValueError('Too many numbers, Cmon..!')

def lenlist(newl):
   return len(newl)==8 and newl.count(newl[5])==3  # fifth number occurs 3 times
  