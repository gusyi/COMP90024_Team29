import couchdb
import json
import sys

class dbAction:
    def __init__(self):
        self.user = 'admin'
        self.pw = 'admin'
        self.localhost = '127.0.0.1'

        # self.dbserver = couchdb.Server("http://{}:{}@{}:5984/".format(self.user, self.pw, self.localhost))
  
        self.INSERTSUCCESS = "Success"
        self.DUPFOUND = "Doc exists"
    
    def get_server(self, user, pw, ip):
        return couchdb.Server("http://{}:{}@{}:5984/".format(user, pw, ip))
    
    def create_or_get_db(self, db, dbs):
        try:
            return dbs.create(db)
        except couchdb.http.PreconditionFailed:
            print ('DB {} exists'.format(db))
            return dbs[db]
    
    def check_db(self, db, dbs):
        if db in dbs:
            print ('DB exists')
            return True
    
    def get_doc(self, id, db):
        try:
            doc = db.get(id)
            return doc
        except:
            print ("doc does not exist")
            return
    
    def get_all_docs(self, db):
        all_docs = []
        docs = db.view('_all_docs')
        for d in docs:
            all_docs.append(self.get_doc(d.id, db))

        return all_docs

    def insert_raw(self, data, db):
        docid = data['_id']
        try:
            db[docid] = data
            print ('Doc added to DB...', docid)
            return self.INSERTSUCCESS
        except couchdb.http.ResourceConflict:
            # db.save(data)
            print ('Doc skipped')
            return self.DUPFOUND