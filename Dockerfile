FROM python:3.11-slim

RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

WORKDIR /strongfitness

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN IS_BUILD_PHASE=True python manage.py collectstatic --no-input

RUN (crontab -l 2>/dev/null; \
     echo "*/3 * * * * cd /strongfitness && /usr/local/bin/python manage.py send_message >> /var/log/cron.log 2>&1"; \
     echo "*/3 * * * * cd /strongfitness && /usr/local/bin/python manage.py update_user_status >> /var/log/cron.log 2>&1") | crontab

EXPOSE 8080

# para ambiente de desenvolvimento
#CMD ["sh", "-c", "cron && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

