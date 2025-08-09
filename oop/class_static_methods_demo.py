# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Does not use class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Has access to class-level data."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
