class Hypothesis():
    def __init__(self, coef_ = None, intercept_ = None, x_values = None):
        self.coef_ = coef_
        self.intercept_ = intercept_
        self.x_values = x_values
    
    def predict(self):
        return [self.predict_value(value) for value in self.x_values]
    
    def predict_value(self, value):
        return self.coef_*value + self.intercept_

    def trace(self, mode = 'lines', name=None, text = []):
        coef_text = f"y = {self.coef_}x"
        intercept_text = f" + {self.intercept_}"
        default_text = coef_text + intercept_text if self.intercept_ else coef_text
        text = name or default_text
        return {'x': self.x_values, 'y': self.predict(), 'mode': mode, 'name': name, 'text': text}
