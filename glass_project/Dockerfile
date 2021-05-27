FROM python:3
 
WORKDIR /glass_project
 
COPY requirements.txt .
RUN pip install -r requirements.txt
 
COPY . .
 
EXPOSE 5000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:5000"]
# CMD ["python3", "manage.py", "runserver", "183.88.226.202:5000"]