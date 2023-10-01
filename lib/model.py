from sqlalchemy import create_engine,Column,Integer,String
import sqlalchemy

class Restautant():
    __tablename__ = "restaurants"

    id = Column(Integer,primary_key=True)
    name = Column(String())
    price = Column(Integer())


    def customers():
        #returns a collection of all the reviews for the `Restaurant`
        pass

    def reviews():
        #returns a collection of all the customers who reviewed the `Restaurant`
        pass

class Review():
    __tablename__ = 'reviews'

    id = Column(Integer,primary_key=True)

    
    def customer():
        #should return the `Customer` instance for this review
        pass
    def restaurant():
        #should return the `Restaurant` instance for this review
        pass

class Customer():
    __tablename__ = "customers"

    id = Column(Integer,primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    def reviews():
        #should return a collection of all the reviews that the `Customer` has left
        pass

    def restaurants():
        # should return a collection of all the restaurants that the `Customer` has reviewed
        pass