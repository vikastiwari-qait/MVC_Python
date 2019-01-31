
class Person(object):
   def __init__(self, first_name = None, last_name = None):
      self.first_name = first_name
      self.last_name = last_name
  
   def name(self):
      return ("%s %s" % (self.first_name,self.last_name))
		
   @classmethod
   
   def getAll(self):
      database = open('db.txt', 'r')
      result = []
      for line in database.readlines():
         temp = line.split()
         person = Person(temp[0],temp[1])
         result.append(person)
      return result