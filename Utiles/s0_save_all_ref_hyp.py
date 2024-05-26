import json

def read_jsonl_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def combine_responses(file_path_1, file_path_2, file_path_3, output_path):
    data_1 = read_jsonl_file(file_path_1)
    data_2 = read_jsonl_file(file_path_2)
    data_3 = read_jsonl_file(file_path_3)

    combined_data = []

    for item_1, item_2, item_3 in zip(data_1, data_2, data_3):
        request_text_1 = next((msg['text'] for msg in item_1['request'] if msg['role'] == 'user'), None)
        response_1 = item_1.get('response', '')
        
        request_text_2 = next((msg['text'] for msg in item_2['request'] if msg['role'] == 'user'), None)
        response_2 = item_2.get('response', '')

        request_text_3 = next((msg['text'] for msg in item_3['request'] if msg['role'] == 'user'), None)
        response_3 = item_3.get('response', '')
        #{"request": [{"role": "system", "text": "Марина Волкова, психоаналитический терапевт, психолог"}, {"role": "user", "text": "Что такое фрустрация?"}], "response":
        if request_text_1 == request_text_2:
            combined_data.append({
                "request": request_text_1,
                "ref": response_1,
                "pro": response_2,
                "trm": response_3
            })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    file_path_1 = 'telegram_messages_OkYasno\Datas\Yft_all_mv.jsonl' #Yft_all_mv #Yft_answe_same_mv
    file_path_2 = 'telegram_messages_OkYasno\Datas\Yft_answe_pro_mv.jsonl' #Yft_answe_pro_mv #Yft_ansve_mv
    file_path_3 = 'telegram_messages_OkYasno\Datas\Yft_answe_tr_te_mv.jsonl' #Yft_answe_pro_mv #Yft_ansve_mv
    output_path = 'telegram_messages_OkYasno\Datas\mv_result.json'

    combine_responses(file_path_1, file_path_2, file_path_3, output_path)
