import json
import numpy as np
import os
import sys

# Настройка путей для Pydroid 3
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
from psri_core import PSRIEngine

def get_input(prompt, default):
    res = input(f"{prompt} [По умолчанию: {default}]: ")
    return res if res else default

def main():
    engine = PSRIEngine()
    print("=== PSRI TERMINAL v2.0 (2026) ===")
    
    mode = input("Загрузить config.json (1) или ввести новые данные (2)? [1/2]: ")
    
    if mode == '1':
        config_path = os.path.join(current_dir, 'config.json')
        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        # Интерактивный ввод данных экспертом
        data = {
            "country": get_input("Введите название страны", "Latvia"),
            "year": 2026,
            "expert_comparisons": {
                "inst_vs_econ": float(get_input("Важность Институтов над Экономикой (1-9)", 2.0)),
                "inst_vs_soc": float(get_input("Важность Институтов над Обществом (1-9)", 4.0)),
                "econ_vs_soc": float(get_input("Важность Экономики над Обществом (1-9)", 2.0))
            },
            "current_metrics": {
                "institutional_strength": float(get_input("Метрика Институтов (0-100)", 80)),
                "economic_adaptability": float(get_input("Метрика Экономики (0-100)", 60)),
                "social_cohesion": float(get_input("Метрика Общества (0-100)", 55))
            }
        }

    # Математический расчет
    c = data['expert_comparisons']
    matrix = np.array([
        [1,               c['inst_vs_econ'], c['inst_vs_soc']],
        [1/c['inst_vs_econ'], 1,               c['econ_vs_soc']],
        [1/c['inst_vs_soc'],  1/c['econ_vs_soc'], 1]
    ])
    
    weights, cr = engine.calculate_priority_vector(matrix)
    metrics = np.array([
        data['current_metrics']['institutional_strength'],
        data['current_metrics']['economic_adaptability'],
        data['current_metrics']['social_cohesion']
    ])
    
    total_score = np.dot(weights, metrics)
    
    # Отчет
    print(f"\n" + "="*40)
    print(f" ОТЧЕТ PSRI: {data['country']} ({data['year']})")
    print("-" * 40)
    print(f" Веса факторов: Инст={weights[0]:.2f}, Экон={weights[1]:.2f}, Соц={weights[2]:.2f}")
    print(f" Согласованность (CR): {cr:.2%} {'[OK]' if cr < 0.1 else '[ВНИМАНИЕ! Проверьте логику]'}")
    print("-" * 40)
    print(f" ИТОГОВЫЙ ИНДЕКС: {total_score:.2f}")
    print(f" СТАТУС СИСТЕМЫ: {engine.get_status(total_score)}")
    print("="*40)

    save = input("\nСохранить эти данные в config.json? (y/n): ")
    if save.lower() == 'y':
        with open(os.path.join(current_dir, 'config.json'), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("Данные обновлены в config.json")

if __name__ == "__main__":
    main()
