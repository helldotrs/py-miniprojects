#If the fox is left alone with the goose it will eat the goose, 
#if the goose is left alone with the corn it will eat corn, 
#the boat only has room for the farmer and one more item/animal. 
#how can the farmer cross the river? 

north_side = []
south_side = ["farmer", "fox", "goose", "corner"]

def n2s(a):
  if(a):
    north_side.remove(a)
    south_side.append(a)
  
  north_side.remove("farmer")
  south_side.append("farmer")
  
  a = ""

def s2n(a):
    if(a):
      south_side.remove(a)
      north_side.append(a)
    
    south_side.remove("farmer")
    north_side.append("farmer")
  
    a = ""

def test():
  def eat_test(a):
    if "goose" in a and ("fox" in a or "corn" in a):
      exit("loose:(")
  
  if "farmer" in list1:
    eat_test(list2)
  elif "farmer" in list2:
    eat_test(list1)

#lose test:
s2n("corn")


