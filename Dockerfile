FROM python:3.9.13-alpine3.16
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV MODE=${MODE}
ENV TOKEN=${TOKEN}
ENV apipswd=${apipswd}
ENV apiusername=${apiusername}
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", "/app/bot.py"]