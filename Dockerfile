
# Section 1- Base Image
FROM python:3.11-slim

# Section 2- Python Interpreter Flags
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Section 3- Compiler
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*



WORKDIR /app/
COPY . /app/

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# migrations
RUN python manage.py makemigrations
RUN python manage.py migrate


# Section 8- Running the App
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

