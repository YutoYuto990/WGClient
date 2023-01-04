class Dict:
  def __init__(self,dictionary):
    if isinstance(dictionary,dict):
      for i in dictionary:
        key="num"+i if i.isdigit() else i
        if isinstance(dictionary[i],dict):
          setattr(self,key,Dict(dictionary[i]))
        else:
          setattr(self,key,dictionary[i])
    else:
      return
