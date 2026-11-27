/**
* Author: Aditya Shinde
* Date: 9/20/25
*/

#include "LocationFromFile.h"

/**
* @brief:  Inputs x and y locations from a file and populates a vector of
*		   Location objects
* @param:  Reference to a vector of Location objects
* @param:  string: input file name
* @return: None
*/
void inputData(vector<Location> &vectorLocations, string fileName){
  std::ifstream inFile; // input file stream
  string info;		  // input file stream name
  int x, y;			  // integers to store input locations read from the file

  // an example of try and catch exception handling -- more in Chapter 16
  try {
    // open the input file
    inFile.open(fileName);
    // if input file fails to open, throw an error (of type string)
    if (inFile.fail())
      throw string("File Open Error");

    // populate the Location vector until the end of input file
    while (!inFile.eof()) {
      getline(inFile, info); // get a line from the input file into the string info
                   // each line contains one location - "x y"
                   // x and y separate by a space

      std::istringstream istream(info); // input stream is the string info
                        // (i.e. the line read from file)
      istream >> x >> y;	// read two integers from the string info

      // Task 11: define an object p of class Location
      // Task 12: add the Location object p into the Location vector\

      Location p(x, y); // this is task 11 and defines the Location object
      vectorLocations.push_back(p); // this is task 12 and adds to the vector
    }
  }
  catch( string msg ) { // catch the error string thrown by the try block
    cout << msg;	  // print the error message
    exit(0);		  // bail out due to the error
  }
}
