import random
random.seed()

function = "" 

listOfOperations = [
  "Sqrt | SQRT(x)",
  "Exp | x^y",
  "Div | x/y",
  "Mult | x*y",
  "Add | x+y",
  "Sub | x-y",
]
inputs = []

def AddOperation(info): 
  termOne = info["termOne"]
  termTwo = info["termTwo"] or None
  oprtn = info["operation"] != None and listOfOperations[info["operation"]] or listOfOperations[random.randint(0,len(listOfOperations))-1]

  oprtn = oprtn.split(" | ")[1]
  oprtn = oprtn.replace("x",termOne)
  oprtn = oprtn.replace("y",termTwo)
  print(oprtn)
  return oprtn

  
AddOperation({
  "termOne": "3",
  "termTwo":"3^2",
  "operation":None
  })
  
