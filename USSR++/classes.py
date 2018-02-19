"""
File for all the classes used in USSR++.

It contains the following:

- Worker
- Factory
- Parse Node
"""

"""Imports..."""
import tables

class Worker:
    """
    The Worker class.

    This class is essentially the heart and
    soul of USSR++. It is what is required to
    make things happen (i.e. printing, math, etc.).
    """
    def __init__(
        self,
        name,
        job
    ):
        """Initialization."""
        # Error checking...
        if type(name) != str: raise TypeError("argument 'name' is not of type 'str'")
        if type(job) != str: raise TypeError("argument 'job' is not of type 'str'")

        # Variables...
        self.name = name
        self.job = tables.JOB_FUNC[job]
        self.pay = tables.JOB_PAY[job]
        self.hours = 0

    def add_to_hrs(self):
        self.hours += 1
        self.repayment = self.pay * self.hours

    def reset_hrs_and_repay(self):
        self.hours = 0
        self.repayment = 0

class Factory:
    """
    The Factory class.

    This class is an upgraded Worker class.
    It's more "efficient" at doing tasks, so you can say, print
    a 96-character long string in one day, but at the cost at a
    higher pay.
    """
    def __init__(
        self,
        name,
        job
    ):
        """Initialization."""
        # Error checking...
        if type(name) != str: raise TypeError("argument 'name' is not of type 'str'")
        if type(job) != str: raise TypeError("argument 'job' is not of type 'str'")

        # Variables...
        self.name = name
        self.job = tables.JOB_FUNC[job]
        self.pay = tables.JOB_PAY[job] * 4
        self.hours = 0
        self.repayment = 0

    def add_to_hrs(self):
        self.hours += 0.25
        self.repayment = self.pay * self.hours

    def reset_hrs_and_repay(self):
        self.hours = 0
        self.repayment = 0

"""
class ParseNode(object):
    \"""
    The Parse Node.

    Used in the parser as part of an AST.
    \"""
    def __init__(
        self
    )
"""      
