FROM python:3.11.5-bookworm
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "app.py" ]