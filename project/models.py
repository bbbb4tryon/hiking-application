from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///outdoors.db")
Session = sessionmaker(bind=engine)

Base = declarative_base()

# Define the join table
recommendations = Table(
    "recommendations",
    Base.metadata,
    Column("clothing_id", Integer, ForeignKey("clothing.id")),
    Column("range_id", Integer, ForeignKey("ranges.id")),
)

# Define the Ranges table
class Ranges(Base):
    __tablename__ = "ranges"
    id = Column(Integer, primary_key=True)
    range_name = Column(String)
    min_temp = Column(Integer)
    max_temp = Column(Integer)
    clothing = relationship("Clothing", secondary=recommendations, back_populates="ranges")

    def __repr__(self):
        return f"<Range(id={self.id}, range_name='{self.range_name}', min_temp={self.min_temp}, max_temp={self.max_temp})>"

# Define the Clothing table
class Clothing(Base):
    __tablename__ = "clothing"
    id = Column(Integer, primary_key=True)
    generic_name = Column(String)
    function = Column(String)
    ranges = relationship("Ranges", secondary=recommendations, back_populates="clothing")

    def __repr__(self):
        return f"<Clothing(id={self.id}, generic_name='{self.generic_name}', function='{self.function}')>"

Base.metadata.create_all(engine)
