class parent:
      def display(self):
            print("Base class")
class child(parent):
      def display(self):
            super().display()
            print("Derive class")

a=child()
a.display()
