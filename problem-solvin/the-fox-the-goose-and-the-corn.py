#If the fox is left alone with the goose it will eat the goose, 
#if the goose is left alone with the corn it will eat corn, 
#the boat only has room for the farmer and one more item/animal. 
#how can the farmer cross the river? 

north_side = []
south_side = ["farmer", "fox", "goose", "corner"]

def n2s(a):
  north_side.remove(a)
  north_side.remove("farmer")

  south_side.append(a)
  south_side.append("farmer")
