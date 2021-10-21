"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a number generator starting at start"""
        self.start = self.next = start

    def __repr__(self):
        """show presentation """
        f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self)
        """generate number increasing by 1 """
        self.next += 1
        return self.next -1
    def reset(self)
    """set generator back to start """
        self.next = self.start    
