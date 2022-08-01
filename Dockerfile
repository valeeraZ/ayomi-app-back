FROM python:3.9

# First, we need to install Pipenv
RUN pip install pipenv

# Then, we need to convert the Pipfile to requirements.txt
COPY Pipfile* /tmp/

RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt

# Last, we install the dependency and then we can start the Gunicorn.
RUN pip install -r /tmp/requirements.txt

COPY . /tmp/app

WORKDIR /tmp/app

RUN rm -rf migrations

ENV FLASK_APP flasky.py

EXPOSE 8000

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "flasky:app"]