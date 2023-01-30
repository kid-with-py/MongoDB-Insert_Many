

import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017/')

mydatabase=client['Employee']

info=mydatabase.employeeinfo

records=[{
    'firstname':'Jhon',
    'lastname':'Wick',
    'job':'Analyst'
},{
    'firstname':'Mithun',
    'lastname':'Gopinathan',
    'job':'Analyst'
},{
    'firstname':'Binil',
    'lastname':'Mukundan',
    'job':'Analyst'
},{
    'firstname':'Neeraj',
    'lastname':'Surendran',
    'job':'Analyst'
}]

data=info.insert_many(records)

print(data.inserted_ids)
