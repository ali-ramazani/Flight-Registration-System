class Aircraft:
    """ Aircraft class with registration, model, number of rows, and number of seats per row """

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        """ Returns aircraft registration """
        return self._registration

    def model(self):
        """ Returns aircraft model """
        return self._model

    def seating_plan(self):
        """ Returns aircraft seating plan """
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])