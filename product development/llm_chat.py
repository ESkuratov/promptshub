import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Загрузка предобученной модели и токенизатора
model_name = "gpt2"  # Вы можете заменить на другую модель, например, "gpt-neo", "gpt-3", и т.д.
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Убедимся, что модель работает на GPU, если он доступен
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_response(prompt, max_length=100):
    # Токенизация входного текста
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    # Генерация ответа
    outputs = model.generate(inputs['input_ids'], max_length=max_length, num_return_sequences=1)
    
    # Декодирование ответа
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main():
    print("Добро пожаловать в LLM-чат! Напишите 'выход' для завершения.")
    
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == 'выход':
            break
        
        response = generate_response(user_input)
        print(f"Модель: {response}")

if __name__ == "__main__":
    main()