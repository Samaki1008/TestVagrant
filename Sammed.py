import json

class RCB:
  f = open('data.json')
  data = json.load(f)
  count=0
  wicketkeeper=False
  
      
  def Question1():
    for i in data['player']:
      if(i['country']!=['India']):
        count++
  
    assertFlag = assertTrue(count==4)
    if(assertFlag):
      print("True")
    else:
      print("False")
    
  def Question2():
    for i in data['player']:
      if(i['role']==['Wicket-keeper']):
        wicketkeeper=True
  
    
    if(wicketkeeper):
      print("True")
    else:
      print("False")
    
    
    
  f.close()
  
sam = RCB()
print("First question", sam.Question1())
print("2nd  question", sam.Question2())

