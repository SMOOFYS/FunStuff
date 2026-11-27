/**
* Author: Aditya Shinde
* Date: 9/20/25
*/

#ifndef __LOCATION_FROM_FILE_H__
#define __LOCATION_FROM_FILE_H__

#include <sstream>
#include <fstream>
#include <vector>
#include <iostream>
#include "LocationHeader.h"

using std::cout;
using std::vector;

// input locations from a file
void inputData(vector<Location> &vectorLocations, string fileName);

#endif // __LOCATION_FROM_FILE_H__