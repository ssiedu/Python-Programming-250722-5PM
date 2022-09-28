class parent:
      def fun1(self):
            print("This is function1")

class child1(parent):
      def fun3(self):
            print("This is function3")

class child2(parent):
      def fun2(self):
            print("This is function2")

class subchild(child1,child2):
      def fun4(self):
            print("This is function4")

a=subchild()
a.fun1()
a.fun3()
#b=child2()
a.fun4()
a.fun2()
