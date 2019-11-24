import textinput
from textinput import *
api_endpoint = 'embeddedassistant.googleapis.com'
grpc_deadline = 60 * 3 + 5
PLAYING = embedded_assistant_pb2.ScreenOutConfig.PLAYING
device_id = 'gapi-7c1b2'
device_model_id = 'gapi-pias'
lang = 'en-US'
display = True
verbose = True
credentials = os.path.join(click.get_app_dir('google-oauthlib-tool'),
                           'credentials.json')
with open(credentials, 'r') as f:
    credentials = google.oauth2.credentials.Credentials(token=None,
                                                        **json.load(f))
    http_request = google.auth.transport.requests.Request()
    credentials.refresh(http_request)
grpc_channel = google.auth.transport.grpc.secure_authorized_channel(
    credentials, http_request, api_endpoint)
with SampleTextAssistant(lang, device_model_id, device_id, display,
                         grpc_channel, grpc_deadline) as assistant:
#        while True:
            
#            query = click.prompt('')
#            click.echo('<you> %s' % query)
    query = input()
    response_text, response_html = assistant.assist(text_query=query)
    print (response_text)
