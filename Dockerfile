# 1. Негізгі образ (Python орнатылған)
FROM python:3.10

# 2. Жұмыс қалтасы
WORKDIR /app

# 3. Барлық файлдарды контейнерге көшіру
COPY . .

# 4. Flask орнату
RUN pip install flask

# 5. Қолданбаны іске қосу
CMD ["python", "app.py"]
