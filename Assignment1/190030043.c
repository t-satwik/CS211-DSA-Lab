/* I have used gcc version 9.3.0 on ubuntu for compiling this code
   I have watched a youtube video on mergesort to understand how it works. */

#include <stdio.h>



void Merge(int left_arr[], int size_left, int right_arr[], int size_right, int main_arr[]);  //function declarations
void MergeSort(int main_arr[], int size_main);



int main(int argc, char *argv[]){
     	FILE *fileptr = fopen(argv[1], "r" );           //opening the input file using command line arguements
 
	if ( fileptr == NULL) {
	    printf("\nCould not open input file");     //returning if we couldnt open it
	}
    	
    	else{
    		int size_input=0;		     //this variable stores the total number of inputs in the file
    		int current_num=0;		 
    		int inp_arr[100000];		    //declaring the array with a large number of elements.
    		
    		while(fscanf(fileptr, "%d", &current_num) != EOF){    //while loop until we reach end of the file
    			inp_arr[size_input]=current_num;	    //storing the current_num in array
			size_input++;				   
    		}
    		
    		MergeSort(inp_arr, size_input);      //calling the MergeSort function
    		
    		FILE *writeptr = fopen("mergesort.txt", "w");	//opening the mergesort.txt file
    		if ( writeptr == NULL) {			
   		 	printf("\nCould not open write file");
		}    
    
    		else{					       //writing the sorted array elements into the mergesort file
    			for(int i=0; i<size_input; i++){
    				fprintf(writeptr, "%d\n", inp_arr[i]);
    			}
    			fclose(writeptr);			
    		}
    		fclose(fileptr);	
    	}
    	return 0;   
}



void Merge(int left_arr[], int size_left, int right_arr[], int size_right, int main_arr[]){ //defining the merge function with left_array, right_array, main-array, size 												    of left array, size of right array as parameters
    
	int l=0, r=0, a=0;				//declaring l, r, a which traverse through left, right and main arrays 
	
	while(l< size_left && r < size_right){		//traversing through left and right arrays 
	    
		if(left_arr[l] <= right_arr[r]){	//storing left array element if it is >= right array element
			main_arr[a] = left_arr[l];
			a++; l++;
		}
		
		else{					//storing right array element if it is > left array element
			main_arr[a]=right_arr[r];
			a++; r++;
		}
	}
	
	while(l<size_left){			 	//if we have used all right array elements, then storing the remaining left array elements into the main array
		main_arr[a] = left_arr[l];
		l++; a++;	
	}
	
	while(r<size_right){                             //if we have used all left array elements, then storing the remaining right array elements into the main array
		main_arr[a]=right_arr[r];
		a++; r++;
	}	
}

void MergeSort(int main_arr[], int size_main){
    
	if(size_main<2){				//declaring the recursion-end condition
		return; 
	}
	
	int mid = size_main/2;				//setting size of left and right arrays to be mid and size-mid
	int size_left=mid;
	int size_right=size_main-mid;
	
	int left_arr[size_left];
	int right_arr[size_right];
	
	for(int i=0; i<size_left; i++){			//creating left and right arrays.
		left_arr[i]=main_arr[i];
	}
	
	for(int i=0; i<size_right; i++){
		right_arr[i]=main_arr[i+mid];
	}
	
	MergeSort(left_arr, size_left);			//implementing mergesort on left and right arrays
	MergeSort(right_arr, size_right);
	Merge(left_arr, size_left, right_arr, size_right, main_arr);  //calling merge on left right and main arrays
}





