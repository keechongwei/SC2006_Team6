from bson.objectid import ObjectId
from enum import Enum


class InstitutionType(Enum):
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    JUNIOR_COLLEGE = "JUNIOR COLLEGE"
    UNIVERSITY = "UNIVERSITY"
    POLYTECHNIC = "POLYTECHNIC"
    ITE = "ITE"
    OTHER = "OTHER"


class Institution:

    COLLECTION = 'Institution'

    def __init__(self, id=None, name=None, type=None, location=None, 
                 latitude=None, longitude=None, ranking=None, 
                 entryRequirements=None, coursesOffered=None, 
                 coCurricularActivities=None, specialPrograms=None,
                 description=None, imageUrl=None):
        self.id = id if id else str(ObjectId())
        self.name = name
        self.type = type
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.ranking = ranking
        self.entryRequirements = entryRequirements or []
        self.coursesOffered = coursesOffered or []
        self.coCurricularActivities = coCurricularActivities or []
        self.specialPrograms = specialPrograms or []
        self.description = description
        self.imageUrl = imageUrl

    def to_dict(self):
        """Convert the Institution object to a dictionary for MongoDB storage"""
        return {
            "_id": ObjectId(self.id) if isinstance(self.id, str) else self.id,
            "name": self.name,
            "type": self.type.value if isinstance(self.type, InstitutionType) else self.type,
            "location": self.location,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "ranking": self.ranking,
            "entryRequirements": self.entryRequirements,
            "coursesOffered": self.coursesOffered,
            "coCurricularActivities": self.coCurricularActivities,
            "specialPrograms": self.specialPrograms,
            "description": self.description,
            "imageUrl": self.imageUrl
        }
    
    @staticmethod
    def from_dict(data):
        """Create an Institution object from a MongoDB document"""
        return Institution(
            id=str(data.get('_id')) if data.get('_id') else None,
            name=data.get('name'),
            type=data.get('type'),
            location=data.get('location'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            ranking=data.get('ranking'),
            entryRequirements=data.get('entryRequirements'),
            coursesOffered=data.get('coursesOffered'),
            coCurricularActivities=data.get('coCurricularActivities'),
            specialPrograms=data.get('specialPrograms'),
            description=data.get('description'),
            imageUrl=data.get('imageUrl')
        )
        
    def save(self, db):
        """Save the institution to MongoDB"""
        institution_dict = self.to_dict()
        
        result = db.db[self.COLLECTION].insert_one(institution_dict)
        self.id = str(result.inserted_id)
        
        return self.id
    
    @staticmethod
    def find_all(db):
        """Get all institutions from the database"""
        result = list(db.db['Institution'].find({}))
    
    # Convert ObjectId to string for JSON serialization
        for institution in result:
            if '_id' in institution:
                institution['_id'] = str(institution['_id'])
    
        return result
    
