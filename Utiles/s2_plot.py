import json
import os
import matplotlib.pyplot as plt

def load_data(file_paths):
    data = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            data.extend(json.load(f))
    return data

def filter_data_by_metric(data, metric_name):
    filtered_data = []
    for entry in data:
        for metric in entry['metrics']:
            if metric['name'] == metric_name:
                filtered_data.append({
                    'request': entry['request'],
                    'score': metric['score']
                })
                break
    return filtered_data

def plot_metric(data1, data2, data3, metric_name):
    requests = [entry['request'] for entry in data1]
    print(requests[0])
    exit()
    scores1 = [entry['score'] for entry in data1]
    scores2 = [entry['score'] for entry in data2]
    scores3 = [entry['score'] for entry in data3]

    x = range(len(requests))

    plt.figure(figsize=(12, 6))
    plt.plot(x, scores1, label='score_pro', marker='o')
    plt.plot(x, scores2, label='score_trm', marker='o')
    #plt.plot(x, scores3, label='File 3', marker='o')

    plt.xlabel('Requests')
    plt.ylabel('Scores')
    plt.title(f'Сравнение результатов по метрики {metric_name}')
    plt.xticks(x, requests, rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Путь к файлам JSON
    file_paths = [
        r'Utiles\telegram_messages_OkYasno\Datas\mv_result_score_pro.json',
        r'Utiles\telegram_messages_OkYasno\Datas\mv_result_score_trm.json',
        r'Utiles\telegram_messages_OkYasno\Datas\mv_result_score_pro.json'
    ]
    # Загрузка данных из файлов
    data = load_data(file_paths)
    
    # Выбранная метрика
    selected_metric = 'ROUGE'
    
    # Фильтрация данных по метрике
    data1 = filter_data_by_metric(data[:len(data)//3], selected_metric)
    data2 = filter_data_by_metric(data[len(data)//3:2*len(data)//3], selected_metric)
    data3 = filter_data_by_metric(data[2*len(data)//3:], selected_metric)
    
    # Построение графика
    plot_metric(data1, data2, data3, selected_metric)
