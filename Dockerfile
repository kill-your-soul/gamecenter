FROM python:3.10.11

WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
ENV SECRET_KEY=123
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
# ENTRYPOINT ["python3"] 
CMD ["python3", "manage.py", "runserver"]