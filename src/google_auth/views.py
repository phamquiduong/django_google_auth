from google_auth_oauthlib.flow import Flow
from core import *
from django.shortcuts import redirect
from django.http import HttpResponse


def authorization_url(request):
    if not request.user.is_authenticated:
        return redirect('/admin')

    flow = Flow.from_client_config(
        client_config=CLIENT_CONFIG,
        scopes=SCOPES
    )

    flow.redirect_uri = CALL_BACK_URL

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )

    return redirect(authorization_url)


def credentials(request):
    if not request.user.is_authenticated:
        return redirect('/admin')

    state = request.GET.get('state', '')

    flow = Flow.from_client_config(
        client_config=CLIENT_CONFIG,
        scopes=SCOPES,
        state=state
    )
    flow.redirect_uri = CALL_BACK_URL

    authorization_response = request.build_absolute_uri()
    # You must use https instead http. If test on localhost uncomment bellow line
    # authorization_response = authorization_response.replace('http', 'https')

    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials

    request.user.refresh_token = credentials.refresh_token
    request.user.save()

    return HttpResponse('Success')
