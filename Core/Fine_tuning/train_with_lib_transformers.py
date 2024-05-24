from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments

# Загружаем модель и токенизатор
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Подготовка данных
def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True)

# Подготовка тренировочного и тестового наборов данных
from datasets import load_dataset
dataset = load_dataset('your_dataset')
tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Настройки тренировки
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Тренировка модели
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['test']
)

trainer.train()
