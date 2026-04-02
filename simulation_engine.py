import numpy as np

def run_stress_test(weights, base_stats, shock_factor, impact_value):
    """
    weights: вектор весов
    base_stats: текущие показатели [Inst, Econ, Soc]
    shock_factor: индекс фактора (0, 1 или 2)
    impact_value: на сколько баллов падает показатель
    """
    new_stats = base_stats.copy()
    new_stats[shock_factor] -= impact_value
    if new_stats[shock_factor] < 0: new_stats[shock_factor] = 0
    
    old_score = np.dot(weights, base_stats)
    new_score = np.dot(weights, new_stats)
    
    return old_score, new_score

# Пример использования:
weights = np.array([0.64, 0.26, 0.10]) # Силовая модель
current = np.array([90, 50, 40])       # Текущее состояние

print("--- СЦЕНАРНЫЙ АНАЛИЗ (STRESS TEST) ---")
# Шок в экономике на 30 баллов
old, new = run_stress_test(weights, current, 1, 30)
print(f"Шок экономики (-30): {old:.2f} -> {new:.2f} (Падение: {old-new:.2f})")

# Шок в силовом блоке на 30 баллов
old, new = run_stress_test(weights, current, 0, 30)
print(f"Раскол элит (-30):    {old:.2f} -> {new:.2f} (Падение: {old-new:.2f})")
