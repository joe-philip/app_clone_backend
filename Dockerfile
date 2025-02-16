# Use official Python image as base
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy project files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run Django server
CMD ["python manage.py runserver", "0.0.0.0:8000"]