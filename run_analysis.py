import json
import numpy as np
from psri_core import PSRIEngine

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def main():
    data = load_config('config.json')
    
    # Извлекаем сравнения
    c = data['expert_comparisons']
    
    # Строим матрицу 3x3 на основе JSON
    matrix = np.array([
        [1,               c['inst_vs_econ'], c['inst_vs_soc']],
        [1/c['inst_vs_econ'], 1,               c['econ_vs_soc']],
        [1/c['inst_vs_soc'],  1/c['econ_vs_soc'], 1]
    ])
    
    engine = PSRIEngine()
    weights, cr = engine.calculate_priority_vector(matrix)
    
    # Считаем финальный индекс
    metrics = data['current_metrics']
    stats = np.array([
        metrics['institutional_strength'],
        metrics['economic_adaptability'],
        metrics['social_cohesion']
    ])
    
    total_score = np.dot(weights, stats)
    
    # Вывод отчета
    print(f"=== PSRI Analysis Report: {data['country']} ({data['year']}) ===")
    print(f"Weights: Inst: {weights[0]:.2f}, Econ: {weights[1]:.2f}, Soc: {weights[2]:.2f}")
    print(f"Consistency Ratio (CR): {cr:.2%}")
    print(f"FINAL INDEX SCORE: {total_score:.2f}")
    print(f"SYSTEM STATUS: {engine.get_status(total_score)}")

if __name__ == "__main__":
    main()
