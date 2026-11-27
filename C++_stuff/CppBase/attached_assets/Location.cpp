/**
* Author: Aditya Shinde
* Date: 9/20/25
*/

#include <cmath>	// for sqrt and pow
#include "LocationHeader.h"	// for the Location class

/**
* @brief:  Default constructor
* @param:  None
*/
Location::Location(){
  x = 0;	// initialize member variable x to 0
  y = 0;	// initialize member variable y to 0
  count++;	// increment static member variable count (reference count)
}

/**
* @brief:  Non-default constructor (with parameters)
* @param:  int: given x-location
* @param:  int: given y-location
*/
Location::Location(int otherX, int otherY) {
  x = otherX; // assign member variable x to the given x-location
  y = otherY; // assign member variable y to the given y-location
  count++;	  // increment static member variable count (reference count)
}

/**
 * @brief:  Calculates the Euclidean distance bettween two locations: 
 *		    sqrt((x1-x2)^2 + (y1-y2)^2)
 * @param:  Location object: a Location object (call by value)
 * @return: double: distance between the current location (x, y) and the given
 *			location in param 
 */
double Location::getDistance(Location other) const {
  // Task 7: Calculate the Euclidean distance between current object's (x,y)
  // 		 and the other object's (x,y) and return the distance

  double distance = sqrt(pow((x - other.x), 2) + pow((y - other.y), 2));
  return distance;
}

/**
* @brief:  Member function that creates a Location object using non-default
*		   constructor and returns it
* @param:  two integers x and y, indicating a given location
* @return: Location object
*/
Location Location::create(int posX, int posY) {
  // Task 8: create a Location object using the non-default constructor
  //       and return the object

  return Location(posX, posY);
}

/**
* @brief:  Member function that creates a Location object using the default
*		   constructor and returns it
* @param:  None
* @return: Location object
*/
Location Location::create() {
  // Task 9: create a Location object using the default constructor
  //       and return the object

  return Location();
}

/**
* @brief:  Member function that combines member variables x and y into
*		   a string of (x,y). Uses std::to_string() function to convert
*		   int to string. More string processing will be covered in Chapter 12.
* @param:  None
* @return: string: (x,y)
*/
string Location::toString() {
  return "(" + std::to_string(x) + "," + std::to_string(y) + ")";
}

/** 
 * @brief: Initialize static member variable count.
 *		   This is the reference count of Location object, i.e. this is a running
 *		   count of number of Location objects created so far.
 */
// Task 10: Initialize the static member variable count to zero.

int Location::count = 0; // this initalizes static count to 0
