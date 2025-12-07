class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Does NOT access class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Has access to class-level data."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
