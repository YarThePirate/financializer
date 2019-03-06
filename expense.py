from constants import freqs

class Expense:

    def __init__(self, name, amnt, freq, date=None):
        self.name = name
        self.amnt = float(amnt)
        self.freq = freqs[freq]
        self.date = date

    def to_monthly(self):
        if self.freq == "annual":
            return self._currency(self.amnt / 12.0)
        if self.freq == "semi-annual":
            return self._currency(self.amnt / 6.0)
        if self.freq == "monthly":
            return self.amnt
        if self.freq == "bi-weekly":
            return self._currency(self.amnt * 4.0)
        if self.freq == "weekly":
            return self._currency(self.amnt * 4.0)

    def to_annual(self):
        if self.freq == "annual":
            return self.amnt
        if self.freq == "semi-annual":
            return self._currency(self.amnt * 2.0)
        if self.freq == "monthly":
            return self._currency(self.amnt * 12)
        if self.freq == "bi-weekly":
            return self._currency(self.amnt * 26)
        if self.freq == "weekly":
            return self._currency(self.amnt * 52)

    def to_weekly(self):
        if self.freq == "annual":
            return self._currency(self.amnt / 52.0)
        if self.freq == "semi-annual":
            return self._currency(self.amnt / 26.0)
        if self.freq == "monthly":
            return self._currency(self.amnt / 4.0)
        if self.freq == "bi-weekly":
            return self._currency(self.amnt / 2.0)
        if self.freq == "weekly":
            return self.amnt

    def to_biweekly(self):
        if self.freq == "annual":
            return self._currency(self.amnt / 26.0)
        if self.freq == "semi-annual":
            return self._currency(self.amnt / 13.0)
        if self.freq == "monthly":
            return self._currency(self.amnt / 2.0)
        if self.freq == "bi-weekly":
            return self.amnt
        if self.freq == "weekly":
            return self._currency(self.amnt * 2.0)

    
    def _currency(self, num):
        return round(num, 2)
    
    def __repr__(self):
        return f"{self.name}; ${self.amnt} paid {self.freq}"
