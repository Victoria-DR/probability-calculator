import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_balls):
        drawn = []

        if num_balls > len(self.contents):
            return self.contents

        for i in range(num_balls):
            drawn.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))

        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        drawn_dict = {}

        for ball in drawn:
            if ball not in drawn_dict:
                drawn_dict[ball] = 1
            else:
                drawn_dict[ball] += 1

        for i in range(1):
            b = True

            for key, value in expected_balls.items():
                if not (key in drawn_dict):
                    b = False
                    break
                if not (drawn_dict[key] >= value):
                    b = False
                    break

            if b:
                m += 1

    return m / num_experiments