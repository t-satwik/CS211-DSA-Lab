/* 
I have seen a youtube video to learn more about stacks and its implementation,
to solve the TOH part, I have referred some slides given in CS201 Course
*/

#include <stdio.h>
#include <stdlib.h>

struct Stack{                       //New structure Stack,
    char name;                      //Name of the stack
    int top;                        //top which stores the index of the topmost part of stack, initialized to -1, if stack is empty
    int size;                       //size of the array required.
    int *array;                     //pointer to the array
};

struct Stack * create_stack(char name, int size); //prototypes of all the functions defined later
int stack_overflow(struct Stack * stack);
int stack_underflow(struct Stack * stack);
void push(struct Stack * stack, int num, FILE * write_ptr);
void pop(struct Stack * stack, FILE * write_ptr);
void print(struct Stack * stack);
void transfer(struct Stack * stack_A, struct Stack * stack_C, FILE * write_ptr);
void toh(struct Stack * stack_A, struct Stack * stack_C, struct Stack * stack_B, int n, FILE * write_ptr);


int main(int argc, char *argv[]){
    int n=atoi(argv[1]);                            //atoi functon converts string arguements into int
    FILE * write_ptr= fopen("toh.txt", "w");        //write_ptr to the file

    if ( write_ptr == NULL) {                       //if file cant be opened
    	printf("\nCould not open write file");
	}    
    else{
        struct Stack *stack_A=create_stack('A', n);     //declaring and creating 3 stacks
        struct Stack *stack_B=create_stack('B', n);
        struct Stack *stack_C=create_stack('C', n);
        
        for(int i=n; i>=1; i--){                        //pushing teh n diskd into stack A
            push(stack_A, i, write_ptr);
        }

        toh(stack_A, stack_C, stack_B, n, write_ptr);      //toh function, which solves the problem.
        //  print(stack_A);
        //  print(stack_B);
        //  print(stack_C);
    }
    
    return 0;
}


struct Stack * create_stack(char name, int size){           //creates and initializes a stack
    struct Stack * new_stack=(struct Stack *)malloc(size*sizeof(struct Stack));
    new_stack->name=name;
    new_stack->top=-1;
    new_stack->size=size;
    new_stack->array = (int *)malloc(new_stack->size*sizeof(int));
    return new_stack;
}

int stack_overflow(struct Stack * stack){               //checks for overflow condition
    if(stack->top==(stack->size)-1){
        return 1;
    }
    else{
        return 0;
    }
}

int stack_underflow(struct Stack * stack){              //checks for underflow condition
    if(stack->top==-1){
        return 1;
    }
    else{
        return 0;
    }
}

void push(struct Stack * stack, int num, FILE * write_ptr){  //push function for a stack
    if(stack_overflow(stack)){                               //if overflow is true then print error and return
        fprintf(write_ptr, "Stack %c is full and %d cannot be inserted\n", stack->name, num);
        return;
    }
    else{                                                   //else, increment top and put the value into in top index
        stack->top++;
        stack->array[stack->top]=num;
        fprintf(write_ptr, "Push disk %d to Stack %c\n", num, stack->name);
        return;
    }
}

void pop(struct Stack * stack, FILE * write_ptr){           //pop operation
    if(stack_underflow(stack)){                             //is underflow is true, print error and return            
        fprintf(write_ptr, "Stack %c is empty hence pop operation failed\n", stack->name);
    }    
    else{                                                   //else change the value in top  index and decrement top
        int num=stack->array[stack->top];
        stack->array[stack->top]=0;
        stack->top--;
        fprintf(write_ptr,"Pop disk %d from Stack %c\n", num, stack->name);
    }
}

void print(struct Stack * stack){                          //This prints the stacks when called.
    for(int i=0; i<=stack->top; i++){
        printf("%d ", stack->array[i]);
    }
    printf("\n");
    return;
}

void transfer(struct Stack * stack_A, struct Stack * stack_C, FILE * write_ptr){ //this function pops the value from one stack and pushes it into other
    int num=stack_A->array[stack_A->top];
    pop(stack_A, write_ptr);
    push(stack_C, num, write_ptr);
    return;
}

/*
I have used recursion to solve the toh problem,
That is first we place the top n-1 disks of stack_A into stack_B,(toh(A, B, C, n-1))
then we transfer the nth disk from stack_A to stack_C
then we place the n-1 disks from stack_b to stack_C, using stack_A as  auxilary(toh(B, C, A, n-1)).
the recursion end condition would be when there is only one disk, then we simply transfer it from one stack to the other.  
*/
void toh(struct Stack * stack_A, struct Stack * stack_C, struct Stack * stack_B, int n, FILE * write_ptr){
    if(n==1){
        transfer(stack_A, stack_C, write_ptr);
        return;
    }
    toh(stack_A, stack_B, stack_C, n-1, write_ptr);
    
    transfer(stack_A, stack_C, write_ptr);
    
    toh(stack_B, stack_C, stack_A, n-1, write_ptr);
}


