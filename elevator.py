from abc import ABC, abstractmethod


class Elevator:

    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state
        self._state.set_elevator(self)

    def go_up_btn(self):
        self._state.go_up()

    def go_down_btn(self):
        self._state.go_down()


class State(ABC):
    def __init__(self):
        self._elevator = None

    @abstractmethod
    def set_elevator(self, elevator):
        self._elevator = elevator

    @abstractmethod
    def go_up(self):
        pass

    @abstractmethod
    def go_down(self):
        pass


class GroundFloor(State):
    def set_elevator(self, elevator):
        self._elevator = elevator

    def go_up(self):
        print('Elevator going up to First floor')
        self._elevator.set_state(FirstFloor())

    def go_down(self):
        print("Elevator is already in min floor")


class FirstFloor(State):
    def set_elevator(self, elevator):
        self._elevator = elevator

    def go_down(self):
        print("Elevator is going down to Ground floor")
        self._elevator.set_state(GroundFloor())

    def go_up(self):
        print("Elevator is going up to Second floor")
        self._elevator.set_state(SecondFloor())


class SecondFloor(State):
    def set_elevator(self, elevator):
        self._elevator = elevator

    def go_down(self):
        print("Elevator is going down to First floor")
        self._elevator.set_state(FirstFloor())

    def go_up(self):
        print("Elevator is already in max floor")


if __name__ == "__main__":
    floor = GroundFloor()
    elevator = Elevator()
    elevator.set_state(floor)

    elevator.go_up_btn()
    elevator.go_up_btn()
    elevator.go_up_btn()
    elevator.go_down_btn()
    elevator.go_down_btn()
    elevator.go_down_btn()
    elevator.go_down_btn()
