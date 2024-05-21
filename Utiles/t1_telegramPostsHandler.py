import json


def process_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Create a new dictionary to store the processed data
    processed_data = {
        'name': data.get('name'),
        'id': data.get('id'),
        'messages': []
    }
    
    # Process each message
    for message in data.get('messages', []):
        processed_message = {
            'id': message.get('id'),
            'type': message.get('type'),
            'date': message.get('date'),
            'date_unixtime': message.get('date_unixtime'),
            'from': message.get('from'),
            'from_id': message.get('from_id'),
            'text': ''
        }
        
        # Collect and concatenate text from text_entities
        texts = [entity.get('text', '') for entity in message.get('text_entities', []) if entity.get('type') != 'custom_emoji']
        processed_message['text'] = ''.join(texts)
        
        processed_data['messages'].append(processed_message)
    
    return processed_data

def save_processed_json(processed_data, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(processed_data, file, ensure_ascii=False, indent=4)

# Example usage
input_file = 'result.json'
output_file = 'processed_result.json'

processed_data = process_json(input_file)
save_processed_json(processed_data, output_file)
