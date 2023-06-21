FROM python:3.8

# upgrade pip
RUN pip install --upgrade pip


RUN mkdir /project
COPY requirements.txt /project/requirements.txt

RUN pip install -r /project/requirements.txt

COPY scripts_airflow/ /project/scripts/
COPY dbt/profiles.yml /root/.dbt/profiles.yml
RUN chmod +x /project/scripts/init.sh
ENTRYPOINT [ "/project/scripts/init.sh" ]