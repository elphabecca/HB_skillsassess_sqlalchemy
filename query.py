"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

# I wrote the queries only -- I did not assign them to variables, and I hope that's OK.
# I also commented the queries out to make interactive mode less ... just less.

# Question: Get the brand with the **id** of 8."
# Brand.query.get(8)

# Question: Get all models with the **name** Corvette and the **brand_name** Chevrolet."
# Model.query.filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()

# Question: Get all models that are older than 1960."
# Model.query.filter(Model.year > 1960).all()

# Question: Get all brands that were founded after 1920."
# Brand.query.filter(Brand.founded > 1920).all()

# Question: Get all models with names that begin with \"Cor\"."
# Model.query.filter(Model.name.like('Cor%')).all()

# Question: Get all brands that were founded in 1903 and that are not yet discontinued."
# Brand.query.filter(Brand.founded==1903, Brand.discontinued==None).all()

# Question: Get all brands that are either 1) discontinued (at any time) or 2) founded before 1950."
# Brand.query.filter( (Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()

# Question: Get all models whose brand_name is not Chevrolet."
# Model.query.filter(Model.brand_name != 'Chevrolet').all()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # ATTEMPT 1 (works but my 2nd attempt is way better)
    # year_cars = db.session.query(Model.name,
    #                              Model.brand_name,
    #                              Brand.headquarters).filter(Model.year==year).join(Brand).all()

    # for name, brand_name, headquarters in year_cars:
    #     print "Name: %s\nBrand: %s\nHeadquarters: %s\n" % (name, brand_name, headquarters)


    year_models = Model.query.options(db.joinedload('brand')).filter(Model.year==year).all()

    for car in year_models:
        print "Name: %s\nBrand: %s\nHeadquarters: %s\n" % (car.name, car.brand_name, car.brand.headquarters)

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    all_brands_models = Brand.query.options(db.joinedload('models')).all()

    for brand in all_brands_models:
        print brand.name
        for model in brand.models:
            print "\t%s (%d)" % (model.name, model.year)

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# ANSWER: It's an object.
# It represents a query for class "Brand" where the name attribute is equal to "Ford".
# No query is run until it is "fetched", using methonds like .all(), .get(), or .one().

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# ANSWER: A bridge b/w two places (tables).  The point is to provide a functional
# path b/w two tables, but not add anything new to the db.  It's a sep. table
# because it holds and idea b/w items with a many to many relationship, but it's
# just a class of middle table. Well, I guess middle table would be a sub-class of
# an association table, b/c a middle class contains another piece of information
# (like a comment) whereas the association table just holds the idea and a place for the
# many to many relationship to be executed.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """returns a list of objects that are brands whose name contains or is equal 
    to the input string."""
    
    mystr_insert = '%'+mystr+'%'

    return Brand.query.filter(Brand.name.ilike(mystr_insert)).all()


def get_models_between(start_year, end_year):
    """returns a list of objects that are models with years that fall between the 
    start year (inclusive) and end year (exclusive)."""
    
    year_list = [year for year in range(start_year, end_year)]

    return Model.query.filter(Model.year.in_(year_list)).all()








