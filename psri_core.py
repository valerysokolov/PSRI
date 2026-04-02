import numpy as np

class PSRIEngine:
    @staticmethod
    def calculate_priority_vector(matrix):
        n = matrix.shape[0]
        # Метод нормализации среднего геометрического
        geom_mean = np.exp(np.log(matrix).mean(axis=1))
        weights = geom_mean / geom_mean.sum()
        
        # Индекс согласованности
        lambda_max = np.mean(np.dot(matrix, weights) / weights)
        ci = (lambda_max - n) / (n - 1)
        return weights, ci

    @staticmethod
    def get_status(score):
        if score > 80: return "RESILIENT (Green)"
        if score > 60: return "STABLE (Yellow)"
        if score > 40: return "FRAGILE (Orange)"
        return "CRITICAL (Red)"
