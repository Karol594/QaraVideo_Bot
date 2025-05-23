# Python негізинде образ
FROM python:3.10-slim

# Жумыс директориясын орнатамыз
WORKDIR /app

# Барлық файлларды контейнерге көшіремиз
COPY . .

# Тәуелдиликлерди орнатамыз
RUN pip install --no-cache-dir -r requirements.txt

# Порт
ENV PORT=8080

# Бастау командасы
CMD ["python3", "main.py"]
