FROM python:alpine

ADD ./ /

RUN pip install -e .

CMD ["python", "example.py"]