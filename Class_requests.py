import requests

Class Objekt ();
   def __init__(self, a,b,c,d,e)
      self.a = a
      self.b = b
      self.c = c
      self.d = d
      self.e = e
   def __str__(self);
      return self.a + ", " + self.b + ", " +  self.c + ", " +  self.d + ", " + self.e

def request();
   request = requests.get("")
   dict = request(request)
   for key in dict.keys:
      i = dict.key
