import json
import os
import matplotlib.pyplot as plt


def plot_metric(data0, data1, data2, data3, metric_name):
    requests = data0
    scores1 = data1
    scores2 = data2
    scores3 = data3

    x = range(len(requests))

    plt.figure(figsize=(12, 6))
    plt.plot(x, scores1, label='ref', marker='o')
    plt.plot(x, scores2, label='pro', marker='o')
    plt.plot(x, scores3, label='trm', marker='o')

    plt.xlabel('Requests')
    plt.ylabel('Scores')
    plt.title(f'Сравнение результатов по растоянию векторов')
    plt.xticks(x, requests, rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Путь к файлам JSON
    file_path = r'Utiles\telegram_messages_OkYasno\Datas\mv_embanding_cos.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
   
       # Выбранная метрика
    selected_metric = 'BLEU'
    
    # Фильтрация данных по метрике
    data0 = [el['request'] for el in data]
    data1 = [el['ref_score'] for el in data]
    data2 = [el['pro_score'] for el in data]
    data3 = [el['trm_score'] for el in data]
    
    # Построение графика
    plot_metric(data0, data1, data2, data3, selected_metric)
