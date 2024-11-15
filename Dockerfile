FROM python:3.11
LABEL authors="maziar"

COPY assets/ assets/
COPY frontend/ frontend/
COPY states/ states/
COPY utils/ utils/
COPY rxconfig.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 3000
CMD ["reflex", "run"]
