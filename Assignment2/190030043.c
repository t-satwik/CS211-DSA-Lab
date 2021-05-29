#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node * root=NULL;				//Global variable named root, which has the pointer to the main root of the bst


struct Node{						//Declaring Node Data type with struct
    struct Node * left_ptr;
    int value;
    struct Node * right_ptr;
};

void insert(int new_num);				//declaring functions, they are defined after the main code
void inorder(struct Node * root, FILE *writeptr, int last_num);
void preorder(struct Node * root, FILE *writeptr, int first_num);
void postorder(struct Node * root, FILE *writeptr, int last_num);
struct Node * search(struct Node * root, int num);
int maximum(struct Node * root);
int minimum(struct Node * root);
void successor(struct Node * root, int num, FILE* writeptr);
void predecessor(struct Node * root, int num, FILE *writeptr);



int main(int argc, char *argv[]){

     	FILE *fileptr = fopen(argv[1], "r" );           //opening the input file using command line arguements
 
	if ( fileptr == NULL) {
	    printf("\nCould not open input file");     //printing error if we couldnt open it
	}
	else{
		FILE *writeptr = fopen("bst.txt", "w");	//opening bst.tst, where we print the output
    		
    		if ( writeptr == NULL) {		//printing error if we couldnt open it
   		 	printf("\nCould not open write file");
		}    
	
		else{
			char function[100];		//this function string stores the operation to be performed
			while(fscanf(fileptr, "%s", function) != EOF){	//reading the operation from inputfile
			
		        	if(strcmp(function, "insert")==0){	//insert operation
            				int num = 0;
            				fscanf(fileptr, "%d", &num);
            				insert(num);
            				fprintf(writeptr, "%d inserted\n", num);
        			}
        		
        		
        			if(strcmp(function, "inorder")==0){	//inorder operation
            				if(root!=NULL){
                				inorder(root, writeptr, maximum(root));
            				}
            				fprintf(writeptr, "\n");
        			}
        		
        		
        			if(strcmp(function, "postorder")==0){	//postorder operation
            				if(root!=NULL){
                				postorder(root, writeptr, root->value);
            				}
            				fprintf(writeptr, "\n");
        			}
        		
        		
        			if(strcmp(function, "preorder")==0){	//preorder operation
            				if(root!=NULL){
                				preorder(root, writeptr, root->value);
            				}
            				fprintf(writeptr, "\n");
        			}
        		
        		
        			if(strcmp(function, "search")==0){	//search operation
            				int num = 0;
            				fscanf(fileptr, "%d", &num);
            				if(search(root, num) == NULL){
                				fprintf(writeptr, "%d not found\n", num);
            				}
            				else{
                				fprintf(writeptr, "%d found\n", num);
            				}
        			}
        		
        		
        			if(strcmp(function, "maximum")==0){	//maximum operation
            				if(root!=NULL){
                				fprintf(writeptr, "%d", maximum(root));
            				}
            				fprintf(writeptr, "\n");
        			}
        
        
        			if(strcmp(function, "minimum")==0){	//minimum operation
            				if(root!=NULL){
                				fprintf(writeptr, "%d", minimum(root));
            				}
            				fprintf(writeptr, "\n");
        			}
        		
        			if(strcmp(function, "successor")==0){	//successor operation
            				int num = 0;
            				fscanf(fileptr, "%d", &num);
            				successor(root, num, writeptr);
        			}
        
        			if(strcmp(function, "predecessor")==0){	//predecessor operation
            				int num = 0;
            				fscanf(fileptr, "%d", &num);
            				predecessor(root, num, writeptr);
        			}
        			
        		}
        		fclose(writeptr);	
        	}
        	fclose(fileptr);
	}	
	return 0;
}

void insert(int new_num){
    struct Node * temp;
    temp = (struct Node *) malloc(sizeof(struct Node));	//creating a new node with malloc and storing in temp
    temp->value=new_num;
    temp->left_ptr=NULL;
    temp->right_ptr=NULL;
    
    struct Node * parent;
    parent=root;
    
    if(root==NULL){	//if bst is empty, then we store it in root
        root=temp;
    }
    else{
        struct Node * current=root;
        while(current!=NULL){	//traversing the bst, using parent pointer
            parent=current;	
            if(temp->value < current->value){
                current=current->left_ptr;
            }
            else{
                current=current->right_ptr;
            }
        }
        if(temp->value < parent->value){	//compare with parent pointer and attach at left or right accordingly
            parent->left_ptr=temp;
        }
        else{
            parent->right_ptr=temp;
        }
    }
}

void inorder(struct Node * root, FILE *writeptr, int last_num){	//inorder traversing
    if(root->left_ptr!=NULL){
        inorder(root->left_ptr, writeptr, last_num);		//left recursion
    }
    
    if(root->value == last_num){				//printing the root->value
    	fprintf(writeptr, "%d", root->value);
    }
    else{
    	fprintf(writeptr, "%d ", root->value);
    }
    
    if(root->right_ptr!=NULL){					//right recursion
        inorder(root->right_ptr, writeptr, last_num);
    }
}

