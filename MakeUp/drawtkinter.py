import Tkinter as tk
from PIL import ImageTk, Image, ImageGrab, ImageDraw
import cv2
from numpy import array


class ExampleApp(tk.Tk):
    def __init__(self):
        window = tk.Tk.__init__(self)
        cv_img = cv2.cvtColor(cv2.imread("image/img7.jpg"), cv2.COLOR_BGR2RGB)
        self.height, self.width, self.no_channels = cv_img.shape

        self.previous_x = self.previous_y = 0
        self.x = self.y = 0
        self.points_recorded = []
        self.canvas = tk.Canvas(self, width=self.width + 200, height=self.height + 200, cursor="cross")
        self.button_close = tk.Button(self, text="close", command=self.button_close)
        self.button_close.pack(side="top", expand=False)
        self.canvas.pack()



        self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv_img))
        self.canvas.create_image(100, 100, image=self.photo, anchor=tk.NW)

        self.wm_attributes('-fullscreen','true')

        self.button_print = tk.Button(self, text="Display points", command=self.print_points)
        self.button_print.pack(side="top", fill="both", expand=True)
        self.button_clear = tk.Button(self, text="Clear", command=self.clear_all)
        self.button_clear.pack(side="top", fill="both", expand=True)
        self.button_save = tk.Button(self, text="save", command=self.save_image)
        self.button_save.pack(side="top", fill="both", expand=True)

        self.canvas.bind("<Motion>", self.tell_me_where_you_are)
        self.canvas.bind("<B1-Motion>", self.draw_from_where_you_are)
        self.image1 = Image.new("RGB", (self.width, self.height), "white")
        draw = ImageDraw.Draw(self.image1)

    def button_close(self):
        self.destroy()

    def clear_all(self):
        self.canvas.delete("all")

    def save_image(self):
        ImageGrab.grab((0, 0, self.width, self.height)).save('img.jpg')
        # filename="img.jpg"
        # self.image1.save(filename)

    def print_points(self):
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()
        self.canvas.create_line(self.points_recorded, fill="black")
        self.points_recorded[:] = []

    def tell_me_where_you_are(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def draw_from_where_you_are(self, event):
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()

        self.x = event.x
        self.y = event.y
        self.canvas.create_line(self.previous_x, self.previous_y,
                                self.x, self.y, fill="black")
        self.points_recorded.append(self.previous_x)
        self.points_recorded.append(self.previous_y)
        self.points_recorded.append(self.x)
        self.points_recorded.append(self.x)
        self.previous_x = self.x
        self.previous_y = self.y


