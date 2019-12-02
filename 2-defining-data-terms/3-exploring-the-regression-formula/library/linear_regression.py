from optimizer import Optimizer
class LinearRegressionModel:
    def fit(self, x_values, y_values, intercept, start, stop, step_count):
        optimizer = Optimizer(x_values, y_values, intercept, start, stop, step_count)
        optimizer.set_hypotheses()
        optimizer.set_losses()
        min_loss = optimizer.find_min()
        self.hypothesis = min_loss.hypothesis
        return self.hypothesis
    
