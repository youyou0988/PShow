all: main

main: main.cpp check.cpp algorithm.cpp run.cpp
	g++ -w main.cpp check.cpp algorithm.cpp -o main
	g++ -w run.cpp algorithm.cpp -o run

clean:
	rm -rf main
