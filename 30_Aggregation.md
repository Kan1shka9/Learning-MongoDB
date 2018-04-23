#### 30. [Aggregation](https://docs.mongodb.com/manual/aggregation/)

###### Framework

![](images/30/1.png)

![](images/30/2.png)

```sh
u64@vm:~/Desktop$ sudo service mongod start
```

`products__m101p_52b20120e2d42362670d8231.js`

```js
use agg
db.products.drop()

db.products.insert({'name':'iPad 16GB Wifi', 'manufacturer':"Apple",
		    'category':'Tablets',
		    'price':499.00})
db.products.insert({'name':'iPad 32GB Wifi', 'category':'Tablets',
		    'manufacturer':"Apple",
		    'price':599.00})
db.products.insert({'name':'iPad 64GB Wifi', 'category':'Tablets',
		    'manufacturer':"Apple",
		    'price':699.00})
db.products.insert({'name':'Galaxy S3', 'category':'Cell Phones',
		    'manufacturer':'Samsung',
		    'price':563.99})
db.products.insert({'name':'Galaxy Tab 10', 'category':'Tablets',
		    'manufacturer':'Samsung',
		    'price':450.99})
db.products.insert({'name':'Vaio', 'category':'Laptops',
		    'manufacturer':"Sony",
		    'price':499.00})
db.products.insert({'name':'Macbook Air 13inch', 'category':'Laptops',
		    'manufacturer':"Apple",
		    'price':499.00})
db.products.insert({'name':'Nexus 7', 'category':'Tablets',
		    'manufacturer':"Google",
		    'price':199.00})
db.products.insert({'name':'Kindle Paper White', 'category':'Tablets',
		    'manufacturer':"Amazon",
		    'price':129.00})
db.products.insert({'name':'Kindle Fire', 'category':'Tablets',
		    'manufacturer':"Amazon",
		    'price':199.00})
```

```sh
u64@vm:~/Desktop$ mongo < products__m101p_52b20120e2d42362670d8231.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
false
WriteResult({ "nInserted" : 1 })
WriteResult({ "nInserted" : 1 })
WriteResult({ "nInserted" : 1 })
WriteResult({ "nInserted" : 1 })
WriteResult({ "nInserted" : 1 })
WriteResult({ "nInserted" : 1 })
WriteResult({ "nInserted" : 1 })
WriteResult({ "nInserted" : 1 })
WriteResult({ "nInserted" : 1 })
WriteResult({ "nInserted" : 1 })
bye
u64@vm:~/Desktop$
```

```sh
u64@vm:~/Desktop$ mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Server has startup warnings:
2018-04-22T11:05:02.839-0700 I STORAGE  [initandlisten]
2018-04-22T11:05:02.839-0700 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2018-04-22T11:05:02.839-0700 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2018-04-22T11:05:05.406-0700 I CONTROL  [initandlisten]
2018-04-22T11:05:05.406-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-04-22T11:05:05.406-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-04-22T11:05:05.406-0700 I CONTROL  [initandlisten]
> show dbs
admin     0.000GB
agg       0.000GB
blog      0.011GB
config    0.000GB
local     0.000GB
m101      0.000GB
school    2.153GB
students  0.001GB
test      0.046GB
video     0.001GB
> use agg
switched to db agg
> show collections
products
> db.products.findOne()
{
	"_id" : ObjectId("5adcced6bed72169a41edcb1"),
	"name" : "iPad 16GB Wifi",
	"manufacturer" : "Apple",
	"category" : "Tablets",
	"price" : 499
}
> db.products.find().pretty()
{
	"_id" : ObjectId("5adcced6bed72169a41edcb1"),
	"name" : "iPad 16GB Wifi",
	"manufacturer" : "Apple",
	"category" : "Tablets",
	"price" : 499
}
{
	"_id" : ObjectId("5adcced6bed72169a41edcb2"),
	"name" : "iPad 32GB Wifi",
	"category" : "Tablets",
	"manufacturer" : "Apple",
	"price" : 599
}
{
	"_id" : ObjectId("5adcced6bed72169a41edcb3"),
	"name" : "iPad 64GB Wifi",
	"category" : "Tablets",
	"manufacturer" : "Apple",
	"price" : 699
}
{
	"_id" : ObjectId("5adcced6bed72169a41edcb4"),
	"name" : "Galaxy S3",
	"category" : "Cell Phones",
	"manufacturer" : "Samsung",
	"price" : 563.99
}
{
	"_id" : ObjectId("5adcced6bed72169a41edcb5"),
	"name" : "Galaxy Tab 10",
	"category" : "Tablets",
	"manufacturer" : "Samsung",
	"price" : 450.99
}
{
	"_id" : ObjectId("5adcced6bed72169a41edcb6"),
	"name" : "Vaio",
	"category" : "Laptops",
	"manufacturer" : "Sony",
	"price" : 499
}
{
	"_id" : ObjectId("5adcced6bed72169a41edcb7"),
	"name" : "Macbook Air 13inch",
	"category" : "Laptops",
	"manufacturer" : "Apple",
	"price" : 499
}
{
	"_id" : ObjectId("5adcced6bed72169a41edcb8"),
	"name" : "Nexus 7",
	"category" : "Tablets",
	"manufacturer" : "Google",
	"price" : 199
}
{
	"_id" : ObjectId("5adcced6bed72169a41edcb9"),
	"name" : "Kindle Paper White",
	"category" : "Tablets",
	"manufacturer" : "Amazon",
	"price" : 129
}
{
	"_id" : ObjectId("5adcced6bed72169a41edcba"),
	"name" : "Kindle Fire",
	"category" : "Tablets",
	"manufacturer" : "Amazon",
	"price" : 199
}
>
```

