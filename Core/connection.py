import sys
import os
import openai

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from constants import YOUR_OPENAI_API_KEY, YOUR_OPENAI_API_ORGANIZATION, MODEL_3_5
from logger import gpt_logger, gpt_debug_logger

class Embedding():
    
    openai_key = YOUR_OPENAI_API_KEY
    organization = YOUR_OPENAI_API_ORGANIZATION
    model = MODEL_3_5

    def __init__(self, openai_key=openai_key, organization=organization, model=model):
        self.openai_key = openai_key
        self.organization = organization
        self.model = model

        #openai.organization = self.organization
        openai.api_key = self.openai_key
        
        
    def get_response(self, prompt, role="user"):
        # response = openai.Completion.create(
        #     engine="davinci-codex",
        #     prompt=prompt,
        #     temperature=0.5,
        #     max_tokens=100,
        #     top_p=1.0,
        #     frequency_penalty=0.0,
        #     presence_penalty=0.0,
        #     stop=["\n"]
        # )
        response = openai.ChatCompletion.create(
        model=self.model,
        messages=[
             {"role": role, "content": prompt}
             ],
        temperature=0,
        )
        return response
        
    def get_response_with_history(self, history, prompt, role="user"):
        messages = history
        messages.append({"role": role, "content": prompt})

        response = openai.ChatCompletion.create(
        model=self.model,
        messages=messages,
        temperature=0,
        )
        return response

def get_gpt_answer(prompt="Who is the CEO of Google?", history=[], role='user', organization = '', model=MODEL_3_5):
    if len(prompt) >= 15000:
        print('WARING: prompt exceeds 15000 characters')
        gpt_logger.warring('WARING: prompt exceeds 15000 characters')
        
    try:
        openai_key =  YOUR_OPENAI_API_KEY        
        embedding = Embedding(openai_key,organization,model)
        # responses = embedding.get_response(prompt) # without history
        responses = embedding.get_response_with_history(history=history,prompt=prompt, role=role)
        gpt_debug_logger.debug(f'USER: {prompt}')
        gpt_debug_logger.debug(f'GPT-{model}: {responses.choices[0].message.content}')
        print(f'USER: {prompt}')
        print(f'GPT-{model}: {responses.choices[0].message.content}')
        return responses.choices[0].message.content
    except Exception as e:
        print(f'WARING: in get gpt answer: {e}')
        gpt_logger.warning(f'WARING: in get gpt answer: {e}')
