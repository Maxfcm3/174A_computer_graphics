# A generic makefile

CC=g++
CFLAGS=-c -std=c++0x  -Wall -Wno-unused-function
LDFLAGS=-lGLEW -lglut -lGL
SOURCES=$(wildcard *.cpp)
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=smash-opengl
ARCHIVE=103710865_linux

all: $(SOURCES) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean: 
	rm -rf $(OBJECTS) $(EXECUTABLE) $(ARCHIVE).zip

run: $(EXECUTABLE)
	./$(EXECUTABLE) $(ARGS)

dist: clean
	zip -r $(ARCHIVE) ./*

