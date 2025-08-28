# This script demonstrates polymorphism in Python using a simple
# example of vehicles. Each vehicle class inherits from a base class
# and implements its own version of the `move()` method.
# ==========================================================


class Vehicle:
    """
    Base class for all types of vehicles.
    """

    def move(self):
        """
        Generic move method for a vehicle.
        This method can be overridden by subclasses
        to define specific movement behavior.
        """
        print("This vehicle moves in some way.")


class Car(Vehicle):
    """
    Car class inheriting from Vehicle.
    """

    def move(self):
        """
        Overrides the base class method to describe
        how a car moves.
        """
        print("Driving 🚗")


class Plane(Vehicle):
    """
    Plane class inheriting from Vehicle.
    """

    def move(self):
        """
        Overrides the base class method to describe
        how a plane moves.
        """
        print("Flying ✈️")


class Bicycle(Vehicle):
    """
    Bicycle class inheriting from Vehicle.
    """

    def move(self):
        """
        Overrides the base class method to describe
        how a bicycle moves.
        """
        print("Pedaling 🚴")


# ===========================
# ==== Demo Section =========
# ===========================
if __name__ == "__main__":
    """
    Demonstration of polymorphism:
    Iterates over different vehicle objects and
    calls the `move()` method on each. The correct
    version of the method is executed based on the
    object's class.
    """
    vehicles = [Car(), Plane(), Bicycle()]

    for v in vehicles:
        v.move()