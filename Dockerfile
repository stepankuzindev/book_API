#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
#
#WORKDIR /app/
#
## Install Poetry
#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
#    cd /usr/local/bin && \
#    ln -s /opt/poetry/bin/poetry && \
#    poetry config virtualenvs.create false
#
#COPY ./pyproject.toml ./poetry.lock /app/
#
## Allow installing dev dependencies to run tests
#ARG INSTALL_DEV=false
#RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"
#
## For development, Jupyter remote kernel, Hydrogen
## Using inside the container:
## jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888
#ARG INSTALL_JUPYTER=false
#RUN bash -c "if [ $INSTALL_JUPYTER == 'true' ] ; then pip install jupyterlab ; fi"
#
#COPY ./ /app
#ENV PYTHONPATH=/app
#
#ENV APP_MODULE=cards.main:app
#

#




FROM python:3.9

WORKDIR /app/

#ENV FLASK_APP=app.py
#ENV FLASK_RUN_HOST=0.0.0.0

#RUN apt install --no-cache gcc musl-dev linux-headers

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"


#EXPOSE 5000
COPY ./ /app
#CMD ["flask", "run"]
