import json
import numpy as np

def calculate_cosine_simelar(vec_a, vec_b):

    dot_prod = np.dot(vec_a, vec_b)

    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)

    cos_similarity = dot_prod / (norm_a * norm_b)
    
    return cos_similarity

input_file_path_ref = r'Utiles\telegram_messages_OkYasno\Datas\mv_result_embanding_ref.json'
input_file_path_pro = r'Utiles\telegram_messages_OkYasno\Datas\mv_result_embanding_pro.json'
input_file_path_trm = r'Utiles\telegram_messages_OkYasno\Datas\mv_result_embanding_trm.json'

mv_embanding_cos = r'Utiles\telegram_messages_OkYasno\Datas\mv_embanding_cos.json'

with open(input_file_path_ref, 'r', encoding='utf-8') as f:
        data_ref = json.load(f)

with open(input_file_path_pro, 'r', encoding='utf-8') as f:
        data_pro = json.load(f)

with open(input_file_path_trm, 'r', encoding='utf-8') as f:
        data_trm = json.load(f)

print(len(data_ref))
print(len(data_pro))
print(len(data_trm))

updated_data = []
for i in range(len(data_ref)):
    if data_ref[i]['request']==data_pro[i]['request']==data_trm[i]['request']:

        ref_score = calculate_cosine_simelar(np.array(data_ref[i]['ref']),np.array(data_ref[i]['ref']))
        pro_score = calculate_cosine_simelar(np.array(data_pro[i]['pro']),np.array(data_ref[i]['ref']))
        trm_score = calculate_cosine_simelar(np.array(data_trm[i]['trm']),np.array(data_ref[i]['ref']))

        updated_item = {
            "request": data_ref[i]['request'],
            "ref_score": ref_score,  # Обновляем поле "ref" с результатом
            "pro_score": pro_score,
            "trm_score": trm_score
        }
        updated_data.append(updated_item)
    
with open(mv_embanding_cos, 'w', encoding='utf-8') as f:
    json.dump(updated_data, f, ensure_ascii=False, indent=4)


        #print(calculate_cosine_simelar(np_data1,np_data2))