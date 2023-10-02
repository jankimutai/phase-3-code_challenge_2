#!/usr/bin/python3

from sqlalchemy import create_engine,Column,Integer,String,Float,Table,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,relationship,backref
import sqlalchemy

Base = declarative_base()

customer_restaurant = Table(
    'customer_restaurants',
    Base.metadata,
    Column('restaurant_id',ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id',ForeignKey('customers.id'), primary_key=True),
    extend_existing=True
)

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer,primary_key=True)
    name = Column(String())
    price = Column(Float())

    reviews = relationship('Review',back_populates='restaurants')
    customers = relationship('Customer',secondary=customer_restaurant,backref=backref('restaurants'))

    # Object Relationship Methods
    def customers(self):
        #returns a collection of all the customers who reviewed the `Restaurant`
        print([review.customer_id for review in self.reviews])
        #return session.query(Restaurant).all()
    

    def reviews(self):
        #returns a collection of all the reviews for the `Restaurant`
        return [review for review in self.reviews]
        #return session.query(Restaurant).all()
    @classmethod
    def fanciest(cls):
        return session.query(Restaurant).order_by(Restaurant.price.desc()).first()
        

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer,primary_key=True)
    star_rating = Column(Integer())
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    #customer = relationship('Customer',back_populates='reviews')
    #restaurant = relationship('Restaurant',back_populates='reviews')

    #Object Relationship Methods
    def customer(self):
        #should return the `Customer` instance for this review
        return session.query(Customer).filter_by(Customer.id == self.customer_id).first()
    def restaurant(self):
        #should return the `Restaurant` instance for this review
        return self._restaurant
    @classmethod
    def full_review(self):
        #not complete
        return f'Review for {self.restaurant.name} by {self.customer.first_name} {self.customer.last_name}: {self.review.star_rating} stars.'
    

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer,primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    restaurants = relationship('Restaurant',secondary=customer_restaurant,back_populates=('customers'))

    review = relationship('Review',backref=backref('customers'))


    #Object Relationship Methods
    def reviews(self):
        #should return a collection of all the reviews that the `Customer` has left

        print(self.reviews)

    def restaurants(self):
        # should return a collection of all the restaurants that the `Customer` has reviewed
        return [review.customer for review in self.reviews]

    #Aggregate and Relationship Methods
    def full_name(self):
        print(f'{self.first_name} {self.last_name}')
    
    def favorite_restaurant(self):
        customer_reviews = [review.customer for review in self.reviews]
        #not complete
        return max(customer_reviews)

    def add_review(self,restaurant, rating):
        add_review = Review(customer = self, restaurant = restaurant, star_rating = rating)
        session.add(add_review)
        session.commit()
    def delete_reviews(self,restaurant):
        pass
        #for loop maybe:
        #session.delete(review)
        for review in self.reviews:
            if review.restaurant == restaurant:
                session.delete(review)
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


    # session.bulk_save_objects([restaurant1,restaurant2,restaurant3,restaurant4,customer1,customer2,customer3,customer4,customer5])
    # session.commit()
    review1 = Review(customer=customer1,restaurant = restaurant1,star_rating=7)
    # session.add(review1)
    # session.commit()

    #customer1.add_review(restaurant1,9)
    #customer2.add_review(restaurant4,8)
    
    



    





    


