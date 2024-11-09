FROM python
WORKDIR /app
COPY . /app
RUN apt update
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]