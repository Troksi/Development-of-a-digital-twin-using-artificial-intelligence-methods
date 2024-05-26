import json
import os
import glob

def filter_long_responses(input_path):
    valid_entries = []
    count_deleted = 0
    with open(input_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            data = json.loads(line)
            if 'response' in data and len(data['response']) <= 2000:
                valid_entries.append(data)
            else:
                len_resp = len(data['response'])
                print(f'delete from: {input_path} becose len: {len_resp}')
                count_deleted += 1
    print(f'{count_deleted=}')
    return valid_entries

def save_filtered_data(output_path, valid_entries):
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for entry in valid_entries:
            outfile.write(json.dumps(entry, ensure_ascii=False) + '\n')

def process_files(input_directory):
    for file_type in ["Yft_test*.jsonl","Yft_train*.jsonl"]:
        input_files = glob.glob(os.path.join(input_directory, file_type))

        for input_path in input_files:
            valid_entries = filter_long_responses(input_path)
            save_filtered_data(input_path, valid_entries)

if __name__ == "__main__":
    input_directory = "telegram_messages_OkYasno\Datas"
    process_files(input_directory)