`simple_example__m101p_52b1e9abe2d4235b7e5ebb63.js`

```js
use agg
db.products.aggregate([
    {$group:
     {
	 _id:"$manufacturer",
	 num_products:{$sum:1}
     }
    }
])
```

```sh
u64@vm:~/Desktop$ mongo < simple_example__m101p_52b1e9abe2d4235b7e5ebb63.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
{ "_id" : "Amazon", "num_products" : 2 }
{ "_id" : "Apple", "num_products" : 4 }
{ "_id" : "Google", "num_products" : 1 }
{ "_id" : "Samsung", "num_products" : 2 }
{ "_id" : "Sony", "num_products" : 1 }
bye
u64@vm:~/Desktop$
```

###### Pipeline

![](images/30/3.png)

![](images/30/4.png)

###### Compound Grouping

![](images/30/5.png)

`simple_example1__m101p_52b1ef62e2d4235b7e5ebb6c.js`

```js
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {'manufacturer':"$manufacturer"},
	 num_products:{$sum:1}
     }
    }
])
```

```sh
u64@vm:~/Desktop$ mongo < simple_example1__m101p_52b1ef62e2d4235b7e5ebb6c.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
{ "_id" : { "manufacturer" : "Amazon" }, "num_products" : 2 }
{ "_id" : { "manufacturer" : "Apple" }, "num_products" : 4 }
{ "_id" : { "manufacturer" : "Google" }, "num_products" : 1 }
{ "_id" : { "manufacturer" : "Samsung" }, "num_products" : 2 }
{ "_id" : { "manufacturer" : "Sony" }, "num_products" : 1 }
bye
u64@vm:~/Desktop$
```

`compound1__m101p_52b1edebe2d4235b7e5ebb69.js`

```js
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "manufacturer":"$manufacturer",
	     "category" : "$category"},
	 num_products:{$sum:1}
     }
    }
])
```

```sh
u64@vm:~/Desktop$ mongo < compound1__m101p_52b1edebe2d4235b7e5ebb69.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
{ "_id" : { "manufacturer" : "Amazon", "category" : "Tablets" }, "num_products" : 2 }
{ "_id" : { "manufacturer" : "Apple", "category" : "Laptops" }, "num_products" : 1 }
{ "_id" : { "manufacturer" : "Apple", "category" : "Tablets" }, "num_products" : 3 }
{ "_id" : { "manufacturer" : "Samsung", "category" : "Cell Phones" }, "num_products" : 1 }
{ "_id" : { "manufacturer" : "Samsung", "category" : "Tablets" }, "num_products" : 1 }
{ "_id" : { "manufacturer" : "Google", "category" : "Tablets" }, "num_products" : 1 }
{ "_id" : { "manufacturer" : "Sony", "category" : "Laptops" }, "num_products" : 1 }
bye
u64@vm:~/Desktop$
```

###### _id field can be a document

