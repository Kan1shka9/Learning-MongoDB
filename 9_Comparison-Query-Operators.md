#### 9. [Comparison Query Operators](https://docs.mongodb.com/manual/reference/operator/query-comparison/)

**Operator**|**Description**
:-----:|:-----:
$eq|Matches values that are equal to a specified value.
$gt|Matches values that are greater than a specified value.
$gte|Matches values that are greater than or equal to a specified value.
$in|Matches any of the values specified in an array.
$lt|Matches values that are less than a specified value.
$lte|Matches values that are less than or equal to a specified value.
$ne|Matches all values that are not equal to a specified value.
$nin|Matches none of the values specified in an array.

```
db.movieDetails.find({ runtime: { $gt: 90 } }).count()
```

```
db.movieDetails.find({ runtime: { $gt: 90, $lt: 120 } }).count()
```

```
db.movieDetails.find({ "tomato.meter": { $gte: 95 }, runtime: { $gt: 180 } })
```

```
db.movieDetails.find({ rated: { $ne: "UNRATED" } }).count()
```

```
db.movieDetails.find({ rated: { $in: ["G", "PG"] } }).pretty()
```