#include <iostream>
using namespace std;

int main() {
    int marks = 72;

    // if / else if / else
    if (marks >= 90)      cout << "A\n";
    else if (marks >= 75) cout << "B\n";
    else if (marks >= 60) cout << "C\n";
    else                   cout << "F\n";

    // Ternary: condition ? yes : no
    string res = (marks >= 60) ? "Pass" : "Fail";
    cout << res << "\n";

    // Nested if
    bool hasAttendance = true;
    if (marks >= 60) {
        if (hasAttendance) cout << "Eligible\n";
        else               cout << "Low attendance\n";
    }

    // Switch — matches exact int/char value
    int day = 2;
    switch (day) {
        case 1: cout << "Mon\n"; break;
        case 2: cout << "Tue\n"; break;
        case 3: cout << "Wed\n"; break;
        default: cout << "Other\n";
    }
    return 0;
}

#include <iostream>
using namespace std;

int main() {
    // for loop
    for (int i = 1; i <= 5; i++)
        cout << i << " ";
    cout << "\n";   // 1 2 3 4 5

    // while loop
    int n = 1;
    while (n <= 4) { cout << n << " "; n++; }
    cout << "\n";   // 1 2 3 4

    // do-while — runs at least once
    int k = 10;
    do {
        cout << k << " ";
        k++;
    } while (k < 10);  // false, but still ran once
    cout << "\n";

    // break — exit loop early
    for (int i = 0; i < 10; i++) {
        if (i == 4) break;
        cout << i << " ";
    }
    cout << "\n";   // 0 1 2 3

    // continue — skip this iteration
    for (int i = 0; i < 6; i++) {
        if (i % 2 == 0) continue;
        cout << i << " ";
    }
    cout << "\n";   // 1 3 5 (odd only)

    // nested loops — multiplication table
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++)
            cout << i*j << "\t";
        cout << "\n";
    }
    return 0;
}

#include <iostream>
using namespace std;

// Basic function
int add(int a, int b) { return a + b; }

// void — returns nothing
void printLine() { cout << "----------\n"; }

// Default parameter
void greet(string name, string msg = "Welcome") {
    cout << msg << ", " << name << "!\n";
}

// Pass by reference — modifies original
void square(int& x) { x = x * x; }

// Function overloading — same name, diff params
double area(double r)           { return 3.14 * r * r; }
double area(double l, double w) { return l * w; }

// Recursive function
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    cout << add(3, 7) << "\n";       // 10
    greet("Bob");                    // Welcome, Bob!
    greet("Alice", "Hello");        // Hello, Alice!
    int v = 5;
    square(v); cout << v << "\n";   // 25
    cout << area(4.0) << "\n";      // 50.24 (circle)
    cout << area(4.0,5.0) << "\n"; // 20 (rectangle)
    cout << factorial(6) << "\n";  // 720
    return 0;
}
