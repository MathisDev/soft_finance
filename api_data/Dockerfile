FROM python:3
WORKDIR /
ADD . /
RUN bash update.sh 
RUN pip3 install -r requirements.txt
CMD ["bash", "start_api.sh"]
