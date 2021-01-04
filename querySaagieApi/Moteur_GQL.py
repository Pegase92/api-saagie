from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import base64
import os

def ExecuteGQL(GQLRequest):

    saagie_projects_api_url = "https://saagie-workspace.prod.saagie.io/api/v1/projects/platform/4/graphql"
    credentials = os.environ['SAAGIE_API_USER'] + ':' + os.environ['SAAGIE_API_PASSWORD']
    key = base64.b64encode(credentials.encode()).decode()
    _transport = RequestsHTTPTransport(
    url=saagie_projects_api_url,
    headers={"Authorization": "Basic " + key},
    use_json=True
    )
    
    client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
    )
    query = gql(GQLRequest)
    Results = client.execute(query)

    return Results
