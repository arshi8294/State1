# todo: try to find a way to don't show transfers between floors manually


from abc import ABC, ABCMeta, abstractmethod


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


class SingletonMeta(ABCMeta):
    _instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__call__(*args, **kwargs)
        return cls._instances


class State(ABC, metaclass=SingletonMeta):
    FLOORS = []

    def __init__(self):
        self._elevator = None
        self.add_floor()

    @abstractmethod
    def set_elevator(self, elevator):
        self._elevator = elevator

    @abstractmethod
    def go_up(self):
        pass

    @abstractmethod
    def go_down(self):
        pass

    def add_floor(self):
        self.FLOORS.append(self)


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

    print(floor.FLOORS)

