import java.util.*;

class Program {
  public static int[] twoNumberSum(int[] array, int targetSum) {
	//#Loop through the main array
    for(int i = 0; i < array.length; i++){
			//#Second loop to step to the right direction
			for(int j = 0; j < array.length; j++){
				//#make sure that we're not adding the same index twice
				if(i != j){
					if(array[i] + array[j] == targetSum){
						return new int[] {array[i], array[j]};
					}
				}
			}
		}
    return new int[0];
  }
}
