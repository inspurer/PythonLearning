#include<iostream>
using namespace std;
int main(){
	int [] array = new int[]{9,5,2,8,6,4,1,3,7,0};
	bool flag = false;
	//冒泡排序
	for(int i = 0; i < 9; i++){
		for(int j = 0; j<9-i; j++){
			if(a[j]>a[j+1]){
				int temp = a[j];
				a[j+1] = a[j];
				a[j] = temp;
				flag = true;
			}
			if(!flag)
				break;
		}
	}
	/*这里是
	多行注释
	*/
	for(int i = 0; i < 9; i++){
		printf("%d",array[i]);
	}
}
		