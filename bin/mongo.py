# coding = utf-8
import sys,os,json
from pymongo import MongoClient
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import  innodb_con as lib_conf
from lib import  innodb_status as lib_status


def conf_conf(host,user,password,db,port):
    a_b=lib_conf.conf(host,user,password,db,port)
    json_json=json.dumps(a_b)
    return json_json


def status_status(host,user,password,db,port):
    b_c=lib_status.mysql_page(host,user,password,db,port)
    json_json=json.dumps(b_c)
    return json_json


def conf_mo(ip_port,host,user,password,db,port):
    a_json = json.load(open('./conf/conf', 'r'))
    conn=MongoClient(a_json['host'],int(a_json['port']))
    db_auth=conn.abc
    db_auth.authenticate(a_json['user'],a_json['passwd'])
    aa=conf_conf(host,user,password,db,port)
    #print(aa)
    db_auth.conf.insert({'ip':ip_port,'local':aa})


def conf_status(ip_port,host,user,password,db,port):
    a_json = json.load(open('./conf/conf', 'r'))
    conn = MongoClient(a_json['host'], int(a_json['port']))
    db_auth=conn.abc
    db_auth.authenticate(a_json['user'], a_json['passwd'])
    aa=status_status(host,user,password,db,port)
    #print(aa)
    db_auth.status.insert({'ip':ip_port,'local':aa})


def main (ip,host,user,password,db,port):
    conf_mo(ip,host,user,password,db,port)
    conf_status(ip,host,user,password,db,port)
