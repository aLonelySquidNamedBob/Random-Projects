#include<iostream>
#include<random>
#include<chrono>

int main () {
	auto start = std::chrono::high_resolution_clock::now();
	int num = 1000000;
	int list1[num] = {};
	int list2[num] = {};
	int x;
	float y;
	for (int i = 0; i < num; i++) {
		x = rand();
		list1[i] = x;
	}
	for (int i = 0; i < num; i++) {
		y = sqrt(list1[i]);
		list2[i] = y;
	}
	auto stop = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
	std::cout << duration.count() << std::endl;
}
