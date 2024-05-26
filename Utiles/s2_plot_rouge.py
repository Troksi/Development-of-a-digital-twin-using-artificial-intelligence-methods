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

#  {
#                 "name": "ROUGE",
#                 "ref": "ref",
#                 "hyp": "trm",
#                 "score": [
#                     {
#                         "name": "rouge-1",
#                         "r": 0.17204301075268819,
#                         "p": 0.21476510067114093,
#                         "f": 0.19104477118039667
#                     },
                    
def plot_metric(data1, data2, metric_name):
    requests = [entry['request'] for entry in data1]
    scores11 = [entry['score'][2]['p'] for entry in data1]
    scores21 = [entry['score'][2]['p'] for entry in data2]
    scores12 = [entry['score'][2]['r'] for entry in data1]
    scores22 = [entry['score'][2]['r'] for entry in data2]
    scores13 = [entry['score'][2]['f'] for entry in data1]
    scores23 = [entry['score'][2]['f'] for entry in data2]

    x = range(len(requests))

    plt.figure(figsize=(12, 6))
    # plt.plot(x, scores11, label='pro_p', marker='o')
    # plt.plot(x, scores21, label='trm_p', marker='o')
    # plt.plot(x, scores13, label='pro_f', marker='o')
    # plt.plot(x, scores23, label='trm_f', marker='o')
    plt.plot(x, scores12, label='pro_r', marker='o')
    plt.plot(x, scores22, label='trm_r', marker='o')
    #plt.plot(x, scores3, label='File 3', marker='o')

    plt.xlabel('Requests')
    plt.ylabel('Scores')
    plt.title(f'Сравнение результатов по метрики {metric_name}-L')
    plt.xticks(x, requests, rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Путь к файлам JSON
    file_paths1 = r'Utiles\telegram_messages_OkYasno\Datas\mv_result_score_pro.json'
    file_paths2 = r'Utiles\telegram_messages_OkYasno\Datas\mv_result_score_trm.json'

    with open(file_paths1, 'r', encoding='utf-8') as f:
       data1 = json.load(f)

    with open(file_paths2, 'r', encoding='utf-8') as f:
       data2 = json.load(f)
    
    # Выбранная метрика
    selected_metric = 'ROUGE'
    
    data1 = filter_data_by_metric(data1, selected_metric)
    data2 = filter_data_by_metric(data2, selected_metric)
	
	
    # Построение графика
    plot_metric(data1, data2, selected_metric)
