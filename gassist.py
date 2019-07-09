import argparse
import os.path
import json
import google.oauth2.credentials
import RPi.GPIO as GPIO
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file
import google.auth
import google.auth.transport.grpc
import google.auth.transport.requests

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--credentials', type=existing_file,
                    metavar='OAUTH2_CREDENTIALS_FILE',
                    default=os.path.join(
                        os.path.expanduser('/home/pi/.config'),
                        'google-oauthlib-tool',
                        'credentials.json'
                    ),
                    help='Path to store and read OAuth2 credentials')
args = parser.parse_args()
with open(args.credentials, 'r') as f:
    credentials = google.oauth2.credentials.Credentials(token=None,
                                                        **json.load(f))