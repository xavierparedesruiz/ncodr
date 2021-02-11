# Pull base image
FROM python:3.9

# Set environment varibles

# Install dependencies
COPY ./requirements /tmp/requirements
RUN pip install --disable-pip-version-check --no-cache-dir -r /tmp/requirements/base.txt

COPY ./app /app

WORKDIR /app/

EXPOSE 8000
CMD ["python", "main.py"]
