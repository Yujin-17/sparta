from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.mhvqxjc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

movie = db.movies.find_one({'title':'가버나움'})
print(movie['star'])
star = movie['star']

all_movies = list(db.movies.find({'star' : star},{'_id':False}))

for m in all_movies:
    print(m['title'])

db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})