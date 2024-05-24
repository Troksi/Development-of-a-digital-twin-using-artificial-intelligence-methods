from sklearn.metrics import accuracy_score, f1_score

# Получение предсказаний
predictions = trainer.predict(tokenized_dataset['test'])
preds = predictions.predictions.argmax(-1)

# Вычисление метрик
labels = tokenized_dataset['test']['labels']
accuracy = accuracy_score(labels, preds)
f1 = f1_score(labels, preds, average='weighted')

print(f'Accuracy: {accuracy}')
print(f'F1 Score: {f1}')
