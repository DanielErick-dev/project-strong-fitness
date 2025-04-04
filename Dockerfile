FROM python:3.11-slim

WORKDIR /strongfitness

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

RUN apt-get update && apt-get install -y cron

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN (crontab -l 2>/dev/null; \
     echo "*/3 * * * * cd /strongfitness && /usr/local/bin/python manage.py send_message >> /var/log/cron.log 2>&1"; \
     echo "*/3 * * * * cd /strongfitness && /usr/local/bin/python manage.py update_user_status >> /var/log/cron.log 2>&1") | crontab
CMD ["sh", "-c", "cron && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]