gajson =  'client1.json'
import os
os.system('sudo pip3 install --upgrade google-assistant-grpc')
os.system('sudo pip install --upgrade google-auth-oauthlib[tool]')
os.system('google-oauthlib-tool --client-secrets '+gajson+' --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless')
