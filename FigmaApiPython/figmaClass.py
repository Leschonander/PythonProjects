import requests as re
import json
from dataclasses import dataclass
from typing import Dict

@dataclass(order = True)
class Figma:
    ''' 
    Base class for all Figma API requests. While some 
    API's use different URL's at minimum one is using the
    correct token!
    ''' 
    token: dict 

@dataclass(order = True)
class figmaAPIFile(Figma):
    '''
    Figma API having to deal with files. 
    '''
    baseFileUrl: str = "https://api.figma.com/v1/files/"

    def jsonFile(self, fileName: str):
        '''
        Returns the JSON file content
        '''
        response = re.get(self.baseFileUrl +  fileName, headers= self.token)
        data = json.loads(response.text)
        return data

    def getNodes(self, fileName: str, node: str):
        '''
        Returns the nodes as JSON of a file
        '''
        response = re.get(self.baseFileUrl + fileName + '/nodes?ids=' + node, headers= self.token)
        data = json.loads(response.text)
        return data
    
    def getVersionHistory(self, fileName: str):
        '''
        Get the version history of a file...
        '''
        response = re.get(self.baseFileUrl + fileName + '/versions', headers= self.token)
        data = json.loads(response.text)
        return data
    
    def getImageUrl(self, fileName: str):
        '''
        Get all image urls for a fill in a document.
        '''
        response = re.get(self.baseFileUrl + fileName + '/images', headers= self.token)
        data = json.loads(response.text)
        return data
@dataclass(order = True)
class figmaAPIImage(Figma):
    '''
    Figma API having to deal with images. Yes Figma files are images,
    however, their is a difference in the URL so...
    '''
    baseImageUrl: str = "https://api.figma.com/v1/images/"

    def getImages(self, fileName: str, fileId: str):
        response = re.get(self.baseImageUrl + fileName + "?ids=" + fileId)
        data = json.loads(response.text)
        return data

@dataclass(order = True)
class figmaAPIComments(Figma):
    '''
    Figma API having to deal solely with grabbing comments.
    '''
    baseCommentUrl: str = 'https://api.figma.com/v1/files/'
    
    def getComments(self, fileName: str):
        '''
        Grab the comments of a file.
        '''
        response = re.get(self.baseCommentUrl + fileName + '/comments', headers= self.token)
        data = json.loads(response.text)
        return data

    def postComment(self, fileName: str):
        '''
        Post a comment. Note the token gets modified to seen the content type json payload.
        '''
        self.token = self.token.update({"Content-Type": "application/json",})
        # (print(self.token)) This is fine
        message = str(input("Input comment: "))
        data = {"message": message}
        r = re.post(self.baseCommentUrl + fileName + '/comments', headers= self.token, data = data)
        print(r.status_code, r.reason)
        if (r.status_code == 400):
            print("Request did not send: ", r.reason)
        elif (r.status_code == 403):
            print("Forbidden: ", r.reason)
        elif (r.status_code == 200):
            print("Success: ", r.reason)

@dataclass(order = True)
class figmaAPITeam(Figma):
    '''
    Figma API having to deal with team information. 
    '''
    baseImageUrl: str = "https://api.figma.com/v1/teams/"

    def getImages(self, teamName: str):
        response = re.get(self.baseImageUrl + teamName + "/projects")
        data = json.loads(response.text)
        return data

@dataclass(order = True)
class figmaAPIProject(Figma):
    '''
    Figma API having to deal with project information. 
    '''
    baseImageUrl: str = "https://api.figma.com/v1/projects/"

    def getImages(self, projectID: str):
        response = re.get(self.baseImageUrl + projectID + "/files")
        data = json.loads(response.text)
        return data