void preorder(struct Node * root, FILE *writeptr, int first_num){ //preorder traversing

    if(root->value == first_num){				//printing the root->value
    	fprintf(writeptr, "%d", root->value);
    }
    else{
    	fprintf(writeptr, " %d", root->value);
    }
    
    if(root->left_ptr!=NULL){					//left recursion
        preorder(root->left_ptr, writeptr, first_num);
    }
    if(root->right_ptr!=NULL){					//right recursion
        preorder(root->right_ptr, writeptr, first_num);
    }
}

void postorder(struct Node * root, FILE *writeptr, int last_num){ //postorder traversing

    if(root->left_ptr!=NULL){					//left recursion
        postorder(root->left_ptr, writeptr, last_num);
    }
    if(root->right_ptr!=NULL){					//right recursion
        postorder(root->right_ptr, writeptr, last_num);
    }
    if(root->value == last_num){				//printing the root->value
    	fprintf(writeptr, "%d", root->value);
    }
    else{
    	fprintf(writeptr, "%d ", root->value);
    }
}
	
struct Node * search(struct Node * root, int num){		//search 
    struct Node * null_ptr=NULL;
    
    if(root==NULL){						//if empty tree, then return null_ptr
	return null_ptr;	
    }
    else{							//if the num is in root, then return
    	if(root->value==num){
        	return root;
    	}
    
    	if(num > root->value){					//searching in left tree or right trees, by comparing left and right pointer's values with num
        	if(root->right_ptr!=NULL){
        	   return search(root->right_ptr, num);
        	}
        
        	else{						//if we dont find then return null_ptr
        	    return null_ptr;
        	}
    	}
    
    
    	if(num < root->value){				
        	if(root->left_ptr!=NULL){
        	    return search(root->left_ptr, num);
        	}
        	else{
        	    return null_ptr;
        	}
    	}
    }
}

int maximum(struct Node * root){	//maximum
    if(root->right_ptr!=NULL){		//traverse right ptr until we reach a leaf
        maximum(root->right_ptr);	
    }
    else{
        return root->value;		//then returning the leaf value
    }
}

int minimum(struct Node * root){	//minimum
    if(root->left_ptr!=NULL){		//traverse left ptr until we reach a leaf
        minimum(root->left_ptr);
    }
    else{	
        return root->value;		//then returning the leaf value
    }
}

void successor(struct Node * root, int num, FILE* writeptr){	//successor
    struct Node * num_ptr = search(root, num);			//searching for the num to find its pointer
    if(num_ptr==NULL){						//is nullptr is sreturned then num doesnot exist in the tree
        fprintf(writeptr, "%d does not exist\n", num);
        return;
    }
    if(num==maximum(root)){					//is num is maximum then successor does not exist
       fprintf(writeptr, "successor of %d does not exist\n", num);
       return;
    }
    else{
        if(num_ptr->right_ptr != NULL){				//if right pointer exists, then getting the minimum in the right subtree
            fprintf(writeptr, "%d\n", minimum(num_ptr->right_ptr));
        }
        
        else{
            struct Node * succ = NULL;				//if rightpointer doesnt exist, we traverse from root until we get the parent of the num ptr.
            while(root != NULL){				
                if(num_ptr->value < root->value){			
                    succ=root;
                    root=root->left_ptr;
                }
                else if(num_ptr->value > root->value){
                    root=root->right_ptr;
                }
                else{
                    break;
                }
            }
            fprintf(writeptr, "%d\n", succ->value);		//printing the successor value
        }
    }
}

void predecessor(struct Node * root, int num, FILE *writeptr){
    struct Node * num_ptr = search(root, num);			//searching for the num to find its pointer
    if(num_ptr==NULL){						//is nullptr is sreturned then num doesnot exist in the tree
        fprintf(writeptr,"%d does not exist\n", num);
        return;
    }
    if(num==minimum(root)){					//is num is minimum then successor does not exist
        fprintf(writeptr, "predecessor of %d does not exist\n", num);
        return;
    }
    else{
        if(num_ptr->left_ptr != NULL){				//if left pointer exists, then getting the maximum in the left subtree
            fprintf(writeptr, "%d\n", maximum(num_ptr->left_ptr));
        }
        else{							//if leftpointer doesnt exist, we traverse from root until we get the parent of the num ptr.
            struct Node * pre = NULL;
            while(root != NULL){
                if(num_ptr->value > root->value){
                    pre=root;
                    root=root->right_ptr;
                }
                else if(num_ptr->value < root->value){
                    root=root->left_ptr;
                }
                else{
                    break;
                }
            }
            fprintf(writeptr, "%d\n", pre->value);		//printing the predeccessor value
        }
    }
}
































