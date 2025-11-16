from typing import Any as Incomplete

logger: Incomplete

def run_random_search(estimator, param_distributions, X_train, y_train, n_iter: int = 10, cv: int = 5, scoring=None): ...