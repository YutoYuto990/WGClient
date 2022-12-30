class Dict:
  def __init__(self,dictionary):
    if isinstance(dictionary,dict):
      for i in dictionary:
        if isinstance(dictionary[i],dict):
          setattr(self,i,Dict(dictionary[i]))
        else:
          setattr(self,i,dictionary[i])
    else:
      return
