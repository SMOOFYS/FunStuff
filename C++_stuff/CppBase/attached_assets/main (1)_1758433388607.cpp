/**
* Lab 4: Demonstrate pointers to objects, pointers to arrays, vectors of objects,
*        reading a set of integers from a file, exception handling, 
*		 dynamic memory allocation and freeing that memory, 
*		 using the last element of a vector.
* Author: Aditya Shinde
* Date: 9/20/25
*/

#include <iostream>
#include <sstream>
#include <iomanip>
//#include"LocationHeader.h"
#include "LocationFromFile.h"

using namespace std;

// Note: for arrays, size should be given along with the array's memory address;
//       while for vectors, vector.size() is determined at run-time

/* @brief:  Fill and display an set of Locations
*  @param:  An array of pointers to Location objects
*  @param:	const int: number of location pointers in the array
*  @return: None
*/
void fillAndDisplay(Location * p[], const int numLocations) {
  /*
   * Task 1.	Create numLocations locations at (0,0), (1,1), etc. 
   *			using non-default Location constructors;
   * 		    and dynamically allocate memory for each location
   * Task 2:  Store pointers to each memory location of the newly created
   * 			Location objects in array p
   * Hint:	loop through the locations, create a Location pointer using keyword "new",
   *			assign the pointer to the i-th element of array p
  */

  for (int i = 0; i < numLocations; i++) {
    p[i] = new Location(i, i); // this is task 1
  }

  // task 2 already done since pointers will be auto stored in array p while its being made.

  // Task 3:	Print each location in the array using each Location object's toString() function

  for (int i = 0; i < numLocations; i++) {
    cout << p[i]->toString() << endl;
  }
}

/* @brief:  Free the allocated memory for the Location objects
*  @param:  An array of pointers to Location objects
*  @param:	int: number of location pointers in the array
*  @return: None
*/
void emptyArray(Location *p[], const int numLocations) {
  // Task 4: Free the dynamically allocated memory for all Location objects
  // Hint: loop through the locations and delete each element of array p
  // Caution: Do not use delete [], because the array is not of objects, but of pointers only

  for (int i = 0; i < numLocations; i++) {
    delete p[i]; // this is task 4 and this deletes the dynamically allocated memory for all location pointers, it doesnt use delete [] 
  }
}

/** main function
*  @params: None
*  @return: int
*/
int main() {
  int x, y; // locations x and y
  cout << "Enter two integers, separated by a space, for the 1st location: ";
  cin >> x >> y; // input two integers

  Location * pLocation1; // pointer to a location object
  // create a Location object using non-default constructor at (x,y)
  Location p1(x,y);
  pLocation1 = &p1; // assign the address of the object to the Location pointer
  // print the location (x,y)
  cout << "First location: " << pLocation1->toString() << endl;

  cout << "Enter two integers, separated by a space, for the 2nd location: ";
  cin >> x >> y; // input two integers
  // create a location object using non-default constructor at (x,y)
  // keyword "new" dynamically allocates memory and returns a pointer to that memory
  Location * pLocation2 = new Location(x, y); 
  // print the location (x,y)
  cout << "Second location: " << pLocation2->toString() << endl;

  // Task 5: Get the distance between first and second location and assign it to
  // 		   local double variable "distance"
  
  double distance = pLocation1->getDistance(*pLocation2); // this is task 5 and this gets the distance between the two locations.
  
  // display the distance
  cout << fixed << std::setw(10) << std::setprecision(2);
  cout << "The distance between " << pLocation1->toString() << " and "
    << pLocation2->toString() << " is: " 
    << distance << endl;
  cout << endl;
  // free the memory allocated for the dynamically allocated second location
  // Note: "delete" calls the object's destructors (if any)
  //       and also frees the memory allocated by "new"
  delete pLocation2;

  const int numLocations = 6; // students may change numLocations
  cout << "Next " << numLocations << " locations: " << endl;
  // create an array of 6 pointers to Location objects
  // the array will only hold the pointers, not the objects
  Location * LocationArray[numLocations];
  // fill and display the Locations pointed to by the pointers in the array
  fillAndDisplay(LocationArray, numLocations);
  cout << endl;
  // cleanup dynamically allocated memory for the Locations in the array
  emptyArray(LocationArray, numLocations);

  // input a vector of Location objects from a data file
  // Note: in Visual C++, the data file should be located in the directory
  //		 where the .vcxproj file is located
  vector<Location> vLocations;
  inputData(vLocations, "LocationData.txt");
  int count = vLocations.size();
  cout << "Found " << count << " locations from file" << endl;
  cout << "They are :" << endl;
  // print each location in vLocations using the location's toString() member function
  for (int i = 0; i < count; i++)
    cout << vLocations[i].toString() << endl;

  // Total locations
  // Note: The reference count should be updated for all Location objects, therefore, all Location objects
  //       should have the same value of static member variable "count", which represents the total
  //		 Location objects created so far. 
  //		 Ideally, in a Location object's destructor, the programmer should decrement the reference count.
  //		 However, in this lab, the task is to get this count from the last object in the vector.
  // Task 6: Assign the reference count (static member variable) of the last location in vLocations
  // 		   to local integer variable totalLocations
  // Hint:   vector::back() function returns a reference to the last element in a std::vector container

  int totalLocations = vLocations.back().count;
  
  // display the total number of locations
  cout << "\nTotal locations: " << totalLocations << endl;

  return 0;
}
