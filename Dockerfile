FROM python:2.7

RUN pip install selenium

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - &&\
    sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' &&\
    apt-get update && \
    apt-get install -y google-chrome-stable

RUN wget https://chromedriver.storage.googleapis.com/2.36/chromedriver_linux64.zip &&\
    apt-get install -y unzip &&\
    unzip chromedriver_linux64.zip -d /usr/bin/

RUN apt-get install -y xvfb &&\
    pip install pyvirtualdisplay
    