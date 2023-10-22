"""
Software 1 - Python Module 8
Using relational databases
"""

import mysql.connector

# Task 1
def getAirportName(ICAO):
    cursor = connection.cursor()
    sql = ("select name, municipality from airport where ident = '"+ICAO+"'")
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# Main Program
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='M4riaDBeast',
    autocommit=True

)

uCode = input("Provide an ICAO code of the airport: ").upper()

print(f"{getAirportName(uCode)}")

# Task 2
def getOrderedAirports(country):
    cursor = connection.cursor()
    sql = "select type, count(type) from airport"
    sql += " where iso_country = '" + country + "' "
    sql += " group by type"
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(f"In this country there are {row[1]} {row[0]} airports")

    return


uCountry = input("Provide the area code of a country: ").upper()

getOrderedAirports(uCountry)

# Task 3
from geopy import distance
def airportCoordinates(ICAO):
    sql = " select latitude_deg, longitude_deg from airport, country "
    sql += " where airport.iso_country = country.iso_country and ident = '" + ICAO + "'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def airportDistance(initial, final):
    start = airportCoordinates(initial)
    end = airportCoordinates(final)
    start_coordinates = (start[0]['latitude_deg'], start[0]['longitude_deg'])
    end_coordinates = (end[0]['latitude_deg'], end[0]['longitude_deg'])

    return int(distance.distance(start_coordinates, end_coordinates).km)

airportOne = input("Enter the first ICAO code: ").upper()
airportTwo = input("Enter the second ICAO code: ").upper()
print(f"The distance between the two airports is {airportDistance(airportOne, airportTwo)} km")
