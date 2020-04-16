import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Base.classes.keys()

measurement = Base.classes.measurement
station = Base.classes.station

precipitation_data = [
{"date" :  "2017-08-21", "prcp" : "0.56"},
{"date" :  "2017-07-24", "prcp" : "0.84"},
{"date" :  "2017-06-15", "prcp" : "1.69"},
{"date" :  "2017-05-24", "prcp" : "2.17"},
{"date" :  "2017-04-28", "prcp" : "2.6"},
{"date" :  "2017-03-01", "prcp" : "2.4"},
{"date" :  "2017-02-07", "prcp" : "1.8"},
{"date" :  "2017-01-25", "prcp" : "2.64"},
{"date" :  "2016-12-03", "prcp" : "1.62"},
{"date" :  "2016-11-21", "prcp" : "2.87"},
{"date" :  "2016-10-30", "prcp" : "0.95"},
{"date" :  "2016-09-07", "prcp" : "1.35"},
{"date" :  "2016-08-24", "prcp" : "2.28"}

]

#################################################
# Flask Setup
#################################################


app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""

    print("Welcome to Surfs Up! API, choose a url to see climate details.")
          
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0/<start>/<end><br>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Precipitation Data for specified dates"""

    print("Here's chosen precipitation data for last year.")
    session = Session(engine)
    
    
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    """Station Names"""

    print("Observation Stations.")

    session = Session(engine)

    results_s = session.query(station.station).all()
    
    station_data = list(np.ravel(results_s))

    return jsonify(station_data)

@app.route("/api/v1.0/tobs")
def tobs():
    """temperature data"""

    print("Temperatures Observed from 2016-08-20 To 2017-08-23")

    session = Session(engine)

    results_t = session.query(measurement.tobs).filter(measurement.date >= "2016-08-20").filter(measurement.date <= "2017-08-23").all()
    tobs_data = list(np.ravel(results_t))

    return jsonify(tobs_data)


@app.route("/api/v1.0/<start>")
def start(start):
    """display the temp min, max and avg"""

    print("Temperature minimum, maximum and average for a received start date")
    session = Session(engine)

    results_start = session.query(measurement.date,func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)).filter(measurement.date >= start).all()

    data = []

    for date, min, max, avg in results_start:

        start_dict ={}

        start_dict["Date"]= date
        start_dict["min"] = min
        start_dict["max"] = max
        start_dict["avg"] = avg

        data.append(start_dict)
        
    return jsonify(data)


@app.route("/api/v1.0/<start>/<end>")
def end(start, end):
    """display the temp min, max and avg"""

    print("Temperature minimum, maximum and average for a received start and end date")
    session = Session(engine)

    results_end = session.query(measurement.date,func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end).all()

    data_2 = []

    for date, min, max, avg in results_end:

        end_dict ={}

        end_dict["Date"]= date
        end_dict["min"] = min
        end_dict["max"] = max
        end_dict["avg"] = avg

        data_2.append(end_dict)
        
    return jsonify(data_2)
                    
if __name__ == '__main__':
    app.run(debug=True)
