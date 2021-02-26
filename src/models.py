from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    # fav_planets = relationship('FavPlanets')
    # fav_characters = relationship('FavCharacters')


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username
            # do not serialize the password, its a security breach
        }

class Personaje(db.Model):
    __tablename__ = 'personajes'
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(50), unique=False, nullable=False)
    eye_color = db.Column(db.String(50), unique=False, nullable=False)
    birth_year = db.Column(db.String(50), unique=False, nullable=False)
    gender = db.Column(db.String(50), unique=False, nullable=False)
    name = db.Column(db.String(50), unique=False, nullable=False)
    url = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return '<Personaje %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "name": self.name,
            "url": self.url

            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    __tablename__ = 'planetas'
    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    surface_water = db.Column(db.Integer, unique=False, nullable=False)
    gravity = db.Column(db.String(80), unique=False, nullable=False)
    climate = db.Column(db.String(50), unique=False, nullable=False)
    terrain = db.Column(db.String(50), unique=False, nullable=False)
    name = db.Column(db.String(50), unique=False, nullable=False)
    url = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return '<Planeta %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "diameter": self.diameter,
            "population": self.population,
            "surface_water": self.surface_water,
            "gravity": self.gravity,
            "climate": self.climate,
            "terrain": self.terrain,
            "name": self.name,
            "url": self.url

            # do not serialize the password, its a security breach
        }





# class FavPlanets(Base):
#     __tablename__ = 'favPlanets'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     userId = Column(Integer, ForeignKey('user.id'))
#     planetId = Column(Integer, ForeignKey('planet.id'))
    

# class FavCharacters(Base):
#     __tablename__ = 'favCharacters'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     userId = Column(Integer, ForeignKey('user.id'))
#     characterId = Column(Integer, ForeignKey('character.id'))
    


#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')