FROM python:3.7
RUN pip3 install oss2
ADD ./backup.py ./
CMD ["python3", "./backup.py"]
