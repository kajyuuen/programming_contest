#include<iostream>
#include<string>
#include<algorithm>
#include<set>
#include<climits>
#include<cstdlib>
#include<map>
#include<math.h>
#include<utility>
#include<vector>
using namespace std ;
typedef long long ll;

// N K
// A_1, ..., A_N

int gcm(int a, int b) {
	int result = a;
	int k = 0;
	int n = b;
	do {
		k = result % n;
		result = n;
		n = k;
	} while(k != 0);
	return result;
}

int lcm(int a, int b) {
	int g;
	g = gcm(a, b);
	return a*b/g;
}

int lcm_n(vector<int> &numbers) {
	int l;
	l = numbers[0];
	for (int i = 1; i < numbers.size(); i++) {
		l = gcm(l, numbers[i]);
	}
	return l;
}

int main(){
  int N, K ;
  cin >> N;

  vector<int> v ;
  for(int i = 0; i!= N; ++i){
    int tmp ;
    cin >> tmp ;
    v.push_back(tmp) ;
  }

  cout << lcm_n(v) << endl;
}