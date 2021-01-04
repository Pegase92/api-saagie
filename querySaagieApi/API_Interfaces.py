import Moteur_GQL
from querySaagieApi.gql_template import *


def GetProjectsbyName(strToFind):

    """ Return all the projects in the Saagie platform which name contains <strToFind> """

    GQLRequest = gql_get_projects_info
    Results = Moteur_GQL.ExecuteGQL(GQLRequest)
    ProjectByName=[]
    for elt in Results['projects']:
        if elt['name'].find(strToFind)>=0:
            ProjectByName.append(elt)

    return(ProjectByName)

def GetProjectsbyCreateur(strToFind):

    """ Return all the projects in the Saagie platform which creator field contains <strToFind> """

    GQLRequest = gql_get_projects_info
    Results = Moteur_GQL.ExecuteGQL(GQLRequest)
    ProjectByName=[]
    for elt in Results['projects']:
        if elt['creator'].find(strToFind)>=0:
            ProjectByName.append(elt)
            
    return(ProjectByName)

def GetProjectsbyDescription(strToFind):

    """ Return all the projects in the Saagie platform which description field contains <strToFind> """

    GQLRequest = gql_get_projects_info
    Results = Moteur_GQL.ExecuteGQL(GQLRequest)
    ProjectByName=[]
    for elt in Results['projects']:
        if elt['description'].find(strToFind)>=0:
            ProjectByName.append(elt)
            
    return(ProjectByName)
