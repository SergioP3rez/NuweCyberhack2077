FROM python:3.9-slim

RUN useradd -m netuser


WORKDIR ./home/netuser

COPY ./requirements.txt /opt/

RUN cd /opt/ && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY switch.py terminal.py vars.py /opt/
COPY flag.txt inmunosupresor.jpg intercepted.wav /home/netuser/

USER netuser

EXPOSE 1337

CMD ["python3","/opt/terminal.py"]
