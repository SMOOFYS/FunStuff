
CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra
LIBS = -lGL -lGLU -lglut -lm
TARGET = main
SOURCES = main.cpp

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCES) $(LIBS)

main-debug: $(SOURCES)
	$(CXX) $(CXXFLAGS) -g -o main-debug $(SOURCES) $(LIBS)

clean:
	rm -f $(TARGET) main-debug

.PHONY: clean
