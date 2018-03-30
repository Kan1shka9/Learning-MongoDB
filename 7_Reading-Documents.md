#### 7. Reading Documents

- [insertMany]()
- [Find the entire document]()
- [Equality matching based on a specific element]()
- [Equality matching based on specific elements]()
- [Equality matching based on a nested element]()
- [Equality match based on the entire array]()
- [Equality matching based position in an array]()
- [Cursors]()
- [Projections]()

###### insertMany

```
> db.moviesScratch.insertMany(
... ...     [
... ...         {
... ...       "_id" : "tt0084726",
... ...       "title" : "Star Trek II: The Wrath of Khan",
... ...       "year" : 1982,
... ...       "type" : "movie"
... ...           },
... ...           {
... ...       "_id" : "tt0796366",
... ...       "title" : "Star Trek",
... ...       "year" : 2009,
... ...       "type" : "movie"
... ...           },
... ...           {
... ...       "_id" : "tt0084776",
... ...       "title" : "Star Trek II: The Wrath of Khan",
... ...       "year" : 1982,
... ...       "type" : "movie"
... ...           },
... ...           {
... ...       "_id" : "tt1408101",
... ...       "title" : "Star Trek Into Darkness",
... ...       "year" : 2013,
... ...       "type" : "movie"
... ...           },
... ...           {
... ...       "_id" : "tt0117731",
... ...       "title" : "Star Trek: First Contact",
... ...       "year" : 1996,
... ...       "type" : "movie"
... ...         }
... ...     ]
... ... );
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
> db.movieDB.insertMany(
...     [
...         {
...         "_id" : ObjectId("5692a15524de1e0ce2dfcfa3"),
...         "title" : "Toy Story 3",
...         "year" : 2010,
...         "rated" : "G",
...         "released" : ISODate("2010-06-18T04:00:00Z"),
...         "runtime" : 103,
...         "countries" : [
...             "USA"
...         ],
...         "genres" : [
...             "Animation",
...             "Adventure",
...             "Comedy"
...         ],
...         "director" : "Lee Unkrich",
...         "writers" : [
...             "John Lasseter",
...             "Andrew Stanton",
...             "Lee Unkrich",
...             "Michael Arndt"
...         ],
...         "actors" : [
...             "Tom Hanks",
...             "Tim Allen",
...             "Joan Cusack",
...             "Ned Beatty"
...         ],
...         "plot" : "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
...         "poster" : "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX300.jpg",
...         "imdb" : {
...             "id" : "tt0435761",
...             "rating" : 8.4,
...             "votes" : 500084
...         },
...         "tomato" : {
...             "meter" : 99,
...             "image" : "certified",
...             "rating" : 8.9,
...             "reviews" : 287,
...             "fresh" : 283,
...             "consensus" : "Deftly blending comedy, adventure, and honest emotion, Toy Story 3 is a rare second sequel that really works.",
...             "userMeter" : 89,
...             "userRating" : 4.3,
...             "userReviews" : 602138
...         },
...         "metacritic" : 92,
...         "awards" : {
...             "wins" : 56,
...             "nominations" : 86,
...             "text" : "Won 2 Oscars. Another 56 wins & 86 nominations."
...         },
...         "type" : "movie"
...         }
...     ]
... );
{
	"acknowledged" : true,
	"insertedIds" : [
		ObjectId("5692a15524de1e0ce2dfcfa3")
	]
}
>
```

###### Find the entire document

```
> db.moviesScratch.find().pretty()
{
	"_id" : "tt0084726",
	"title" : "Star Trek II: The Wrath of Khan",
	"year" : 1982,
	"type" : "movie"
}
{
	"_id" : "tt0796366",
	"title" : "Star Trek",
	"year" : 2009,
	"type" : "movie"
}
{
	"_id" : "tt0084776",
	"title" : "Star Trek II: The Wrath of Khan",
	"year" : 1982,
	"type" : "movie"
}
{
	"_id" : "tt1408101",
	"title" : "Star Trek Into Darkness",
	"year" : 2013,
	"type" : "movie"
}
{
	"_id" : "tt0117731",
	"title" : "Star Trek: First Contact",
	"year" : 1996,
	"type" : "movie"
}
>
```

###### Equality matching based on a specific element

```
> db.moviesScratch.find( { year: 1982} ).pretty()
{
	"_id" : "tt0084726",
	"title" : "Star Trek II: The Wrath of Khan",
	"year" : 1982,
	"type" : "movie"
}
{
	"_id" : "tt0084776",
	"title" : "Star Trek II: The Wrath of Khan",
	"year" : 1982,
	"type" : "movie"
}
>
```

```
> db.moviesScratch.find( { year: 1982} ).count()
2
>
```

###### Equality matching based on specific elements

```
> db.moviesScratch.find( { year: 1982, _id: "tt0084726"} ).pretty()
{
	"_id" : "tt0084726",
	"title" : "Star Trek II: The Wrath of Khan",
	"year" : 1982,
	"type" : "movie"
}
>
```

```
> db.moviesScratch.find( { year: 1982, _id: "tt0084726"} ).count()
1
>
```

