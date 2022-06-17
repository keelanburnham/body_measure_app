class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, weight):
        try:
            self.model.weight = weight
            self.model.save()
        except ValueError as error:
            print(error)