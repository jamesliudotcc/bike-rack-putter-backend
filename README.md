# Bike Rack Need Hackathon Data Backend

This pulls from two data sources, Yelp, and a [list of bike racks located in Seattle](<https://data.seattle.gov/Transportation/Bike-Racks/bx5k-jjni>). Both sources were loaded into a MongoDB store, which was replicated on mLab.

The "algorithm" for determining bike rack need is pretty simple: the count of Yelp reviews as a proxy for how heavily trafficked a spot is, divided by the distance to the nearest bike rack.

The front code end lives [here](<https://github.com/jamesliudotcc/hackathon_spotdash>) and is deployed on [Heroku](<https://hackathon-spotdash.herokuapp.com/>).