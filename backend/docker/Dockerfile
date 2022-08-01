# Pull ofiicial Python Docker image
FROM python:3.10.5-slim-buster

# Set the working directory
WORKDIR /usr/src/app

# Set up Python behaviour
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv

# Switch on virtual environment
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set the server port
EXPOSE 8000

# Install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements/requirements.txt ./requirements/requirements-dev.txt ./
RUN pip install -r requirements/requirements.txt \
  && pip install -r requirements/requirements-dev.txt

# Copy all files
COPY . .

# Add the file entrypoint.sh
COPY ./docker/entrypoint.sh .
RUN chmod +x /usr/src/app/docker/entrypoint.sh

# Execute entrypoint.sh
ENTRYPOINT ["/usr/src/app/docker/entrypoint.sh"]

# Start up the backend server
CMD alembic upgrade head \
  && uvicorn app.main:app --reload --workers 2 --host 0.0.0.0 --port 8000