#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "green")
       	    self.down.bind("<Button-1>", self.downClicked)
       	    self.down.grid(row=2,column=1)

            self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "green")
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    self.left.grid(row=1,column=0)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "green")
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    self.right.grid(row=1,column=2)
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    #drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
		
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	   
        def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
        
        def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
app = MyApp(root)
root.mainloop()