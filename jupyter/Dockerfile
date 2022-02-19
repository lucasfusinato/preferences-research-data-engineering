FROM jupyter/minimal-notebook
WORKDIR /home/jovyan
COPY config/jupyter_notebook_config.py .jupyter/jupyter_notebook_config.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY notebooks notebooks