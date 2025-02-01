import tkinter as tk
import math
import time


class AnalogClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analog Clock")
        self.geometry("500x500")

        # Initialize with system time
        self.hours = time.localtime().tm_hour % 12
        self.minutes = time.localtime().tm_min
        self.seconds = time.localtime().tm_sec

        # Create a canvas to draw the clock
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack(pady=20)

        # Set up the center of the clock
        self.center = (200, 200)
        self.radius = 150
        self.second_color = 'red'

        # Update the clock every second
        self.update_clock()

    def draw_hand(self, angle, length, color, width):
        # Convert angle to radians
        angle_rad = math.radians(angle)
        x_end = self.center[0] + length * math.sin(angle_rad)
        y_end = self.center[1] - length * math.cos(angle_rad)

        # Draw the hand
        self.canvas.create_line(self.center[0], self.center[1], x_end, y_end, width=width, fill=color, arrow=tk.LAST)

    def update_clock(self):
        self.canvas.delete("all")

        # Draw the clock face
        self.canvas.create_oval(50, 50, 350, 350)

        # Draw clock numbers
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            x = self.center[0] + (self.radius - 20) * math.cos(angle)
            y = self.center[1] + (self.radius - 20) * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i + 1), font=("Arial", 14))

        # Draw the hour hand
        hour_angle = (self.hours % 12) * 30 + (self.minutes / 2) - 90
        self.draw_hand(hour_angle, self.radius - 60, 'black', 6)

        # Draw the minute hand
        minute_angle = self.minutes * 6 - 90
        self.draw_hand(minute_angle, self.radius - 40, 'black', 4)

        # Draw the second hand and change its color every minute
        if self.seconds == 0:
            self.second_color = 'red' if self.second_color != 'red' else 'green'
        second_angle = self.seconds * 6 - 90
        self.draw_hand(second_angle, self.radius - 20, self.second_color, 2)

        # Update seconds (auto-tick every second)
        self.seconds = (self.seconds + 1) % 60
        if self.seconds == 0:
            self.minutes = (self.minutes + 1) % 60
            if self.minutes == 0:
                self.hours = (self.hours + 1) % 12

        # Update the clock every 1000ms (1 second)
        self.after(1000, self.update_clock)


if __name__ == "__main__":
    clock = AnalogClock()
    clock.mainloop()
