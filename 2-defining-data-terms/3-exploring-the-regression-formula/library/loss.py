from plots import trace_values
class Loss():
    def __init__(self, hypothesis, x_values, y_values):
        self.hypothesis = hypothesis
        self.x_values = x_values
        self.y_values = y_values
        
    def errors(self):
        expecteds = self.hypothesis.predict()
        pairs = list(zip(self.y_values, expecteds))
        return [actual - expected for actual, expected in pairs]
    
    def squared_errors(self):
        return [error**2 for error in self.errors()]
    
    def rss(self):
        return sum(self.squared_errors())

    def error_traces_and_hypothesis(self):
        data_trace = trace_values(self.x_values, self.y_values)
        return [data_trace, self.hypothesis.trace(), *self.error_traces()]

    def error_traces(self):
        coords_and_errors = list(zip(self.x_values, self.y_values, self.errors()))
        return [self.error_trace(x, y, error) for x, y, error in coords_and_errors]

    def error_trace(self, x, y, error):
        name = 'error at ' + str(x)
        return {'x': [x, x], 'y': [y - error, y], 'mode': 'lines', 
                'marker': {'color': 'red'}, 'name': name, 'text': [error], 
                'textposition':'top right', 'hoverinfo': 'none'}


