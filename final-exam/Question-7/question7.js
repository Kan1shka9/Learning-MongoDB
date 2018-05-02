use photoshare

print("Adding index on images")
db.albums.ensureIndex({'images':1});

print("iterating over images");
var cur = db.images.find();

var j = 0;
while (cur.hasNext()) {
	doc = cur.next();
	image_id = doc._id

	b = db.albums.find({images:image_id}).count()
	if (b == 0) {
		// delete it from images
		db.images.remove({_id:image_id})
		j++
	}
}

print("total removed was ", j)

db.images.find({'tags':'kittens'}).count();