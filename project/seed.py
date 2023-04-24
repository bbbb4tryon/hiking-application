from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Clothing, Ranges, Base

# Create an engine to connect to the database
engine = create_engine('sqlite:///outdoors.db')

# Create all tables defined in models.py
Base.metadata.create_all(engine)

# Create a sessionmaker object to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# RANGES
sixtyplusplus = Ranges(
    range_name="very hot",  # very hot, hot, warm, cool, cold, very cold
    min_temp=65,
    max_temp=100
)
sixty = Ranges(
    range_name="hot",
    min_temp=60,
    max_temp=65)
fifty_two = Ranges(
    range_name="warm",
    min_temp=52,
    max_temp=59
)
forty = Ranges(
    range_name="cool",
    min_temp=40,
    max_temp=51
)
thirty = Ranges(
    range_name="cold",
    min_temp=30,
    max_temp=39
)
twenty_five = Ranges(
    range_name="very cold",
    min_temp=25,
    max_temp=29
)

# CLOTHING
shoes = Clothing(
    generic_name="Trail running sneakers",
    function="...for your feet!"
)
shorts = Clothing(
    generic_name="Shorts",
    function="Warm-weather bottom"
)
tshirt = Clothing(
    generic_name="Active t-shirt",
    function="Warm-weather top - no cotton"
)
sunshirt = Clothing(
    generic_name="Sunshirt",
    function="Warm-weather top plus sun protection"
)
pants = Clothing(
    generic_name="Pants",
    function="Cooler/cold-weather bottom"
)
rainjacket = Clothing(
    generic_name="Rain jacket",
    function="Covering top"
)
puffyjacket = Clothing(
    generic_name="Puffy jacket",
    function="Top for warmth"
)
fleecevest = Clothing(
    generic_name="Fleece vest",
    function="Warm top with added mobility"
)
shortsocks = Clothing(
    generic_name="Short socks",
    function="Sock for hot feet"
)
shortwoolsocks = Clothing(
    generic_name="Short wool socks",
    function="Cool-weather sock"
)
longwoolsocks = Clothing(
    generic_name="Long wool socks",
    function="Cold-weather sock"
)
everything = [
    shoes, shorts, tshirt, sunshirt, pants, rainjacket, puffyjacket, fleecevest, shortsocks, shortwoolsocks, longwoolsocks,

    sixtyplus, sixty, fifty_two, forty, thirty, twenty_five

    # range_id
]