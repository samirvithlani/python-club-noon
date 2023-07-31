#include<iostream>
using namespace std;
#define MAX 1000

class Stack{

    public:
    int a[MAX];
    int top;
    Stack(){
        top = -1;
    }

    bool push(int x);
    int pop();
    int peek();
    bool isEmpty();

};

bool Stack :: push(int x){

    //-1 >= 999
    if(top>= (MAX-1)){
        cout<<"Stack Overflow";
        return false;
    }
    else{
        a[++top] = x;
        return true;
    }

}
int Stack ::pop(){

    if(top<0){
        cout<<"Stack Underflow";
        return 0;
    }
    else{
        int x = a[top--];
        return x;
    }
    
}

bool Stack :: isEmpty(){
    return (top<0);
}
int main(){

    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);


    while(!s.isEmpty()){
        cout<<s.pop()<<" ";
    }

}