/*
THE RIVER I
Difficulty: Easy
Link: https://www.codingame.com/training/easy/the-river-i-
*/

#include <iostream>
#include <string>

using namespace std;

 long long get_next(long long r)
{
    long long next_r = r;
    while (r > 0) {
        next_r += r % 10;
        r -= r % 10;
        r /= 10;
    }
    return next_r;
}

int main()
{
    long long r1;
    cin >> r1; cin.ignore();
    long long r2;
    cin >> r2; cin.ignore();

    while (r1 != r2) {
        if (r1 < r2) {
            r1 = get_next(r1);
        } else {
            r2 = get_next(r2);
        }
    }

    cout << r1 << endl;
}

