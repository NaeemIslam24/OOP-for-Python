#include<stdio.h> 
 
int main()  
 
{ 
 
    int Balance[1000],customers; 
 
    int Total_Balance=0,Positive_Balance=0,Loan_Balance=0; 
 
    printf("Enter the customers number: "); 
 
    scanf("%d",&customers); 
 
    for(int i=0;i<customers;i++) { 
 
        scanf("%d",&Balance[i]); 
 
    } 
 
    for(int i=0;i<customers;i++) { 
 
        Total_Balance+=Balance[i]; 
 
        if(Balance[i]>0) { 
 
            Positive_Balance += Balance[i]; 
        } 
 
        else { 
 
            Loan_Balance +=-Balance[i]; 
 
        } 
 
    } 
 
    printf("%d\n",Total_Balance); 
 
    printf("%d\n",Positive_Balance); 
 
    printf("%d\n",Loan_Balance); 
 
    for(int i=0;i<customers;i++) { 
 
        if(Balance[i]<0) { 
 
            printf("%d\t",Balance[i]); 
 
        } 
 
    } 
 
    return 0; 
}