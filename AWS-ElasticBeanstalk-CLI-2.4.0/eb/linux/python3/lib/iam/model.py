#!/usr/bin/env python
#==============================================================================
# Copyright 2012 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License"). You may not use
# this file except in compliance with the License. A copy of the License is
# located at
#
#       http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file. This file is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or
# implied. See the License for the specific language governing permissions
# and limitations under the License.
#==============================================================================
import urllib.request, urllib.parse, urllib.error
from datetime import datetime


class BaseModel(object):
    
    def __str__(self):
        return self.__repr__()
   
    def __repr__(self):
        ret = "\n"
        for attr, value in self.__dict__.items():
            ret += "(" + str(attr) + ":" + str(value) + ")\n"
        return ret    


class Role(BaseModel):

    def __init__(self):
        self._name = None
        self._id = None
        self._assume_role_policy_document= None
        self._path = None
        self._arn = None
        self._create_date = None

    @classmethod
    def from_json(cls, json_data):
        """ Create instance of InstanceProfile from structured json data"""
        ro = cls()
        ro._name = json_data['RoleName']     
        ro._id = json_data['RoleId']     
        ro._assume_role_policy_document = urllib.parse.unquote(json_data['AssumeRolePolicyDocument'])     
        ro._path = json_data['Path']     
        ro._arn = json_data['Arn']     
        ro._create_date_raw = json_data['CreateDate']     
        ro._create_date = datetime.fromtimestamp(ro._create_date_raw).replace(microsecond=0)             
        return ro
        
    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id
    
    @property
    def assume_role_policy_document(self):
        return self._assume_role_policy_document
    
    @property
    def path(self):
        return self._path
    
    @property
    def arn(self):
        return self._arn
    
    @property
    def create_date(self):
        return self._create_date


class InstanceProfile(BaseModel):

    def __init__(self):
        self._name = None
        self._id = None
        self._roles = None
        self._path = None
        self._arn = None
        self._create_date = None

    @classmethod
    def from_json(cls, json_data):
        """ Create instance of InstanceProfile from structured json data"""
        ip = cls()
        ip._name = json_data['InstanceProfileName']     
        ip._id = json_data['InstanceProfileId']     
        ip._roles = []
        for role in json_data['Roles']:
            ip._roles.append(Role.from_json(role))
        ip._path = json_data['Path']     
        ip._arn = json_data['Arn']     
        ip._create_date_raw = json_data['CreateDate']     
        ip._create_date = datetime.fromtimestamp(ip._create_date_raw).replace(microsecond=0)             
        return ip
        
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id

    @property
    def roles(self):
        return self._roles
    
    @property
    def path(self):
        return self._path
    
    @property
    def arn(self):
        return self._arn
    
    @property
    def create_date(self):
        return self._create_date
    
        