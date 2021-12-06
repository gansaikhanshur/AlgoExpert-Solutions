#include <vector>
using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum) {
	//Loop through the main array
	for(int i = 0; i < array.size(); i++){
		//Second loop to step to the right direction
		for(int j = 0; j < array.size(); j++){
			//make sure that we're not adding the same index twice
			if(i != j){
				if(array[i] + array[j] == targetSum){
					return vector<int>{array[i], array[j]};
				}
			}
		}
	}
  return {};
}
