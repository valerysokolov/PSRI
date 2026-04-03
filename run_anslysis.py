import json
import numpy as np
import sys
import os

# Принудительно исправляем пути для Pydroid 3
sys.path.append(os.getcwd())

try:
    from psri_core import PSRIEngine
except ImportError:
    print("Ошибка: Не найден файл psri_core.py в текущей папке!")
    sys.exit()

def main():
    # Определяем путь к папке, где лежит этот скрипт
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.json')

    if not os.path.exists(config_path):
        print(f"Ошибка: Файл не найден по пути: {config_path}")
        return

    with open(config_path, 'r') as f:
        data = json.load(f)
    
    # ... далее остальной код без изменений





#def main():
 #   if not os.path.exists('config.json'):
#        print("Ошибка: Файл config.json не найден!")
     #   return

    with open('config.json', 'r') as f:
        data = json.load(f)
    
    c = data['expert_comparisons']
    # Матрица на основе экспертных оценок
    matrix = np.array([
        [1,               c['inst_vs_econ'], c['inst_vs_soc']],
        [1/c['inst_vs_econ'], 1,               c['econ_vs_soc']],
        [1/c['inst_vs_soc'],  1/c['econ_vs_soc'], 1]
    ])
    
    engine = PSRIEngine()
    weights, cr = engine.calculate_priority_vector(matrix)
    
    metrics = data['current_metrics']
    stats = np.array([
        metrics['institutional_strength'],
        metrics['economic_adaptability'],
        metrics['social_cohesion']
    ])
    
    total_score = np.dot(weights, stats)
    
    print(f"\n--- PSRI Report: {data['country']} ---")
    print(f"Weights: Inst={weights[0]:.2f}, Econ={weights[1]:.2f}, Soc={weights[2]:.2f}")
    print(f"CR: {cr:.2%} {'(OK)' if cr < 0.1 else '(Inconsistent!)'}")
    print(f"RESULT: {total_score:.2f} -> {engine.get_status(total_score)}\n")

if __name__ == "__main__":
    main()
