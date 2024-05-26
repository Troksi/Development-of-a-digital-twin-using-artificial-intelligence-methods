
import json
import os
import glob

def process_line(line):
    data = json.loads(line)
    
    if 'messages' in data:
        messages = data['messages']
        request = [{"role": msg["role"], "text": msg["content"]} for msg in messages if msg["role"] != "assistant"]
        response = next((msg["content"] for msg in messages if msg["role"] == "assistant"), "")

        processed_data = {"request": request, "response": response}
        return json.dumps(processed_data, ensure_ascii=False)
    return None

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            processed_line = process_line(line)
            if processed_line:
                outfile.write(processed_line + '\n')

def main():
    input_directory = "telegram_messages_OkYasno\Datas"
    output_directory = "telegram_messages_OkYasno\Datas"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_type in ["ft_test*.jsonl","ft_train*.jsonl"]:
        input_files = glob.glob(os.path.join(input_directory, file_type))
        
        for input_path in input_files:
            filename = os.path.basename(input_path)
            output_filename = f"Y{filename}"
            output_path = os.path.join(output_directory, output_filename)
            process_file(input_path, output_path)

if __name__ == "__main__":
    main()
