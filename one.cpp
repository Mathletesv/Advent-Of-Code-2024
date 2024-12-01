#include <bits/stdc++.h>
using ll = long long;
using namespace std;

void one() {
  ifstream fin("one.txt");
  vector<int> one, two;
  int a, b;
  while (!fin.eof()) {
    fin >> a >> b;
    one.push_back(a);
    two.push_back(b);
  }
  sort(one.begin(), one.end());
  sort(two.begin(), two.end());
  ll sum = 0;
  for (int i = 0; i < one.size(); i++) {
    sum += abs(one[i] - two[i]);
  }
  cout << sum << "\n";
}

void two() {
  ifstream fin("one.txt");
  vector<int> one;
  multiset<int> two;
  int a, b;
  while (!fin.eof()) {
    fin >> a >> b;
    one.push_back(a);
    two.insert(b);
  }
  ll sum = 0;
  for (int i = 0; i < one.size(); i++) {
    sum += one[i] * two.count(one[i]);
  }
  cout << sum << "\n";
}

int main() {
  one();
  two();
}