import json 
import csv 
def get_database():
    from pymongo import MongoClient
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    print(client)
    return client['squadcast-dev']
if __name__ == "__main__":    
    dbname = get_database()
    collection_name = dbname["organizations"]
    old_active_orgs = collection_name.find({"deActivated":False,"deleted":False})
    slugs=["testpunit","squadcast-test","squadcastt", 'hydratest', 'wayne-enterprise', 'bsg', 'xyz', 'go-corona', 'ott', 'mx', 'test-double', 'td', 'screenshots', 'underworld', 'c', 'ashorg', 'bhai-ka-adda', 'test1234', 'test34543543', 'qwwerty', 'qazxsw', 'regrefg', 'mkoiju', 'dev-org', 'hkv', 'arrival', 'squadcastt-test']
    deactivate_list=[]
    active_orgs=[]
    not_updated_orgs=[]
    for i in old_active_orgs:
        if(i["slug"] not in slugs):
            query = {"slug":i["slug"]}
            new_value = {"$set":{"deActivated":True}}
            result=collection_name.update_one(query,new_value)
            if(result.modified_count<1):
                not_updated_orgs.append(i["slug"])
            else:
                deactivate_list.append(i["slug"])
        else:
            active_orgs.append(i["slug"])
    print(deactivate_list)
    print("\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(active_orgs)
    print("\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(not_updated_orgs)