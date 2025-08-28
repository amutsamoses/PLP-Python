# This script demonstrates how to create a custom class in Python
# with attributes, methods, and inheritance to add extra features.
# The base class is `Smartphone`, and the subclass `SmartphonePro`
# inherits from it and adds new functionality.
# ==========================================================


class Smartphone:
    """
    A basic Smartphone class that simulates simple smartphone behavior.
    """

    def __init__(self, brand, model, battery=100):
        """
        Constructor method to initialize the smartphone's attributes.

        Parameters:
        brand (str): The brand of the smartphone (e.g., Samsung, Apple)
        model (str): The model name of the smartphone (e.g., Galaxy S24)
        battery (int): Battery level in percentage, defaults to 100
        """
        self.brand = brand
        self.model = model
        self.battery = battery
        self.is_on = False  # Represents the phone's power state

    def power_on(self):
        """
        Turns on the smartphone.
        Checks if the phone is already on before switching the state.
        """
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        """
        Turns off the smartphone.
        Checks if the phone is already off before switching the state.
        """
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def charge(self, amount):
        """
        Increases the battery level of the smartphone by a given amount.
        The battery percentage is capped at 100%.

        Parameters:
        amount (int): The amount to increase the battery by.
        """
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}%.")

    def __str__(self):
        """
        Returns a human-readable string representation of the smartphone object.

        Returns:
        str: A string describing the phone's brand, model, battery level, and status.
        """
        status = "ON" if self.is_on else "OFF"
        return f"{self.brand} {self.model} - Battery: {self.battery}%, Status: {status}"


class SmartphonePro(Smartphone):
    """
    A Pro version of Smartphone that inherits the base Smartphone
    class and adds extra features.
    """

    def take_photo(self):
        """
        Simulates taking a high-quality photo.
        This action only works if the smartphone is turned ON.
        """
        if self.is_on:
            print(f"{self.brand} {self.model} took a high-quality photo! 📸")
        else:
            print(f"Turn on your {self.brand} {self.model} first to take a photo.")


# ===========================
# ==== Demo Section =========
# ===========================
if __name__ == "__main__":
    # Create an instance of the base Smartphone class
    phone = Smartphone("Samsung", "Galaxy S24", 80)
    print(phone)  # Display phone details
    phone.power_on()  # Turn phone ON
    phone.charge(15)  # Charge the battery
    print(phone)  # Display updated phone details

    print("\n--- SmartphonePro Demo ---")
    # Create an instance of the SmartphonePro subclass
    pro_phone = SmartphonePro("Apple", "iPhone 15 Pro", 50)
    print(pro_phone)  # Display phone details
    pro_phone.take_photo()  # Try to take a photo while phone is OFF
    pro_phone.power_on()  # Turn phone ON
    pro_phone.take_photo()  # Take a photo while phone is ON