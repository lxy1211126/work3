#include "team.h"
#include <limits>

void showMenu() {
    cout << "1加2删3查4统计0退 输编号：";
}

int main() {
    V v1(1); E e2(2); M m3(3); P p4(4);
    int c; string s, n, g; 
    while (1) {
        showMenu(); cin >> c; cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (c) {
            case 1:
                cout << "组号1-4："; getline(cin,g);
                cout << "学号："; getline(cin,s);
                cout << "姓名："; getline(cin,n);
                
                switch(stoi(g)) {
                    case 1: v1.addMember(s,n); break;
                    case 2: e2.addMember(s,n); break;
                    case 3: m3.addMember(s,n); break;
                    case 4: p4.addMember(s,n); break;
                    default: cout << "组号错误" << endl;
                }
                break;
            case 2:
                cout << "组号1-4："; getline(cin,g);
                cout << "学号："; getline(cin,s);
                
                switch(stoi(g)) {
                    case 1: v1.deleteMember(s); break;
                    case 2: e2.deleteMember(s); break;
                    case 3: m3.deleteMember(s); break;
                    case 4: p4.deleteMember(s); break;
                    default: cout << "组号错误" << endl;
                }
                break;
            case 3:
                cout << "组号1-4："; getline(cin,g);
               
                switch(stoi(g)) {
                    case 1: v1.showGroupInfo(); break;
                    case 2: e2.showGroupInfo(); break;
                    case 3: m3.showGroupInfo(); break;
                    case 4: p4.showGroupInfo(); break;
                    default: cout << "组号错误" << endl;
                }
                break;
            case 4: cout << "总组数：" << University::getTotalGroups() << endl; break;
            case 0: cout << "结束" << endl; return 0;
            default: cout << "错" << endl;
        }
        cin.get();
    }
}
