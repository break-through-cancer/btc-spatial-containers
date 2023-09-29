FROM python:3.11

RUN git clone https://github.com/FertigLab/pycogaps.git

RUN cd pycogaps/ && git submodule update --init --recursive

RUN cd pycogaps/ && pip install -r requirements.txt && pip install --upgrade pybind11 && pip install .

COPY cli.py /bin/cli.py

RUN chmod +x /bin/cli.py

ENTRYPOINT ["/bin/cli.py"]