#### 6. Create Documents

- [`insertOne` without `id`](#insertone-without-id)
- [`insertOne` with `id`](#insertone-with-id)
- [`insertMany`](#insertmany)

```
> show dbs
admin  0.000GB
>
```

###### `insertOne` without `id`

```
> db.moviesScratch.insertOne({ "title": "Rocky", "year": "1976", "imdb": "tt0075148"});
{
	"acknowledged" : true,
	"insertedId" : ObjectId("5abe672b7614dcf35aca9046")
}
>
```

```
> db.moviesScratch.find().pretty()
{
	"_id" : ObjectId("5abe672b7614dcf35aca9046"),
	"title" : "Rocky",
	"year" : "1976",
	"imdb" : "tt0075148"
}
>
```

###### `insertOne` with `id`

```
> db.moviesScratch.insertOne({ "_id": "tt0075148", "title": "Rocky", "year": "1976" });
{ "acknowledged" : true, "insertedId" : "tt0075148" }
>
```

```
> db.moviesScratch.find().pretty()
{
	"_id" : ObjectId("5abe672b7614dcf35aca9046"),
	"title" : "Rocky",
	"year" : "1976",
	"imdb" : "tt0075148"
}
{ "_id" : "tt0075148", "title" : "Rocky", "year" : "1976" }
>
```

###### `insertMany`

```
> db.moviesScratch.insertMany(
...     [
...         {
...       "_id" : "tt0084726",
...       "title" : "Star Trek II: The Wrath of Khan",
...       "year" : 1982,
...       "type" : "movie"
...           },
...           {
...       "_id" : "tt0796366",
...       "title" : "Star Trek",
...       "year" : 2009,
...       "type" : "movie"
...           },
...           {
...       "_id" : "tt0084776",
...       "title" : "Star Trek II: The Wrath of Khan",
...       "year" : 1982,
...       "type" : "movie"
...           },
...           {
...       "_id" : "tt1408101",
...       "title" : "Star Trek Into Darkness",
...       "year" : 2013,
...       "type" : "movie"
...           },
...           {
...       "_id" : "tt0117731",
...       "title" : "Star Trek: First Contact",
...       "year" : 1996,
...       "type" : "movie"
...         }
...     ]
... );
{
	"acknowledged" : true,
	"insertedIds" : [
		"tt0084726",
		"tt0796366",
		"tt0084776",
		"tt1408101",
		"tt0117731"
	]
}
>
```

```
> db.moviesScratch.drop()
true
>
```

```
> db.moviesScratch.insertMany(
...     [
...         {
...       "_id" : "tt0084726",
...       "title" : "Star Trek II: The Wrath of Khan",
...       "year" : 1982,
...       "type" : "movie"
...           },
...           {
...       "_id" : "tt0796366",
...       "title" : "Star Trek",
...       "year" : 2009,
...       "type" : "movie"
...           },
...           {
...       "_id" : "tt0084726",
...       "title" : "Star Trek II: The Wrath of Khan",
...       "year" : 1982,
...       "type" : "movie"
...           },
...           {
...       "_id" : "tt1408101",
...       "title" : "Star Trek Into Darkness",
...       "year" : 2013,
...       "type" : "movie"
...           },
...           {
...       "_id" : "tt0117731",
...       "title" : "Star Trek: First Contact",
...       "year" : 1996,
...       "type" : "movie"
...         }
...     ]
... );
2018-03-30T10:01:27.927-0700 E QUERY    [thread1] BulkWriteError: write error at item 2 in bulk operation :
BulkWriteError({
	"writeErrors" : [
		{
			"index" : 2,
			"code" : 11000,
			"errmsg" : "E11000 duplicate key error collection: test.moviesScratch index: _id_ dup key: { : \"tt0084726\" }",
			"op" : {
				"_id" : "tt0084726",
				"title" : "Star Trek II: The Wrath of Khan",
				"year" : 1982,
				"type" : "movie"
			}
		}
	],
	"writeConcernErrors" : [ ],
	"nInserted" : 2,
	"nUpserted" : 0,
	"nMatched" : 0,
	"nModified" : 0,
	"nRemoved" : 0,
	"upserted" : [ ]
})
BulkWriteError@src/mongo/shell/bulk_api.js:369:48
BulkWriteResult/this.toError@src/mongo/shell/bulk_api.js:333:24
Bulk/this.execute@src/mongo/shell/bulk_api.js:1177:1
DBCollection.prototype.insertMany@src/mongo/shell/crud_api.js:314:5
@(shell):1:1
>
```

```
> db.moviesScratch.drop()
true
>
```

```
> db.moviesScratch.insertMany(
...     [
...         {
...     "_id" : "tt0084726",
...     "title" : "Star Trek II: The Wrath of Khan",
...     "year" : 1982,
...     "type" : "movie"
...         },
...         {
...     "_id" : "tt0796366",
...     "title" : "Star Trek",
...     "year" : 2009,
...     "type" : "movie"
...         },
...         {
...     "_id" : "tt0084726",
...     "title" : "Star Trek II: The Wrath of Khan",
...     "year" : 1982,
...     "type" : "movie"
...         },
...         {
...     "_id" : "tt1408101",
...     "title" : "Star Trek Into Darkness",
...     "year" : 2013,
...     "type" : "movie"
...         },
...         {
...     "_id" : "tt0117731",
...     "title" : "Star Trek: First Contact",
...     "year" : 1996,
...     "type" : "movie"
...         }
...     ],
...     {
...         "ordered": false
...     }
... );
2018-03-30T10:03:16.932-0700 E QUERY    [thread1] BulkWriteError: write error at item 2 in bulk operation :
BulkWriteError({
	"writeErrors" : [
		{
			"index" : 2,
			"code" : 11000,
			"errmsg" : "E11000 duplicate key error collection: test.moviesScratch index: _id_ dup key: { : \"tt0084726\" }",
			"op" : {
				"_id" : "tt0084726",
				"title" : "Star Trek II: The Wrath of Khan",
				"year" : 1982,
				"type" : "movie"
			}
		}
	],
	"writeConcernErrors" : [ ],
	"nInserted" : 4,
	"nUpserted" : 0,
	"nMatched" : 0,
	"nModified" : 0,
	"nRemoved" : 0,
	"upserted" : [ ]
})
BulkWriteError@src/mongo/shell/bulk_api.js:369:48
BulkWriteResult/this.toError@src/mongo/shell/bulk_api.js:333:24
Bulk/this.execute@src/mongo/shell/bulk_api.js:1177:1
DBCollection.prototype.insertMany@src/mongo/shell/crud_api.js:314:5
@(shell):1:1
>
```
