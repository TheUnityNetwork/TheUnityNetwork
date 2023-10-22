# ethical_metrics_enhancements.py

class EthicalMetrics:
    def __init__(self, environmental_responsibility, social_equality, economic_fairness, transparency):
        self._validate_metric(environmental_responsibility)
        self._validate_metric(social_equality)
        self._validate_metric(economic_fairness)
        self._validate_metric(transparency)
        
        self._environmental_responsibility = environmental_responsibility
        self._social_equality = social_equality
        self._economic_fairness = economic_fairness
        self._transparency = transparency

    def _validate_metric(self, metric_value):
        if not isinstance(metric_value, (int, float)):
            raise ValueError("Metric value must be a number")
        if metric_value < 0 or metric_value > 100:
            raise ValueError("Metric value must be between 0 and 100")

    @property
    def environmental_responsibility(self):
        return self._environmental_responsibility

    @property
    def social_equality(self):
        return self._social_equality

    @property
    def economic_fairness(self):
        return self._economic_fairness

    @property
    def transparency(self):
        return self._transparency