#!/usr/bin/python3

from sqlalchemy import create_engine,Column,Integer,String,Float,Table,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,relationship,backref
import sqlalchemy

Base = declarative_base()

customer_restaurant = Table(
    'customer_restaurants',
    Base.metadata,
    Column('restaurant_id',Integer,ForeignKey('restaurant.id')),
    Column('customer_id',Integer,ForeignKey('customer.id')),
    # extend_existing=True
)

class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer,primary_key=True)
    name = Column(String())
    price = Column(Float())

    reviews = relationship('Review',backref='restaurant')
    customers = relationship('Customer',secondary=customer_restaurant,back_populates=('restaurants'))

    # # Object Relationship Methods
    def review_customers(self):
        return [review.customer for review in self.reviews]
      
    def review_restaurant(self):
        return self.reviews

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()
    
    @classmethod
    def all_reviews(cls):
        return cls.reviews
class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer,primary_key=True)
    star_rating = Column(Integer())
    customer_id = Column(Integer(), ForeignKey('customer.id'))
    restaurant_id = Column(Integer(), ForeignKey('restaurant.id'))


    # # #Object Relationship Methods
    def review_customer(self):
        #should return the `Customer` instance for this review
        return self._customer
    def review_restaurant(self):
        #should return the `Restaurant` instance for this review
        return self._restaurant
    @classmethod
    def full_review(self):
        #not complete
        return f'Review for {self._restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars'
    

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer,primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    restaurants = relationship('Restaurant',secondary=customer_restaurant,back_populates=('customers'))
    reviews = relationship('Review',backref=backref('customer'))

    # #Object Relationship Methods
    def customerreviews(self):
        #should return a collection of all the reviews that the `Customer` has left
        print(self.reviews)

    def restaurantsreviews(self):
        # should return a collection of all the restaurants that the `Customer` has reviewed
        return [review.restaurant for review in self.reviews]

    # #Aggregate and Relationship Methods
    def full_name(self):
        print(f'{self.first_name} {self.last_name}')
    
    def favorite_restaurant(self):
        customer_reviews = [review.star_rating for review in self.reviews]
        #not complete
        return max(customer_reviews)
    def add_review(self, restaurant, rating):
        review = Review(restaurant_id=restaurant.id, star_rating=rating, customer_id=self.id)
        session.add(review)
        session.commit()

    def delete_reviews(self,restaurant):
        pass
        #for loop maybe:
        #session.delete(review)
        review = session.query(Review).filter_by(restaurant_id = restaurant.id)
        for item_review in review:
            session.delete(item_review)
        session.commit()
        
            
if __name__ == "__main__":
    engine = create_engine('sqlite:///model.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session = Session()

    restaurant1 = Restaurant(name='Maggies',price=4.7)
    restaurant2 = Restaurant(name='Pizza Hut',price=10.7)
    restaurant3 = Restaurant(name='Chicken Inn',price=14.7)
    restaurant4 = Restaurant(name='Sarova Woodlands',price=34.7)

    customer1 = Customer(first_name = "Jan",last_name="Kimutai")
    customer2 = Customer(first_name = "Bin",last_name="Amin")
    customer3 = Customer(first_name = "Laban",last_name="Kibet")
    customer4 = Customer(first_name = "Cynthia",last_name="Oloo")
    customer5 = Customer(first_name = "Brian",last_name="Ng'eno")

    # session.add_all([customer1,customer2,customer3,customer4,customer5,restaurant1,restaurant2,restaurant3,restaurant4])
    # session.commit()
    review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
    review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)
    review3 = Review(star_rating=3, restaurant=restaurant3, customer=customer3)

    # session.add_all([review1,review2,review3])
    # session.commit()
    customer3.add_review(restaurant=restaurant3,rating = 0)
    
    
    
    


    
    
    
    

    
    



    





    


