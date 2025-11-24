#include "team.h"

University::University() : schoolName("南华大学") {
    totalGroups++;
}

string University::getSchoolName() const {
    return schoolName;
}

int University::getTotalGroups() {
    return totalGroups;
}

void University::showSchoolInfo() const {
    cout << "所属学校 " << schoolName << endl;
}

HengshanPiTeam::HengshanPiTeam(int id) : teamName("衡山π战队"), groupId(id) {}

void HengshanPiTeam::addMember(string studentId, string name) {
    string memberInfo = studentId + name;
    members.push_back(memberInfo);
    cout << "已添加成员到" << teamName << "小组" << groupId << " " << name << "学号 " << studentId << endl;
}

bool HengshanPiTeam::deleteMember(string studentId) {
    for (auto it = members.begin(); it != members.end(); it++) {
        if (it->substr(0, studentId.size()) == studentId) {
            string name = it->substr(studentId.size());
            members.erase(it);
            cout << "已删除成员 " << name << "学号 " << studentId << endl;
            return true;
        }
    }
    cout << "未找到学号为" << studentId << "的成员" << endl;
    return false;
}

void HengshanPiTeam::showGroupInfo() const {
    showSchoolInfo();
    cout << "所属战队 " << teamName << endl;
    cout << "小组编号 " << groupId << endl;
    cout << "小组成员共" << members.size() << "人 " << endl;
    if (members.empty()) {
        cout << "暂无成员" << endl;
        return;
    }
    for (size_t i = 0; i < members.size(); i++) {
        string id = members[i].substr(0, 10);
        string name = members[i].substr(10);
        cout << i + 1 << " 学号 " << id << " 姓名 " << name << endl;
    }
}

HengshanPiTeam::~HengshanPiTeam() {
    cout << "衡山π战队小组" << groupId << "析构完成" << endl;
}

int HengshanPiTeam::getGroupId() const {
    return groupId;
}

V::V(int id) : HengshanPiTeam(id) {
    mainTask = "机器人视觉识别图像处理目标追踪";
    skills = {"OpenCV", "PythonC++", "图像处理算法", "深度学习"};
}

void V::addSkill(string skill) {
    skills.push_back(skill);
    cout << "V组新增技能 " << skill << endl;
}

void V::showGroupInfo() const {
    HengshanPiTeam::showGroupInfo();
    cout << "核心任务 " << mainTask << endl;
    cout << "所需技能 ";
    for (size_t i = 0; i < skills.size(); i++) {
        if (i > 0) cout << " ";
        cout << skills[i];
    }
    cout << endl;
}

E::E(int id) : HengshanPiTeam(id) {
    mainTask = "机器人电机控制电路设计程序调试";
    hardware = {"STM32单片机", "电机驱动器", "传感器", "电源模块"};
}

void E::showGroupInfo() const {
    HengshanPiTeam::showGroupInfo();
    cout << "核心任务 " << mainTask << endl;
    cout << "常用硬件 ";
    for (size_t i = 0; i < hardware.size(); i++) {
        if (i > 0) cout << " ";
        cout << hardware[i];
    }
    cout << endl;
}

M::M(int id) : HengshanPiTeam(id) {
    mainTask = "机器人结构设计零件建模装配调试";
    software = {"SolidWorks", "AutoCAD", "ANSYS", "3D打印"};
}

void M::showGroupInfo() const {
    HengshanPiTeam::showGroupInfo();
    cout << "核心任务 " << mainTask << endl;
    cout << "常用软件 ";
    for (size_t i = 0; i < software.size(); i++) {
        if (i > 0) cout << " ";
        cout << software[i];
    }
    cout << endl;
}

P::P(int id) : HengshanPiTeam(id) {
    mainTask = "战队活动策划文案撰写海报设计视频剪辑";
    tools = {"Photoshop", "Premiere", "Canva", "文案编辑"};
}

void P::showGroupInfo() const {
    HengshanPiTeam::showGroupInfo();
    cout << "核心任务 " << mainTask << endl;
    cout << "宣传工具 ";
    for (size_t i = 0; i < tools.size(); i++) {
        if (i > 0) cout << " ";
        cout << tools[i];
    }
    cout << endl;
}

void getGroupPrivateId(const HengshanPiTeam& group) {
    cout << "友元函数获取小组私有编号 " << group.groupId << endl;
}

int University::totalGroups = 0;
