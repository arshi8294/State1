class Elevator:
    def __init__(self, max_floor, min_floor, current_floor=0):
        self.max_floor = max_floor
        self.min_floor = min_floor
        self.current_floor = current_floor

    def go_up(self):
        if self.current_floor < self.max_floor:
            print("Elevator is going up to:", self.current_floor + 1)
            self.current_floor += 1

    def go_down(self):
        if self.current_floor > self.min_floor:
            print("Elevator going down to:", self.current_floor - 1)
            self.current_floor -= 1


if __name__ == "__main__":
    elevator = Elevator(10, -1)
    for i in range(15):
        elevator.go_up()
        if i % 3 == 0:
            elevator.go_down()
