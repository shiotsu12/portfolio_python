from Circle import Circle
from Rectangle import Rectangle
from Line import Line
import tkinter
import random
class AddShapePanelv4:

 def __init__(self):
     print("AddShapePanel オブジェクトの生成")
     self.create_window()
     self.listOfObject=[]
     self.IDforCircleRed = 1
     self.IDforRectangleBlue = 2
     self.IDforLineGreen= 3
 def create_window(self):
     self.window = tkinter.Tk()
     self.canvas = tkinter.Canvas(self.window, bg = "white",
     width = 320, height = 240)
     self.canvas.pack()

     circle_button1 = tkinter.Button(self.window, text = "NewCircle1",
     command = lambda:self.createShape(self.IDforCircleRed))
     circle_button1.pack(side = tkinter.LEFT)
     rectangle_button = tkinter.Button(self.window, text = "NewRectangle",
     command = lambda:self.createShape(self.IDforRectangleBlue))
     rectangle_button.pack(side = tkinter.LEFT)
     Line_button = tkinter.Button(self.window, text = "NewLine",
     command = lambda:self.createShape(self.IDforLineGreen))
     Line_button.pack(side = tkinter.LEFT)

 def createShape(self, drawID):
     print("createShape メソッドの実行") 
     x = random.randint(0,320)
     y = random.randint(0,240)
     wid = random.randint(0,90) + 10
     len = random.randint(0,90) + 10
     if(drawID == self.IDforCircleRed):
         color = "Red"
         self.listOfObject.append(Circle(x,y,wid,len,color))
         self.repaint()
     elif(drawID == self.IDforRectangleBlue):
         color = "Blue"
         self.listOfObject.append(Rectangle(x,y,wid,len,color))
         self.repaint()
     elif(drawID == self.IDforLineGreen):
         color = "Green"
         self.listOfObject.append(Line(x,y,wid,len,color))
         self.repaint()
 def repaint(self):
     print("repaint メソッドの実行：画面をクリア＆paint メソッドを呼び出す")
     self.canvas.delete("all")
     self.paint()

 def paint(self):
     print("paint メソッドの実行")
     for drawObject in self.listOfObject:
         drawObject.draw(self.canvas)
 def run(self):
     self.window.mainloop()

AddShapePanelv4().run() 