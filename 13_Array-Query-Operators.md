#### 13. [Array Query Operators](https://docs.mongodb.com/manual/reference/operator/query-array/)

**Operator**|**Description**
:-----:|:-----:
$all|Matches arrays that contain all elements specified in the query.
$elemMatch|Selects documents if element in the array field matches all the specified $elemMatch conditions.
$size|Selects documents if the array field is a specified size.

```
db.movieDB.find({ genres: { $all: ["Comedy", "Crime", "Drama"] } }).pretty()
```

```
> db.movieDB.find({ countries: { $size: 1 } }).pretty()
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
boxOffice: [ { "country": "USA", "revenue": 41.3 },
             { "country": "Australia", "revenue": 2.9 },
             { "country": "UK", "revenue": 10.1 },
             { "country": "Germany", "revenue": 4.3 },
             { "country": "France", "revenue": 3.5 } ]
```

```
db.movieDB.find({ boxOffice: {$elemMatch: { country: "UK", revenue: { $gt: 15 } } } })
```