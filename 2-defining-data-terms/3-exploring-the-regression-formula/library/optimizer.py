from hypothesis import Hypothesis
from loss import Loss
class Optimizer:
    def __init__(self, x_values, y_values, intercept, start, stop, step_count):
        self.x_values = x_values
        self.y_values = y_values
        self.intercept = intercept
        self.start = start
        self.stop = stop
        self.step_count = step_count

    def steps(self):
        step_size = (self.stop - self.start)/self.step_count
        steps = []
        for count in list(range(0, self.step_count)):
            steps.append(self.start + count*step_size)
        return steps

    def set_hypotheses(self):
        coefs = self.steps()
        self.hypotheses = [Hypothesis(coef, self.intercept, self.x_values) for coef in coefs]

    def set_losses(self):
        self.losses = [Loss(hypothesis, self.x_values, self.y_values) for hypothesis in self.hypotheses]

    def find_min(self):
        return min(self.losses, key = lambda loss: loss.rss())




