import numpy as np


class CrossEntropy:
    @staticmethod
    def error(outputs, targets):
        batch_size = len(outputs)
        cross_entropies = - np.sum(targets * np.log(outputs), axis=1)
        return cross_entropies.reshape(batch_size, 1), cross_entropies.sum() / batch_size


    @staticmethod
    def derivative(outputs, targets):
        return np.where(outputs != 0, -targets/outputs, 0.0)