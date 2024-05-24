import os
import re
import json

def collect_questions_answers(base_directory):
    question_pattern = re.compile(r'(.*?)✔️Отвечает', re.DOTALL)
    answer_pattern = re.compile(r'✔️Отвечает.*?«Ясно»(.*)', re.DOTALL)

    # Проверяем, существует ли указанный каталог
    if not os.path.isdir(base_directory):
        print(f"Directory does not exist: {base_directory}")
        return

    unsplited = []
    # Проходим по всем подкаталогам в базовом каталоге
    for subdir in os.listdir(base_directory):
        subdir_path = os.path.join(base_directory, subdir)
        if os.path.isdir(subdir_path):
            output_jsonl = os.path.join(subdir_path, 'questions_answers.jsonl')
            with open(output_jsonl, 'w', encoding='utf-8') as jsonl_file:
                for filename in os.listdir(subdir_path):
                    if filename.endswith('.txt'):
                        file_path = os.path.join(subdir_path, filename)
                        
                        try:
                            with open(file_path, 'r', encoding='utf-8') as file:
                                content = file.read()
 
                            # Ищем вопрос в содержимом файла
                            question_match = question_pattern.search(content)
                            # Ищем ответ в содержимом файла
                            answer_match = answer_pattern.search(content)
                            print(f'{subdir}: {bool(question_match)} {bool(answer_match)}')
                            if question_match and answer_match:
                                question = question_match.group(1).strip()
                                answer = answer_match.group(1).strip()

                                if question and answer:
                                    # Создаем запись в формате JSONL #TODO: нужно в  указать не имя, а все что вместо Отвечает и Ясно
                                    message = {
                                        "messages": [
                                            {"role": "system", "content": subdir},
                                            {"role": "user", "content": question},
                                            {"role": "assistant", "content": answer}
                                        ]
                                    }
                                    jsonl_file.write(json.dumps(message, ensure_ascii=False) + '\n')
                                    print(f"Added Q&A from {file_path}")
                                else:
                                    unsplited.add({'subdir':subdir,'filename':filename})
                        except Exception as e:
                            print(f"Failed to process file: {file_path} due to {e}")
                            print(unsplited)
    print(unsplited)

# Пример использования функции
base_directory = 'telegram_messages_OkYasno\Психологи\Более 10'
collect_questions_answers(base_directory)

# content = '''Как заставить себя сделать то, что вызывает отвращение? В моём случае это учёба в университете. Отторжение настолько сильное, что всё доходит до истерик и желания исчезнуть. ✔️Отвечает Александр Самойличенко, гештальт-терапевт, психолог сервиса «Ясно» «Заставить»‎ себя можно только одним способом — снизить чувствительность к отвращению. Но если мы обнаружили себя в ситуации, которая вызывает такой дискомфорт, это значит, что наша чувствительность уже снижена. И потому мы «проглотили» то, что нам не подходит. Обычно мы учимся игнорировать отвращение в семье. Например, членам семьи приходилось ухаживать за родным с алкогольной зависимостью — несмотря на его неприглядный вид и запах алкоголя. Это было таким негласным правилом «общежития»: терпеть избыточную близость человека, приносящего дискомфорт. Влияет и культура дефицита: в ней жили практически все наши родители и старшее поколение. Это когда принято больше принимать, чем отказываться: «Бери, пока дают». Отказ расценивался как беспечность или каприз. Сейчас ситуация иная — мы живём в эпоху профицита, когда на каждом углу предлагают новые курсы, эко еду и декор для дома. И основа комфортной жизни — способность отказываться. Отказаться — значит быть в контакте со своим отвращением, быть чувствительным к нему и не «приглушать» его. Но как к этому прийти? Прежде чем рубить сплеча и отменять всё, что не подходит, можно поисследовать своё отвращение. В этом поможет простой вопрос: «Чего в моей жизни много?». Мы часто концентрируемся на том, чего не хватает, но забываем о той ноше, которую нести уже тяжело. Это могут быть советы, которых вы не просили; излишняя строгость в учёбе, которая для вас не настолько важна, как для преподавателей или родителей; избыточная забота. Смысл этой практики в том, чтобы приблизиться к своим подлинным чувствам, набраться смелости — и отходить от того, что дискомфортно.'''
# question_pattern = re.compile(r'(.*?)✔️Отвечает', re.DOTALL)
# answer_pattern = re.compile(r'✔️Отвечает.*?«Ясно»(.*)', re.DOTALL)
# question_match = question_pattern.search(content)
# answer_match = answer_pattern.search(content)
# print(bool(question_match))
# print(bool(answer_match))
# answer = answer_match.group(1).strip()
# print(answer)
# question = question_match.group(1).strip()
# print(question)
