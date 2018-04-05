FROM python:latest

ADD ./ /

RUN pip install -e .

CMD ["python", "example.py"]