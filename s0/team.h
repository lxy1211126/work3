
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class University {
protected:
    string schoolName;
    static int totalGroups;
public:
    University();
    string getSchoolName() const;
    static int getTotalGroups();
    virtual void showSchoolInfo() const;
};

class HengshanPiTeam : public University {
protected:
    string teamName;
    vector<string> members;
private:
    int groupId;
public:
    HengshanPiTeam(int id);
    void addMember(string studentId, string name);
    bool deleteMember(string studentId);
    virtual void showGroupInfo() const;
    friend void getGroupPrivateId(const HengshanPiTeam& group);
    virtual ~HengshanPiTeam();
    int getGroupId() const;
};

class V : public HengshanPiTeam {
private:
    string mainTask;
    vector<string> skills;
public:
    V(int id);
    void addSkill(string skill);
    void showGroupInfo() const override;
};

class E : public HengshanPiTeam {
private:
    string mainTask;
    vector<string> hardware;
public:
    E(int id);
    void showGroupInfo() const override;
};

class M : public HengshanPiTeam {
private:
    string mainTask;
    vector<string> software;
public:
    M(int id);
    void showGroupInfo() const override;
};

class P : public HengshanPiTeam {
private:
    string mainTask;
    vector<string> tools;
public:
    P(int id);
    void showGroupInfo() const override;
};

void getGroupPrivateId(const HengshanPiTeam& group);
