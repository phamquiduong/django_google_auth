# Google app auth
GOOGLE_CLIENT_ID = ''
GOOGLE_CLIENT_SECRET = ''

CLIENT_CONFIG = {
    "web": {
        "client_id": GOOGLE_CLIENT_ID,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": GOOGLE_CLIENT_SECRET
    }
}

SCOPES = [
    'https://www.googleapis.com/auth/drive.metadata.readonly'
]

# Server info
BASE_URL = 'http://localhost'
AUTH_APP = 'google'
CALL_BACK_URI = 'oauth2callback'

CALL_BACK_URL = f'{BASE_URL}/{AUTH_APP}/{CALL_BACK_URI}'
