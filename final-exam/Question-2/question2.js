use enron
db.messages.aggregate([{
        $unwind: '$headers.To'
    },

    {
        $group: {
            _id: {
                '_id': '$_id',
                From: '$headers.From'
            },
            To: {
                $addToSet: '$headers.To'
            }
        }
    },
    {
        '$unwind': '$To'
    },
    {
        '$group': {
            _id: {
                'From': '$_id.From',
                'To': '$To'

            },
            count: {
                '$sum': 1
            }
        }
    },
    {
        '$sort': {
            'count': -1
        }
    },
    {
        '$limit': 10
    }
])