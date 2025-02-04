from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "italic")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0  # Default high score in case the file is empty or doesn't exist.

        # Read high score from file, but handle the case where the file is empty or missing
        try:
            with open("data.txt") as data:
                content = data.read().strip()  # Remove any surrounding whitespace or newlines
                if content:  # Check if there's content in the file
                    self.high_score = int(content)
        except FileNotFoundError:
            # If the file doesn't exist, the high score remains 0
            pass
        except ValueError:
            # If the file contains invalid data, leave high score as 0
            pass

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Save the new high score to the file
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
