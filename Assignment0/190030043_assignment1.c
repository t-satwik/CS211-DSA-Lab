 #include <stdio.h>

 int main (int argc, char *argv[]) {
 int i=0;
 FILE *fileptr = fopen(argv[1], "r" );
 
 if ( fileptr == NULL) {
    printf("\nCould not open read file");
 }
  
 else {
    int i=0;
    int count=0;
    int min=32768;
    int max=-32768;
    long long int sum=0;
    while(fscanf(fileptr, "%d", &i) != EOF){
	count++;
	if(i < min){
		min =i;
		
	}
	if(i > max){
		max=i;		
	}
	sum += i;	
    }
    float avg = sum/((double)count);
    
    
    FILE *writeptr = fopen("output.txt", "w");
    if ( writeptr == NULL) {
    	printf("\nCould not open write file");
	}    
    
    else{
    fprintf(writeptr, "%d\n%d\n%d\n%lld\n%.2f\n", count, min, max, sum, avg);
    fclose(writeptr);
    }
    fclose(fileptr);
 }
 return 0;
 }
 

