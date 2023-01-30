
### pymongo is the library which helps to interact with MongoDB using Python ###
 
import pymongo

### Creating URI for MongoDB ###

client=pymongo.MongoClient('mongodb://localhost:27017/')

### Setting DB's Name ###

mydatabase=client['Employee']

### Setting collection's(employeeinfo) Name ###

info=mydatabase.employeeinfo

### Creating Collection ###

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

### Inserting The Data into the database-collection ###

data=info.insert_many(records)

print(data.inserted_ids)
