show dbs
use testdb1

show collections

db.test.insert({"vul_id" : 10001, "task_id" : 201, "site_id" : 1, "url_infos" : [ { "url" : "https://10.7.201.22/admin/test?a=1&b=2", "url_status" : 0 }, { "url" : "https://www.nsfocus.com/hehe?a=3", "url_status" : 0 }, { "url" : "http://www.nsc.com/aaaa/", "status" : 2 }]})
db.test.insert({"vul_id" : 10002, "task_id" : 202, "site_id" : 1, "url_infos" : [ { "url" : "https://10.7.201.22/admin/test?a=1&b=2", "url_status" : 0 }, { "url" : "https://www.nsfocus.com/hehe?a=3", "url_status" : 0 }, { "url" : "http://www.nsfocus.com/aaaa/", "status" : 2 }]})


db.test.find({"vul_id":10001})
db.test.find({"url_infos":{"$elemMatch":{"url_status":1}}})


db.test.find({"url_id":10001,"task_id":201,"site_id":1})

db.test.update({"url_id":10001,"task_id":201},{"$set":{"url_infos.2.url_status":2}})

//ensureIndex


db.test.ensureIndex({"vul_id":1},{"name":"vul_id_index"})
db.system.indexes.find()
db.runCommand({"dropIndexes":"test","index":"vul_id_index"})


