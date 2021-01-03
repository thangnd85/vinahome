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
RUN pip install --no-cache-dirwheel
RUN pip install --no-cache-dirPySDL2
RUN pip install --no-cache-dirrequests
RUN pip install --no-cache-dirregex
RUN pip install --no-cache-dirpya20
RUN pip install --no-cache-dirtermcolor
RUN pip install --no-cache-dirpyAesCrypt
RUN pip install --no-cache-dircffi
RUN pip install --no-cache-dirgoogle-cloud-speech
RUN pip install --no-cache-dirsix
RUN pip install --no-cache-dirgoogletrans
RUN pip install --no-cache-dirwikipedia
RUN pip install --no-cache-dirforecastiopy
RUN pip install --no-cache-dirclick
RUN pip install --no-cache-dirpyyaml
RUN pip install --no-cache-dirdatetime
RUN pip install --no-cache-dirbs4
RUN pip install --no-cache-dirdatefinder
RUN pip install --no-cache-dirpafy
RUN pip install --no-cache-diryoutube_dl
RUN pip install --no-cache-dirpyalsaaudio
RUN pip install --no-cache-dirgTTS
RUN pip install --no-cache-dirpython-vlc
RUN pip install --no-cache-dirSpeechRecognition
RUN pip install --no-cache-dirfeedparser
RUN pip install --no-cache-dirmutagen
RUN pip install --no-cache-dirpyaudio
RUN pip install --no-cache-dirpulsectl
RUN pip install --no-cache-dirgoogle-assistant-library
RUN pip install --no-cache-dirgoogle-assistant-sdk[samples]
RUN pip install --no-cache-dirgoogle-auth-oauthlib[tool]
RUN pip install --no-cache-dirgoogle-assistant-grpc
RUN pip install --no-cache-dirspidev
RUN pip install --no-cache-dirgit+https://github.com/plamere/spotipy.git --upgrade
RUN pip install --no-cache-dirfuzzywuzzy
RUN pip install --no-cache-dirpython-Levenshtein
RUN pip install --no-cache-dirplaysound
RUN pip install --no-cache-dirwget
RUN pip install --no-cache-dirpydub
RUN pip install --no-cache-dirpulsemixer
RUN pip install --no-cache-dircython
RUN pip install --no-cache-dirunderthesea
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