```sh
u64@vm:~/Desktop$ mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Server has startup warnings:
2018-04-22T11:05:02.839-0700 I STORAGE  [initandlisten]
2018-04-22T11:05:02.839-0700 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2018-04-22T11:05:02.839-0700 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2018-04-22T11:05:05.406-0700 I CONTROL  [initandlisten]
2018-04-22T11:05:05.406-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-04-22T11:05:05.406-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-04-22T11:05:05.406-0700 I CONTROL  [initandlisten]
> db.foo.insert({_id:{name:"kan1shka9", class:"m101"}, hometown:"LA"})
WriteResult({ "nInserted" : 1 })
> db.foo.find()
{ "_id" : ObjectId("5acea21079160f2994f5afaf"), "a" : 1, "b" : 2 }
{ "_id" : ObjectId("5acea2d679160f2994f5afb0"), "a" : 3, "b" : [ 3, 5, 7 ] }
{ "_id" : ObjectId("5acea3c279160f2994f5afb2"), "a" : [ 3, 4, 6 ], "b" : 7 }
{ "_id" : { "name" : "kan1shka9", "class" : "m101" }, "hometown" : "LA" }
>
> db.foo.insert({_id:{name:"kan1shka9", class:"m101"}, hometown:"LA"})
WriteResult({
	"nInserted" : 0,
	"writeError" : {
		"code" : 11000,
		"errmsg" : "E11000 duplicate key error collection: test.foo index: _id_ dup key: { : { name: \"kan1shka9\", class: \"m101\" } }"
	}
})
>
```

###### Aggregation Expressions

![](images/30/6.png)

###### sum

`using_sum__m101p_52b1f103e2d4235b7e5ebb74.js`

```js
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 sum_prices:{$sum:"$price"}
     }
    }
])
```

```sh
u64@vm:~/Desktop$ mongo < using_sum__m101p_52b1f103e2d4235b7e5ebb74.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
{ "_id" : { "maker" : "Amazon" }, "sum_prices" : 328 }
{ "_id" : { "maker" : "Apple" }, "sum_prices" : 2296 }
{ "_id" : { "maker" : "Google" }, "sum_prices" : 199 }
{ "_id" : { "maker" : "Samsung" }, "sum_prices" : 1014.98 }
{ "_id" : { "maker" : "Sony" }, "sum_prices" : 499 }
bye
u64@vm:~/Desktop$
```

```sh
u64@vm:~/Desktop$ mongoimport zips.json
2018-04-22T12:01:23.313-0700	no collection specified
2018-04-22T12:01:23.315-0700	using filename 'zips' as collection
2018-04-22T12:01:23.339-0700	connected to: localhost
2018-04-22T12:01:23.825-0700	imported 29353 documents
u64@vm:~/Desktop$
```

`quiz_sum_by_state__m101p_52b208b5e2d42362670d8246.js`

```js
use agg;
db.zips.aggregate([{"$group":{"_id":"$state", "population":{$sum:"$pop"}}}])
```

```sh
u64@vm:~/Desktop$ mongo < quiz_sum_by_state__m101p_52b208b5e2d42362670d8246.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
bye
u64@vm:~/Desktop$
```

###### avg

`using_avg__m101p_52b1f306e2d4235b7e5ebb77.js`

```js
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "category":"$category"
	 },
	 avg_price:{$avg:"$price"}
     }
    }
])
```

```sh
u64@vm:~/Desktop$ mongo < using_avg__m101p_52b1f306e2d4235b7e5ebb77.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
{ "_id" : { "category" : "Laptops" }, "avg_price" : 499 }
{ "_id" : { "category" : "Cell Phones" }, "avg_price" : 563.99 }
{ "_id" : { "category" : "Tablets" }, "avg_price" : 396.4271428571428 }
bye
u64@vm:~/Desktop$
```

###### addToSet

`using_addToSet__m101p_52b1f3dde2d4235b7e5ebb79.js`

```js
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 categories:{$addToSet:"$category"}
     }
    }
])
```

```sh
u64@vm:~/Desktop$ mongo < using_addToSet__m101p_52b1f3dde2d4235b7e5ebb79.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
{ "_id" : { "maker" : "Amazon" }, "categories" : [ "Tablets" ] }
{ "_id" : { "maker" : "Apple" }, "categories" : [ "Laptops", "Tablets" ] }
{ "_id" : { "maker" : "Google" }, "categories" : [ "Tablets" ] }
{ "_id" : { "maker" : "Samsung" }, "categories" : [ "Tablets", "Cell Phones" ] }
{ "_id" : { "maker" : "Sony" }, "categories" : [ "Laptops" ] }
bye
u64@vm:~/Desktop$
```

###### push

`using_push__m101p_52b1f44ae2d4235b7e5ebb7c.js`

```js
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 categories:{$push:"$category"}
     }
    }
])
```

