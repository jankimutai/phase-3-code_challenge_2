from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base
import sqlalchemy
Base = declarative_base()
engine = create_engine('sqlite3:///model.db')
Session = sessionmaker(bind=engine)
session = Session()

class Restautant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer,primary_key=True)
    name = Column(String())
    price = Column(Integer())

    # Object Relationship Methods
    def customers(self):
        #returns a collection of all the reviews for the `Restaurant`
        pass

    def reviews():
        #returns a collection of all the customers who reviewed the `Restaurant`
        pass

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer,primary_key=True)

    #Object Relationship Methods
    def customer(self):
        #should return the `Customer` instance for this review
        return self._customer
        pass
    def restaurant(self):
        #should return the `Restaurant` instance for this review
        return self._restaurant
        pass
    def full_review():
        pass

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer,primary_key=True)
    first_name = Column(String())
    last_name = Column(String())


    #Object Relationship Methods
    def reviews():
        #should return a collection of all the reviews that the `Customer` has left
        pass

    def restaurants():
        # should return a collection of all the restaurants that the `Customer` has reviewed
        pass

    #Aggregate and Relationship Methods
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def favorite_restaurant(self):
        pass

    def add_review(self,restaurant, rating):
        add_review = Review(customer = self, restaurant = restaurant, rating = rating)
        session.add(add_review)
        session.commit()
    def delete_reviews(self,restaurant):
        #takes a `restaurant` (an instance of the `Restaurant` class)
        #removes **all** their reviews for this restaurant

        #for loop maybe:
        #session.delete(review)
        pass


