#include <iostream>
#include <vector>

using namespace std;

struct pathStruct {
    float fuel, distance = {};
};

static int tank = 50;
vector<pathStruct> info;

int func(int, int);


int main() {

    int numberOfStation;
    cin >> numberOfStation;

    for (int i = 0; i < numberOfStation - 1; i++) {
        char type;
        float distance;
        pathStruct asd = {};
        cin >> type >> distance;
        if (type == 'b') {
            asd.fuel = 5.8;
            asd.distance = distance / 100;
            info.push_back(asd);
        }
        else if (type == 'o') {
            asd.fuel = 7.2;
            asd.distance = distance / 100;
            info.push_back(asd);
        }
        else {
            asd.fuel = 8.6;
            asd.distance = distance / 100;
            info.push_back(asd);
        }
    }

    //for (int i = 0; i < info.size(); i++) {
    //    cout << info[i].fuel << endl;
    //    cout << info[i].distance << endl;}

    int start = -1, end = -1;
    while (start < 1 || end < 1) {
        cout << "Enter start and end points:";
        cin >> start >> end;
    }

    func(start, end);

    /*
    ########################################################################
    Query Part

    //int numberOfQueries;
    //cout << "Enter number of queries: " << endl; cin >> numberOfQueries;

    //struct query {
    //    int start, end;
    //};

    //vector<query> queryStore;

    //cout << "Enter start and end points: ";
    //for (int i = 0; i < numberOfQueries; i++) {
    //    cout << i + 1 << ". query" << endl;
    //    int start, end;
    //    cin >> start >> end;
    //    queryStore[i].start = start;
    //    queryStore[i].end = end;
    //}


    //for (int i = 0; i < numberOfQueries; i++) {
    //    func(queryStore[i].start, queryStore[i].end);
    //}
        ########################################################################
    */
}

int func(int x, int y) {
    int count = 0;
    if (x == y) {
        cout << 0 << endl;
        return 0;
    }
    else if (x > y) {
        cout << -1 << endl;
        return -1;
    }
    else {
        for (int i = x-1; i < y - 1; i++) {
            tank = tank - (info[i].fuel * info[i].distance);
            if (tank == 0 || tank < 0) {
                count++;
                tank = 50;
            }
        }
        cout << count << endl;
        return count;
    }
}