###### Equality matching based on a nested element

```
> db.movieDB.find( {"tomato.meter": 99} ).pretty()
{
	"_id" : ObjectId("5692a15524de1e0ce2dfcfa3"),
	"title" : "Toy Story 3",
	"year" : 2010,
	"rated" : "G",
	"released" : ISODate("2010-06-18T04:00:00Z"),
	"runtime" : 103,
	"countries" : [
		"USA"
	],
	"genres" : [
		"Animation",
		"Adventure",
		"Comedy"
	],
	"director" : "Lee Unkrich",
	"writers" : [
		"John Lasseter",
		"Andrew Stanton",
		"Lee Unkrich",
		"Michael Arndt"
	],
	"actors" : [
		"Tom Hanks",
		"Tim Allen",
		"Joan Cusack",
		"Ned Beatty"
	],
	"plot" : "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
	"poster" : "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX300.jpg",
	"imdb" : {
		"id" : "tt0435761",
		"rating" : 8.4,
		"votes" : 500084
	},
	"tomato" : {
		"meter" : 99,
		"image" : "certified",
		"rating" : 8.9,
		"reviews" : 287,
		"fresh" : 283,
		"consensus" : "Deftly blending comedy, adventure, and honest emotion, Toy Story 3 is a rare second sequel that really works.",
		"userMeter" : 89,
		"userRating" : 4.3,
		"userReviews" : 602138
	},
	"metacritic" : 92,
	"awards" : {
		"wins" : 56,
		"nominations" : 86,
		"text" : "Won 2 Oscars. Another 56 wins & 86 nominations."
	},
	"type" : "movie"
}
>
```

```
> db.movieDB.find( {"tomato.meter": 99} ).count()
1
>
```

###### Equality match based on the entire array

```
> db.movieDB.find({ "writers": ["John Lasseter", "Andrew Stanton", "Lee Unkrich", "Michael Arndt"] }).pretty()
{
	"_id" : ObjectId("5692a15524de1e0ce2dfcfa3"),
	"title" : "Toy Story 3",
	"year" : 2010,
	"rated" : "G",
	"released" : ISODate("2010-06-18T04:00:00Z"),
	"runtime" : 103,
	"countries" : [
		"USA"
	],
	"genres" : [
		"Animation",
		"Adventure",
		"Comedy"
	],
	"director" : "Lee Unkrich",
	"writers" : [
		"John Lasseter",
		"Andrew Stanton",
		"Lee Unkrich",
		"Michael Arndt"
	],
	"actors" : [
		"Tom Hanks",
		"Tim Allen",
		"Joan Cusack",
		"Ned Beatty"
	],
	"plot" : "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
	"poster" : "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX300.jpg",
	"imdb" : {
		"id" : "tt0435761",
		"rating" : 8.4,
		"votes" : 500084
	},
	"tomato" : {
		"meter" : 99,
		"image" : "certified",
		"rating" : 8.9,
		"reviews" : 287,
		"fresh" : 283,
		"consensus" : "Deftly blending comedy, adventure, and honest emotion, Toy Story 3 is a rare second sequel that really works.",
		"userMeter" : 89,
		"userRating" : 4.3,
		"userReviews" : 602138
	},
	"metacritic" : 92,
	"awards" : {
		"wins" : 56,
		"nominations" : 86,
		"text" : "Won 2 Oscars. Another 56 wins & 86 nominations."
	},
	"type" : "movie"
}
>
```

```
> db.movieDB.find({ "writers": ["John Lasseter", "Andrew Stanton", "Lee Unkrich", "Michael Arndt"] }).count()
1
>
```

```
> db.movieDB.find({ "writers": ["John Lasseter", "Andrew Stanton", "Michael Arndt", "Lee Unkrich"] }).count()
0
>
```

```
> db.movieDB.find({ "writers": ["John Lasseter", "Andrew Stanton", "Lee Unkrich"] }).count()
0
>
```

```
> db.movieDB.find({ "writers": "John Lasseter" }).count()
1
>
```

- Note
	- **```Array matching is strict as it requires the exact (match) elements and the order of the elements also matters which is not the case with string matching```**

###### Equality matching based position in an array

```
> db.movieDB.find({ "writers.0": "John Lasseter" }).pretty()
{
	"_id" : ObjectId("5692a15524de1e0ce2dfcfa3"),
	"title" : "Toy Story 3",
	"year" : 2010,
	"rated" : "G",
	"released" : ISODate("2010-06-18T04:00:00Z"),
	"runtime" : 103,
	"countries" : [
		"USA"
	],
	"genres" : [
		"Animation",
		"Adventure",
		"Comedy"
	],
	"director" : "Lee Unkrich",
	"writers" : [
		"John Lasseter",
		"Andrew Stanton",
		"Lee Unkrich",
		"Michael Arndt"
	],
	"actors" : [
		"Tom Hanks",
		"Tim Allen",
		"Joan Cusack",
		"Ned Beatty"
	],
	"plot" : "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
	"poster" : "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX300.jpg",
	"imdb" : {
		"id" : "tt0435761",
		"rating" : 8.4,
		"votes" : 500084
	},
	"tomato" : {
		"meter" : 99,
		"image" : "certified",
		"rating" : 8.9,
		"reviews" : 287,
		"fresh" : 283,
		"consensus" : "Deftly blending comedy, adventure, and honest emotion, Toy Story 3 is a rare second sequel that really works.",
		"userMeter" : 89,
		"userRating" : 4.3,
		"userReviews" : 602138
	},
	"metacritic" : 92,
	"awards" : {
		"wins" : 56,
		"nominations" : 86,
		"text" : "Won 2 Oscars. Another 56 wins & 86 nominations."
	},
	"type" : "movie"
}
>
```

