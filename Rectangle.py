from Shape import Shape
class Rectangle(Shape):
        
    def draw(self,canvas):
        print("Rectangleオブジェクトのdrawメソッドによる描画処理")
        x1 = self.x-self.wid/2
        y1 = self.y-self.len/2
        canvas.create_rectangle(x1,y1,x1+self.wid,y1+self.len,outline=self.color)
  

        
