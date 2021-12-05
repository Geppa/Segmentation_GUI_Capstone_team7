import sys
from tkinter import *
from tkinter import filedialog
import tkinter
import PIL.Image, PIL.ImageTk
from PyQt5.QtWidgets import QApplication
import cv2
import time
from PIL import ImageGrab
import numpy

class videoGUI:
    def __init__(self, window, window_title):
        self.window = window
        self.window.geometry("800x600+50+30")
        self.window.resizable(False,False)
        self.window.title(window_title)
        self.top_frame = Frame(self.window)
        self.top_frame.pack(side=TOP, pady=5)
        

        side_frame=Frame(self.window)
        side_frame.pack(side=BOTTOM,pady=5)

        bottom_frame = Frame(self.window)
        bottom_frame.pack(side=BOTTOM, pady=5)

        #self.pixel_x=[]
        #self.pixel_y=[]

        #polygon
        self.coord=[]  # for saving coord of each click position

        self.Dict_Polygons={}   # Dictionary for saving polygons
        self.list_of_points=[]
        self.poly = None


        self.cap = None
        self.pause = False   # Parameter that controls pause button
        self.delay = 15   # ms
        self.canvas = Canvas(self.top_frame)
        self.canvas.pack()
        
        # Select Button

        self.btn_select=Button(bottom_frame, text="Select Video File", width=15, command=self.open_file)
        self.btn_select.grid(row=0, column=0)

        # Play Button
        self.btn_play=Button(bottom_frame, text="Play", width=15, command=self.play_video)
        self.btn_play.grid(row=0, column=1)

        # Pause Button
        self.btn_pause=Button(bottom_frame, text="Pause", width=15, command=self.pause_video)
        self.btn_pause.grid(row=0, column=2)
        

        self.setButton=Button(side_frame,text="객체지정",width=15,command=self.capt)
        self.segButton=Button(side_frame,text="객체분할",width=15, command=self.pause_video)
        self.uncButton=Button(side_frame,text="불확실성측정",width=15, command=self.pause_video)
        self.mosButton=Button(side_frame,text="분할모자이크",width=15, command=self.pause_video)
        self.setButton.grid(row=0,column=0)
        self.segButton.grid(row=0,column=1)
        self.uncButton.grid(row=0,column=2)
        self.mosButton.grid(row=0,column=3)

        self.canvas.pack(expand=True, fill="both")
        self.canvas.bind("<B1-Motion>", self.draw_polygons)
        

        self.window.mainloop()

    def open_file(self):
        self.pause = True
        self.elaspedTime=0
        self.totalElaspedTime=0
        self.filename = filedialog.askopenfilename(title="Select file", filetypes=(("MP4 files", "*.mp4"),
                                       ("WMV files", "*.wmv"), ("AVI files", "*.avi")))
        
        self.cap = cv2.VideoCapture(self.filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = self.width, height = self.height)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        
        pass

    def get_videoFrame(self):   # get only one frame
        try:
            if self.cap.isOpened():
                self.elapsedTime=  time.time()- self.start_time #sec
                seekVal= int( self.fps*(self.totalElaspedTime+self.elapsedTime))
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, seekVal)
                ret, frame = self.cap.read()
                if frame is None:
                    return (False, None)
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        except Exception as e:
            print(e)
            return (False, None)

    def play_video(self):
        print("play_video...")
        if self.pause:
            self.pause= False
            self.start_time = time.time()
            self.play_loop()
        pass

    def pause_video(self):
        print("pause_video...")
        if self.pause:
            return
        self.pause= True
       
        self.totalElaspedTime=self.totalElaspedTime+ self.elapsedTime

    def play_loop(self):
        if self.pause:
            return
        
       
        ret, video_frame = self.get_videoFrame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(video_frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
            
        else:
            return
        self.canvas.update()
        self.after_id = self.window.after(self.delay, self.play_loop)
        pass

    def callback(self,event):
        
        self.canvas.create_line(event.x,event.y,event.x+1,event.y+1)

    def draw_polygons(self,event):
        mouse_xy = (event.x, event.y)
        self.func_Draw_polygons(mouse_xy)  


    # Function to draw polygon
    def func_Draw_polygons(self,mouse_xy):
        
        center_x, center_y = mouse_xy
        self.list_of_points.append((center_x, center_y))

        for pt in self.list_of_points:
            x, y =  pt
            #draw dot over position which is clicked
            x1, y1 = (x - 1), (y - 1)
            x2, y2 = (x + 1), (y + 1)
            try : 
                self.canvas.create_oval(x1, y1, x2, y2, fill='green', outline='green', width=5)

            # add clicked positions to list
                numberofPoint=len(self.list_of_points)
            # Draw polygon
                if numberofPoint>40:
                    self.poly=self.canvas.create_polygon(self.list_of_points, fill="greenyellow",width=2)
                    
                self.canvas.update()
        

            except:
                pass 
        
    
    

    def capt(self):
        x=self.top_frame.winfo_rootx()+80
        y=self.top_frame.winfo_rooty()+160
        w=self.top_frame.winfo_width()+x
        h=self.top_frame.winfo_height()+y
        box=(x,y,w,h)
        img=ImageGrab.grab(box)
        cv_img = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
        cv2.imshow('image',cv_img)
        cv2.waitKey(0)
        

    def __del__(self):
        if self.cap==None:
            return
        if self.cap.isOpened():
            self.cap.release()

    

                         
pass #End of Class

if __name__ == "__main__":
   
    videoGUI(Tk(), "Video Segmentation")
    
    pass