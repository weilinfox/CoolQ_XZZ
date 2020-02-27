import requests
import json
from config import APIURL, ALLWORKERS, AUTHORIZATION
from worker import emmm

class StdAns():
    AllowGroup = []
    AllowUser = []
    AllowRole = []
    GroupNotAllow = '汝所在的群组不被允许这样命令咱呢.'
    UserNotAllow = '汝不被允许呢.'
    RoleNotAllow = '汝的角色不被允许哦.'

    def __init__(self,parms,uid,gid,role,raw_msg):
        self.parms = parms
        self.uid = uid
        self.gid = gid
        self.role = role
        self.raw_msg = raw_msg


    def CheckPermission(self):
            if self.AllowGroup and self.gid not in self.AllowGroup:
                return self.GroupNotAllow
            if self.AllowUser and self.uid not in self.AllowUser:
                return self.UserNotAllow
            if self.AllowRole and self.role not in self.AllowRole:
                return self.RoleNotAllow
            return 0

    def GETMSG(self):
        return self.__module__ +'的话，咱已经知道了，但是还在学习呢！'

    def sendmsg(self,msg):
        url = APIURL + "send_msg"
        Headers = {
            'content-type': 'application/json',
            'Authorization':'Bearer ' + AUTHORIZATION
            }
        
        data = {
            'message_type' : 'group',
            'group_id' : self.gid,
            'message': msg
            }
        requests.post(url = url, data = json.dumps(data),headers = Headers)
