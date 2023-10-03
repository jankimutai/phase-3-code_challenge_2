# phase-3-code_challenge_2
This code challenge uses SQLAlchemy to create a database schema for a restaurant review application. It defines three classes: Restaurant, Customer, and Review.
The Restaurant  has many `Review`s, a `Customer` has many `Review`s, and a `Review` belongs to a `Restaurant` and to a `Customer`. `Restaurant` - `Customer` is a many-to-many relationship.

# Topics
- SQLAlchemy Migrations
- SQLAlchemy Relationships
- Class and Instance Methods
- SQLAlchemy Querying

# Usage
1. Clone the repository and navigate to  the challenge directory
2. Run 'pipenv install' to install necessary dependencies
3. Navigate to the 'lib' directory and open 'models.py' and see my models

