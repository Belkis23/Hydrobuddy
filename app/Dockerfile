FROM python:3.6
EXPOSE 5000
WORKDIR /app
COPY requirements.txt /app
CMD source venv/vin/activate
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD python3 run.py