```sh
u64@vm:~/Desktop$ mongo < using_push__m101p_52b1f44ae2d4235b7e5ebb7c.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
{ "_id" : { "maker" : "Amazon" }, "categories" : [ "Tablets", "Tablets" ] }
{ "_id" : { "maker" : "Apple" }, "categories" : [ "Tablets", "Tablets", "Tablets", "Laptops" ] }
{ "_id" : { "maker" : "Google" }, "categories" : [ "Tablets" ] }
{ "_id" : { "maker" : "Samsung" }, "categories" : [ "Cell Phones", "Tablets" ] }
{ "_id" : { "maker" : "Sony" }, "categories" : [ "Laptops" ] }
bye
u64@vm:~/Desktop$
```

###### max and min

`using_max__m101p_52b1f47ae2d4235b7e5ebb7f.js`

```js
use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 maxprice:{$max:"$price"}
     }
    }
])
```

```sh
u64@vm:~/Desktop$ mongo < using_max__m101p_52b1f47ae2d4235b7e5ebb7f.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
{ "_id" : { "maker" : "Amazon" }, "maxprice" : 199 }
{ "_id" : { "maker" : "Apple" }, "maxprice" : 699 }
{ "_id" : { "maker" : "Google" }, "maxprice" : 199 }
{ "_id" : { "maker" : "Samsung" }, "maxprice" : 563.99 }
{ "_id" : { "maker" : "Sony" }, "maxprice" : 499 }
bye
u64@vm:~/Desktop$
```

###### Double group stages

`single_group__m101p_52b1f5b5e2d4235b7e5ebb87.js`

```js
use agg
db.grades.aggregate([
    {'$group':{_id:{class_id:"$class_id", student_id:"$student_id"}, 'average':{"$avg":"$score"}}}])
```

```sh
u64@vm:~/Desktop$ mongo < single_group__m101p_52b1f5b5e2d4235b7e5ebb87.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
bye
u64@vm:~/Desktop$
```

`double_group__m101p_52b1f544e2d4235b7e5ebb84.js`

```js
use agg
db.grades.aggregate([
    {'$group':{_id:{class_id:"$class_id", student_id:"$student_id"}, 'average':{"$avg":"$score"}}},
    {'$group':{_id:"$_id.class_id", 'average':{"$avg":"$average"}}}])
```

```sh
u64@vm:~/Desktop$ mongo < double_group__m101p_52b1f544e2d4235b7e5ebb84.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
bye
u64@vm:~/Desktop$
```

###### project

![](images/30/7.png)

`quiz_using_project__m101p_52b1f62ae2d42360b66c713f.js`

```js
use agg
db.zips.aggregate([{$project:{_id:0, city:{$toLower:"$city"}, pop:1, state:1, zip:"$_id"}}])
```

```sh
u64@vm:~/Desktop$ mongo < quiz_using_project__m101p_52b1f62ae2d42360b66c713f.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
bye
u64@vm:~/Desktop$
```

`reshape_products__m101p_52b1f77ee2d42360b66c7140.js`

```js
use agg
db.products.aggregate([
    {$project:
     {
	 _id:0,
	 'maker': {$toLower:"$manufacturer"},
	 'details': {'category': "$category",
		     'price' : {"$multiply":["$price",10]}
		    },
	 'item':'$name'
     }
    }
])
```

```sh
u64@vm:~/Desktop$ mongo < reshape_products__m101p_52b1f77ee2d42360b66c7140.js
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db agg
{ "maker" : "apple", "details" : { "category" : "Tablets", "price" : 4990 }, "item" : "iPad 16GB Wifi" }
{ "maker" : "apple", "details" : { "category" : "Tablets", "price" : 5990 }, "item" : "iPad 32GB Wifi" }
{ "maker" : "apple", "details" : { "category" : "Tablets", "price" : 6990 }, "item" : "iPad 64GB Wifi" }
{ "maker" : "samsung", "details" : { "category" : "Cell Phones", "price" : 5639.9 }, "item" : "Galaxy S3" }
{ "maker" : "samsung", "details" : { "category" : "Tablets", "price" : 4509.9 }, "item" : "Galaxy Tab 10" }
{ "maker" : "sony", "details" : { "category" : "Laptops", "price" : 4990 }, "item" : "Vaio" }
{ "maker" : "apple", "details" : { "category" : "Laptops", "price" : 4990 }, "item" : "Macbook Air 13inch" }
{ "maker" : "google", "details" : { "category" : "Tablets", "price" : 1990 }, "item" : "Nexus 7" }
{ "maker" : "amazon", "details" : { "category" : "Tablets", "price" : 1290 }, "item" : "Kindle Paper White" }
{ "maker" : "amazon", "details" : { "category" : "Tablets", "price" : 1990 }, "item" : "Kindle Fire" }
bye
u64@vm:~/Desktop$
```

