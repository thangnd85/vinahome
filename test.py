
import os
import logging
import json

import click
import google.auth.transport.grpc
import google.auth.transport.requests
import google.oauth2.credentials

from google.assistant.embedded.v1alpha2 import (
    embedded_assistant_pb2,
    embedded_assistant_pb2_grpc
)
def gettext(data):
    import dem
    text = data
    return text
	
try:
    from . import (
        assistant_helpers,
        browser_helpers,
    )
except (SystemError, ImportError):
    import assistant_helpers
    import browser_helpers

def text():
	a = '1'
	b = '2'
	return a
def printx():
	t = textinput.main()
	print (t)
