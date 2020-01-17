/*
1/16/20
Palindrome Checker in C++
*/

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Palindrome Checker
// Given a string, return True or False whether the string is a palindrome or not
// Example: hannah = True , Dog = False

bool isPalindrome(string);

int main()
{
    // Test Cases
    string t1 = "hannah";
    string t2 = "dog";
    string t3 = "doddod";
    string t4 = "tot";
    cout << "TestCase 1: " << isPalindrome(t1) << endl; // Expected: 1
    cout << "TestCase 2: " << isPalindrome(t2) << endl; // Expected: 0
    cout << "TestCase 3: " << isPalindrome(t3) << endl; // Expected: 1
    cout << "TestCase 4: " << isPalindrome(t4) << endl; // Expected: 1
}

bool isPalindrome(string str)
{
    int start = 0;
    int end = str.length() - 1;

    transform(str.begin(), str.end(), str.begin(), ::tolower); // Makes the string lowercase

    while (start < end)
    {
        if (str[start] != str[end])
            return false;
        else
        {
            start++;
            end--;
        }
    }

    return true;
}