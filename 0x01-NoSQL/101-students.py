#!/usr/bin/env python3
""" 101-students """

def top_students(mongo_collection):
    """fnction to get the average of each student scores
    and list the students in desc order
    """
    students = mongo_collection.aggregate(
        [ { "$project": {
            "_id": 1,
            "name": 1,
            "averageScore": {
                "$avg": {
                    "$avg": "$topics.score",
                },
            },
            "topics": 1,
        }},
        {
            "$sort": {"averageScore": -1},
        }
        ]
        )
    return students