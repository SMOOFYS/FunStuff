/**
* Author: Aditya Shinde
* Date: 9/20/25
 */

#ifndef __LOCATION_HEADER_H__
#define __LOCATION_HEADER_H__

#include <string>
using std::string;

class Location{
private: 
  int x; // location x
  int y; // location y

public:
  static int count; // reference count of Location objects, 
            // i.e. a running count of Location objects created so far
  // constructors
  Location();
  Location(int argx, int argy);
  // prototypes of member functions 
  double getDistance(Location other) const; // Further discussion on const in week6 lecture and lab
  Location create(int posX, int posY);
  Location create();
  string toString();
  // getter functions
  int getX() { return x; }
  int getY() { return y; }
};

#endif // __LOCATION_HEADER_H__