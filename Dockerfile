FROM python:3.7-slim

RUN pip3 install --upgrade pip && \
    pip3 install sklearn jupyter matplotlib tensorflow keras keras-rl lightgbm graphviz opencv-python

EXPOSE 8888

RUN useradd jupyter && mkdir /home/jupyter && chown jupyter:jupyter /home/jupyter
USER jupyter
CMD ["jupyter", "notebook", "--ip=0.0.0.0"]
