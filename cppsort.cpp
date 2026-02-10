#include <bits/stdc++.h>
using namespace std;

const int N = 1000000;
int A[N];
double B[N];

int main() {
    cout << setprecision(3) << fixed;
    for (int num = 1; num <= 10; ++num) {
        cout << "Running test " << num << "\n";
        ifstream inp = ifstream(("testcases\\test" + to_string(num) + ".txt").c_str());
        if (1 <= num && num <= 5) {
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
Cppsort took 0.056 seconds
Running test 2
Cppsort took 0.049 seconds
Running test 3
Cppsort took 0.165 seconds
Running test 4
Cppsort took 0.233 seconds
Running test 5
Cppsort took 0.179 seconds
Running test 6
Cppsort took 0.105 seconds
Running test 7
Cppsort took 0.112 seconds
Running test 8
Cppsort took 0.112 seconds
Running test 9
Cppsort took 0.108 seconds
Running test 10
Cppsort took 0.120 seconds
*/
