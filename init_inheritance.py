class parent:
      def __init__(self):
            print("Base class")

class child(parent):
      def __init__(self):
            parent.__init__(self)
            print("Derive Class")

a=child()

