class DummyModel:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, X):
        return 1


def train(X, y):
    model = DummyModel()
    model.fit(X, y)
    model.predict(X)
    return model
