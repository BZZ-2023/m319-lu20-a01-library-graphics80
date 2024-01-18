from dataclasses import dataclass
from datetime import datetime

@dataclass
class Rental:
    rental_date: datetime
    return_date: datetime
    num_rental_days: int

    @property
    def cost(self):
        """
        Caculate the cost of the rental
        :return: rentalcost
        """
        base_cost = 4.50
        overdue_days = (self.return_date - self.rental_date).days - self.num_rental_days
        if overdue_days < 0:
            overdue_days == 0
        penalty = 3.35 * overdue_days
        return base_cost + penalty