###### match

`match__m101p_52b203fce2d42362670d8234.js`

```js
use agg
db.zips.aggregate([
    {$match:
     {
	 state:"NY"
     }
    }
])
```

`match_and_group__m101p_52b20442e2d42362670d8235.js`

```js
use agg
db.zips.aggregate([
    {$match:
     {
	 state:"NY"
     }
    },
    {$group:
     {
	 _id: "$city",
	 population: {$sum:"$pop"},
	 zip_codes: {$addToSet: "$_id"}
     }
    }
])
```

`match_group_and_project__m101p_52b20448e2d42362670d8236.js`

```js
use agg
db.zips.aggregate([
    {$match:
     {
	 state:"NY"
     }
    },
    {$group:
     {
	 _id: "$city",
	 population: {$sum:"$pop"},
	 zip_codes: {$addToSet: "$_id"}
     }
    },
    {$project:
     {
	 _id: 0,
	 city: "$_id",
	 population: 1,
	 zip_codes:1
     }
    }

])
```

###### text

![](images/30/8.png)

![](images/30/9.png)

![](images/30/10.png)

![](images/30/11.png)

![](images/30/12.png)

###### sort

![](images/30/13.png)

`sort__m101p_52b20714e2d42362670d823d.js`

```js
use agg
db.zips.aggregate([
    {$match:
     {
	 state:"NY"
     }
    },
    {$group:
     {
	 _id: "$city",
	 population: {$sum:"$pop"},
     }
    },
    {$project:
     {
	 _id: 0,
	 city: "$_id",
	 population: 1,
     }
    },
    {$sort:
     {
	 population:-1
     }
    }



])
```

![](images/30/14.png)

###### limit and skip

![](images/30/15.png)

`limit__m101p_52b2071ae2d42362670d823e.js`

```js
use agg
db.zips.aggregate([
    {$match:
     {
	 state:"NY"
     }
    },
    {$group:
     {
	 _id: "$city",
	 population: {$sum:"$pop"},
     }
    },
    {$project:
     {
	 _id: 0,
	 city: "$_id",
	 population: 1,
     }
    },
    {$sort:
     {
	 population:-1
     }
    },
    {$skip: 10},
    {$limit: 5}
])
```

![](images/30/16.png)

###### first and last

![](images/30/17.png)

`first__m101p_52b208b6e2d42362670d8247.js`

```js
use agg
db.zips.aggregate([
    /* get the population of every city in every state */
    {$group:
     {
	 _id: {state:"$state", city:"$city"},
	 population: {$sum:"$pop"},
     }
    },
     /* sort by state, population */
    {$sort:
     {"_id.state":1, "population":-1}
    },

    /* group by state, get the first item in each group */
    {$group:
     {
	 _id:"$_id.state",
	 city: {$first: "$_id.city"},
	 population: {$first:"$population"}
     }
    },

    /* now sort by state again */
    {$sort:
     {"_id":1}
    }
])
```

![](images/30/18.png)

`first_phase1__m101p_52b208b4e2d42362670d8245.js`

```js
use agg
db.zips.aggregate([
    /* get the population of every city in every state */
    {$group:
     {
	 _id: {state:"$state", city:"$city"},
	 population: {$sum:"$pop"},
     }
    }
])
```

![](images/30/19.png)

`first_phase2__m101p_52b208b3e2d42362670d8244.js`

```js
use agg
db.zips.aggregate([
    /* get the population of every city in every state */
    {$group:
     {
	 _id: {state:"$state", city:"$city"},
	 population: {$sum:"$pop"},
     }
    },
     /* sort by state, population */
    {$sort:
     {"_id.state":1, "population":-1}
    }
])
```

![](images/30/20.png)

`first_phase3__m101p_52b208b2e2d42362670d8243.js`

```js
use agg
db.zips.aggregate([
    /* get the population of every city in every state */
    {$group:
     {
	 _id: {state:"$state", city:"$city"},
	 population: {$sum:"$pop"},
     }
    },
     /* sort by state, population */
    {$sort:
     {"_id.state":1, "population":-1}
    },
    /* group by state, get the first item in each group */
    {$group:
     {
	 _id:"$_id.state",
	 city: {$first: "$_id.city"},
	 population: {$first:"$population"}
     }
    }
])
```

![](images/30/21.png)