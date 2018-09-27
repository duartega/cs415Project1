#include <iostream>

using namespace std;
int global_count = 0;


int euclids_ago(int m, int n, int count, int done)
{
        int gcd;

        if (n == 0)
                return 0;
        else
        {
                gcd = m % n;

                count += 1;


                if (gcd == 0)
                {
                        if (done == 10) {
                                cout << "Count: " << count << endl;
                                global_count = count;
                        }
                        return n;
                }
                else
                {
                        if (done == 10)
                                euclids_ago(n, gcd, count, 10);
                        else
                                euclids_ago(n, gcd, count, 11);
                }
        }
}

float calc_avg(int sCount)
{
        int array[sCount];
        int rec = 11;
        for(int i=0; i < sCount; i++)
        {
                array[i] = euclids_ago(sCount, i, 0, rec);
                rec++;


        }
        float avg = 0.0;
        int total = 0;

        for (int j = 0; j < sCount; j++)
        {
                total +=array[j];
        }

        avg = (float)total / (float)sCount;

        return avg;

}

int consec_int_checking(int m, int n)
{
        int temp = 0;
        int temp2 = 0;
        int t = 0;
        if (n < m)
        {
                while (temp != temp2)
                {
                        t = n;
                        cout << "t = " << t << endl;
                        temp = n/t;
                        cout << "temp = " << temp << endl;
                        if (isdigit(temp))
                        {
                                cout << "This made it\n";
                                temp2 = m/t;
                        }
                        n -=1;
                }
        }

}

int main() {


        int count = 0;
        int eu_al_m = 0;
        int eu_al_n = 0;
        int out = 0;

        cout << "Please enter an integer for m: ";
        cin >> eu_al_m;
        cout << endl;
        cout << "Please enter an integer for n: ";
        cin >> eu_al_n;
        cout << endl;

        out = euclids_ago(eu_al_m, eu_al_n, count, 10);

        cout << "GCD: " << out << endl;

        float output2 = calc_avg(global_count);
        cout << "Average is: " << output2 << endl;

        return 0;
}