```
> db.movieDB.find({ "writers.0": "John Lasseter" }).count()
1
>
```

```
> db.movieDB.find({ "writers.1": "John Lasseter" }).count()
0
>
```

###### Cursors

```
> db.moviesScratch.find()
{ "_id" : "tt0084726", "title" : "Star Trek II: The Wrath of Khan", "year" : 1982, "type" : "movie" }
{ "_id" : "tt0796366", "title" : "Star Trek", "year" : 2009, "type" : "movie" }
{ "_id" : "tt0084776", "title" : "Star Trek II: The Wrath of Khan", "year" : 1982, "type" : "movie" }
{ "_id" : "tt1408101", "title" : "Star Trek Into Darkness", "year" : 2013, "type" : "movie" }
{ "_id" : "tt0117731", "title" : "Star Trek: First Contact", "year" : 1996, "type" : "movie" }
>
```

`it` to iterate 

```
> var c = db.moviesScratch.find()
```

```
> var doc = function() { return c.hasNext() ? c.next() : null; }
```

```
> c.objsLeftInBatch();
5
>
```

```
> doc()
{
	"_id" : "tt0084726",
	"title" : "Star Trek II: The Wrath of Khan",
	"year" : 1982,
	"type" : "movie"
}
> doc()
{
	"_id" : "tt0796366",
	"title" : "Star Trek",
	"year" : 2009,
	"type" : "movie"
}
> doc()
{
	"_id" : "tt0084776",
	"title" : "Star Trek II: The Wrath of Khan",
	"year" : 1982,
	"type" : "movie"
}
>
```

```
> c.objsLeftInBatch();
2
>
```

###### Projections

- It is a way to reduce the size of data returned by any query.
- Reduce network overhead
- Reduce processing requirements

```
> db.movieDB.find({ "writers": "John Lasseter" }).pretty()
{
	"_id" : ObjectId("5692a15524de1e0ce2dfcfa3"),
	"title" : "Toy Story 3",
	"year" : 2010,
	"rated" : "G",
	"released" : ISODate("2010-06-18T04:00:00Z"),
	"runtime" : 103,
	"countries" : [
		"USA"
	],
	"genres" : [
		"Animation",
		"Adventure",
		"Comedy"
	],
	"director" : "Lee Unkrich",
	"writers" : [
		"John Lasseter",
		"Andrew Stanton",
		"Lee Unkrich",
		"Michael Arndt"
	],
	"actors" : [
		"Tom Hanks",
		"Tim Allen",
		"Joan Cusack",
		"Ned Beatty"
	],
	"plot" : "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
	"poster" : "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX300.jpg",
	"imdb" : {
		"id" : "tt0435761",
		"rating" : 8.4,
		"votes" : 500084
	},
	"tomato" : {
		"meter" : 99,
		"image" : "certified",
		"rating" : 8.9,
		"reviews" : 287,
		"fresh" : 283,
		"consensus" : "Deftly blending comedy, adventure, and honest emotion, Toy Story 3 is a rare second sequel that really works.",
		"userMeter" : 89,
		"userRating" : 4.3,
		"userReviews" : 602138
	},
	"metacritic" : 92,
	"awards" : {
		"wins" : 56,
		"nominations" : 86,
		"text" : "Won 2 Oscars. Another 56 wins & 86 nominations."
	},
	"type" : "movie"
}
>
```

```
> db.movieDB.find( {"writers": "John Lasseter"}, {title: 1} ).pretty()
{ "_id" : ObjectId("5692a15524de1e0ce2dfcfa3"), "title" : "Toy Story 3" }
>
```

```
> db.movieDB.find( {"writers": "John Lasseter"}, {title: 1, _id: 0} ).pretty()
{ "title" : "Toy Story 3" }
>
```

```
> db.movieDB.find( {"writers": "John Lasseter"}, {writers: 0, actors: 0, awards: 0, tomato: 0, _id: 0} ).pretty()
{
	"title" : "Toy Story 3",
	"year" : 2010,
	"rated" : "G",
	"released" : ISODate("2010-06-18T04:00:00Z"),
	"runtime" : 103,
	"countries" : [
		"USA"
	],
	"genres" : [
		"Animation",
		"Adventure",
		"Comedy"
	],
	"director" : "Lee Unkrich",
	"plot" : "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
	"poster" : "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX300.jpg",
	"imdb" : {
		"id" : "tt0435761",
		"rating" : 8.4,
		"votes" : 500084
	},
	"metacritic" : 92,
	"type" : "movie"
}
>
```