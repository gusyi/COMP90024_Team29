import couchdb
import json
import sys

class dbAction:
    def __init__(self):
        self.user = 'admin'
        self.pw = 'admin'
        self.localhost = '127.0.0.1'

        self.dbserver = couchdb.Server("http://{}:{}@{}:5984/".format(self.user, self.pw, self.localhost))

        self.db = self.dbserver['testdb']
    
    def create_or_get_db(self, db, dbs):
        try:
            return dbs.create(db)
        except couchdb.http.PreconditionFailed:
            print ('DB {} already exists'.format(db))
            return dbs[db]
    
    def check_db(self, db, dbs):
        if db in dbs:
            print ('DB exists')
            return True
    
    def insert_raw(self, data, db):
        # processed = json.loads(data)
        # docid = jdata['id_str']
        print(type(data))
        docid = data['id_str']
        print (docid)
        try:
            db[docid] = data
        except couchdb.http.ResourceConflict:
            db.save(data)
        print ("ok")