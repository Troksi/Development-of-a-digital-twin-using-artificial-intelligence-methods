import unittest
from prompt_split import prompts_split 

class TestPromptsSplit(unittest.TestCase):
    
    def test_less_than_step_for_split(self):
        # Проверяем, что если входной список меньше чем step_for_split, то функция возвращает его без изменений
        input_list = ["This is a short text."]
        expected_output = [input_list]
        self.assertEqual(prompts_split(input_list), expected_output)
        
    def test_split_text(self):
        # Проверяем, что текст разбивается на части правильно и добавляются промпты между частями
        input_list = ["This is a long text that needs to be split into multiple parts for sending.", "Each part should not exceed the character limit."]
        expected_output = [
            "Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as 'Part 1/2 received' and wait for the next part.\n[START PART 1/2]\nThis is a long text that needs to be split into multiple parts for sending.\n[END PART 1/2]\nRemember not answering yet. Just acknowledge you received this part with the message 'Part 1/2 received' and wait for the next part.",
            "Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as 'Part 2/2 received' and wait for the next part.\n[START PART 2/2]\nEach part should not exceed the character limit.\n[END PART 2/2]\nRemember not answering yet. Just acknowledge you received this part with the message 'Part 2/2 received' and wait for the next part."
        ]
        self.assertEqual(prompts_split(input_list), expected_output)
    
    def test_empty_list(self):
        # Проверяем, что если входной список пустой, то функция возвращает пустой список
        input_list = []
        expected_output = []
        self.assertEqual(prompts_split(input_list), expected_output)
        
if __name__ == '__main__':
    #unittest.main()
    print(prompts_split(['1','2']))