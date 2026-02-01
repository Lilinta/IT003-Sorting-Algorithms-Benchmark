#include <bits/stdc++.h>
using namespace std;

const int N = 1000000;
int A[N];
double B[N];

int main() {
    for (int num = 1; num <= 10; ++num) {
        cout << "Running test " << num << "\n";
        ifstream inp = ifstream(("testcases\\test" + to_string(num) + ".txt").c_str());
        if (num == 1 || (3 <= num && num <= 6)) {
            for (int i = 0; i < N; ++i) {
                inp >> B[i];
            }
            auto start_time = chrono::steady_clock::now();
            sort(B, B+N);
            auto end_time = chrono::steady_clock::now();
            chrono::duration<double> duration = end_time - start_time;
            cout << "Cppsort took " << duration.count() << " seconds\n";
        } else {
            for (int i = 0; i < N; ++i) {
                inp >> A[i];
            }
            auto start_time = chrono::steady_clock::now();
            sort(A, A+N);
            auto end_time = chrono::steady_clock::now();
            chrono::duration<double> duration = end_time - start_time;
            cout << "Cppsort took " << duration.count() << " seconds\n";
        }
    }
}
/*
Running test 1
Cppsort took 0.182447 seconds
Running test 2
Cppsort took 0.010141 seconds
Running test 3
Cppsort took 0.193314 seconds
Running test 4
Cppsort took 0.17626 seconds
Running test 5
Cppsort took 0.170007 seconds
Running test 6
Cppsort took 0.147433 seconds
Running test 7
Cppsort took 0.091037 seconds
Running test 8
Cppsort took 0.088141 seconds
Running test 9
Cppsort took 0.085416 seconds
Running test 10
Cppsort took 0.098085 seconds
*/
