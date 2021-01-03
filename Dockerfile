ARG ARCH=
FROM ${ARCH}debian:buster-slim
RUN apt-get update
RUN apt-get install -y sox
RUN apt-get install -y libsdl-mixer1.2
RUN apt-get install -y swig
RUN apt-get install -y libatlas-base-dev
RUN apt-get install -y python3-pyaudio
RUN apt-get install -y vlc
RUN apt-get install -y python3-setuptools
RUN apt-get install -y build-essential
RUN apt-get install -y libsdl1.2-dev
RUN apt-get install -y libfreetype6-dev
RUN apt-get install -y libsdl-dev
RUN apt-get install -y libsdl-image1.2-dev
RUN apt-get install -y libsdl-ttf2.0-dev
RUN apt-get install -y libsmpeg-dev
RUN apt-get install -y libportmidi-dev
RUN apt-get install -y libavformat-dev
RUN apt-get install -y libswscale-dev
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-numpy
RUN apt-get install -y python3-cffi
RUN apt-get install -y python3-scipy
RUN apt-get install -y python-matplotlib
RUN apt-get install -y ipython
RUN apt-get install -y python-pandas
RUN apt-get install -y python-sympy
RUN apt-get install -y python-nose
RUN apt-get install -y libffi-dev
RUN apt-get install -y libcurl4-openssl-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y libsoup2.4-dev
RUN apt-get install -y git
RUN apt-get install -y libgcrypt20-dev
RUN apt-get install -y libgstreamer-plugins-bad1.0-dev
RUN apt-get install -y gstreamer1.0-plugins-good
RUN apt-get install -y libasound2-dev
RUN apt-get install -y flac
RUN apt-get install -y curl
RUN apt-get install -y apt-transport-https
RUN apt-get install -y libportaudio2
RUN apt-get install -y libportaudiocpp0
RUN apt-get install -y portaudio19-dev
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-venv
RUN apt-get install -y ffmpeg
RUN apt-get install -y autossh
RUN apt-get install -y supervisor
RUN apt-get install -y libxml2-dev
RUN apt-get install -y libxslt-dev
RUN apt-get install -y python-dev
RUN apt-get install -y python3-lxml
RUN apt-get install -y python3-pygame
RUN apt-get install -y python3-sklearn 
RUN apt-get install -y python3-sklearn-lib 
RUN mkdir /usr/share/vinahome
COPY . /usr/share/vinahome
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir PySDL2
RUN pip3 install --no-cache-dir requests
RUN pip3 install --no-cache-dir regex
RUN pip3 install --no-cache-dir pya20
RUN pip3 install --no-cache-dir termcolor
RUN pip3 install --no-cache-dir pyAesCrypt
RUN pip3 install --no-cache-dir cffi
RUN pip3 install --no-cache-dir google-cloud-speech
RUN pip3 install --no-cache-dir six
RUN pip3 install --no-cache-dir googletrans
RUN pip3 install --no-cache-dir wikipedia
RUN pip3 install --no-cache-dir forecastiopy
RUN pip3 install --no-cache-dir click
RUN pip3 install --no-cache-dir pyyaml
RUN pip3 install --no-cache-dir datetime
RUN pip3 install --no-cache-dir bs4
RUN pip3 install --no-cache-dir datefinder
RUN pip3 install --no-cache-dir pafy
RUN pip3 install --no-cache-dir youtube_dl
RUN pip3 install --no-cache-dir pyalsaaudio
RUN pip3 install --no-cache-dir gTTS
RUN pip3 install --no-cache-dir python-vlc
RUN pip3 install --no-cache-dir SpeechRecognition
RUN pip3 install --no-cache-dir feedparser
RUN pip3 install --no-cache-dir mutagen
RUN pip3 install --no-cache-dir pyaudio
RUN pip3 install --no-cache-dir pulsectl
RUN pip3 install --no-cache-dir google-assistant-library
RUN pip3 install --no-cache-dir google-assistant-sdk[samples]
RUN pip3 install --no-cache-dir google-auth-oauthlib[tool]
RUN pip3 install --no-cache-dir google-assistant-grpc
RUN pip3 install --no-cache-dir spidev
RUN pip3 install --no-cache-dir git+https://github.com/plamere/spotipy.git --upgrade
RUN pip3 install --no-cache-dir fuzzywuzzy
RUN pip3 install --no-cache-dir python-Levenshtein
RUN pip3 install --no-cache-dir playsound
RUN pip3 install --no-cache-dir wget
RUN pip3 install --no-cache-dir pydub
RUN pip3 install --no-cache-dir pulsemixer
RUN pip3 install --no-cache-dir cython
RUN pip3 install --no-cache-dir underthesea
RUN rm -rf /root/.cache
WORKDIR /usr/share/vinahome
RUN rm ./swig/Python3/_snowboydetect.so
RUN rm ./swig/Python3/snowboy-detect-swig.cc
RUN rm ./swig/Python3/snowboy-detect-swig.o 
RUN rm ./swig/Python3/snowboydetect.py
RUN cd ./swig/Python3 && make
RUN cd ../..
RUN cp ./swig/Python3/_snowboydetect.so ./
RUN cp ./swig/Python3/snowboydetect.py ./
CMD [ "python", "dem.py" ]
