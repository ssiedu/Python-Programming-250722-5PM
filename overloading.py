class Area:
      def findarea(self,a=None,b=None):
            if(a!=None and b!=None):
                  print("Area of rectangle : ",a*b)
            elif(a!=None):
                  print("Area of square : ",a*a)
            else:
                  print("Nothing")

a=Area()
a.findarea()
a.findarea(10)
a.findarea(5,3)
a.findarea(10.5,20)
