class University:
    total_student_count = 0
    def __init__(self):
        self.school_name = "南华大学"
    def get_school_name(self):
        return self.school_name
    @staticmethod
    def add_student_count():
        University.total_student_count += 1
    @staticmethod
    def get_total_student_count():
        return University.total_student_count

class HengshanPiTeam:
    def __init__(self):
        self.team_name = "衡山π战队"
    def get_team_name(self):
        return self.team_name

class College(University):
    def __init__(self, college_name):
        super().__init__()
        self.college_name = college_name
        self.college_students = []
    def add_common_student(self, student_id, name):
        student_info = f"{student_id}|{name}|普通学生"
        self.college_students.append(student_info)
        University.add_student_count()
        print(f"已添加普通学生到{self.college_name}：学号：{student_id}，姓名：{name}")
    def add_team_student_to_college(self, student_id, name, group_name):
        student_info = f"{student_id}|{name}|战队-{group_name}"
        self.college_students.append(student_info)
        University.add_student_count()
    def show_all_students_in_college(self):
        print(f"===== {self.college_name} 所有学生（共{len(self.college_students)}人）=====")
        if not self.college_students:
            print("该学院暂无学生")
            return
        for idx, info in enumerate(self.college_students, 1):
            student_id, name, identity = info.split("|")
            print(f"{idx}. 学号：{student_id} | 姓名：{name} | 身份：{identity} | 所属学校：{self.get_school_name()}")
    def get_college_name(self):
        return self.college_name
    def get_college_member_count_in_group(self, group_name):
        target = f"战队-{group_name}"
        return sum(1 for info in self.college_students if info.split("|")[-1] == target)

class TeamGroup(HengshanPiTeam):
    def __init__(self, group_name):
        super().__init__()
        self.group_name = group_name
        self.group_members = []
        self.related_colleges = []
    def add_team_student(self, student_id, name, college):
        student_info = f"{student_id}|{name}|{college.get_college_name()}"
        self.group_members.append(student_info)
        if college not in self.related_colleges:
            self.related_colleges.append(college)
        college.add_team_student_to_college(student_id, name, self.group_name)
        print(f"已添加新生到{self.group_name}：学号：{student_id}，姓名：{name}，所属学院：{college.get_college_name()}")
    def delete_team_member(self, student_id):
        for idx, info in enumerate(self.group_members):
            if info.startswith(student_id):
                _, name, _ = info.split("|")
                del self.group_members[idx]
                print(f"已从{self.group_name}淘汰成员：学号：{student_id}，姓名：{name}（保留学院学籍）")
                return True
        return False
    def show_all_members_in_group(self):
        team_name = self.get_team_name()
        print(f"===== {team_name}-{self.group_name} 成员（共{len(self.group_members)}人）=====")
        if not self.group_members:
            print("该小组暂无成员")
            return
        for idx, info in enumerate(self.group_members, 1):
            student_id, name, college = info.split("|")
            print(f"{idx}. 学号：{student_id} | 姓名：{name} | 所属学院：{college} | 所属战队：{team_name}")
    def get_group_name(self):
        return self.group_name
    def get_group_total_count(self):
        return len(self.group_members)
    def __gt__(self, other_group):
        return len(self.group_members) > len(other_group.group_members)
    def __eq__(self, other_group):
        return len(self.group_members) == len(other_group.group_members)

class TeamFreshmanManager:
    def __init__(self):
        self.colleges = []
        self.team_groups = []
    def init_system(self):
        college_names = [
            "计算机学院", "电气工程学院", "数理学院", "机械工程学院",
            "核科学与技术学院", "语言文学学院", "土木工程学院"
        ]
        for name in college_names:
            self.colleges.append(College(name))
        group_names = ["视觉组", "机械组", "电控组", "宣传组"]
        for name in group_names:
            self.team_groups.append(TeamGroup(name))
        print("南华大学衡山π战队新生管理系统初始化完成！")
    def add_common_student(self, college_name, student_id, name):
        for college in self.colleges:
            if college.get_college_name() == college_name:
                college.add_common_student(student_id, name)
                return
        print(f"未找到{college_name}，添加失败！")
    def add_team_student(self, group_name, college_name, student_id, name):
        target_group = None
        target_college = None
        for group in self.team_groups:
            if group.get_group_name() == group_name:
                target_group = group
                break
        for college in self.colleges:
            if college.get_college_name() == college_name:
                target_college = college
                break
        if target_group and target_college:
            target_group.add_team_student(student_id, name, target_college)
        else:
            print("未找到目标小组或学院，添加失败！")
    def delete_team_member(self, group_name, student_id):
        for group in self.team_groups:
            if group.get_group_name() == group_name:
                if group.delete_team_member(student_id):
                    return True
                else:
                    print(f"未在{group_name}找到学号为{student_id}的成员，删除失败！")
                    return False
        print(f"未找到{group_name}，删除失败！")
        return False
    def show_college_students(self, college_name):
        for college in self.colleges:
            if college.get_college_name() == college_name:
                college.show_all_students_in_college()
                return
        print(f"未找到{college_name}，显示失败！")
    def show_group_members(self, group_name):
        for group in self.team_groups:
            if group.get_group_name() == group_name:
                group.show_all_members_in_group()
                return
        print(f"未找到{group_name}，显示失败！")
    def show_college_ratio_in_group(self, college_name, group_name):
        target_college = None
        target_group = None
        for college in self.colleges:
            if college.get_college_name() == college_name:
                target_college = college
                break
        for group in self.team_groups:
            if group.get_group_name() == group_name:
                target_group = group
                break
        if target_college and target_group:
            college_count = target_college.get_college_member_count_in_group(group_name)
            group_total = target_group.get_group_total_count()
            ratio = (college_count / group_total * 100) if group_total != 0 else 0.0
            print(f"===== {college_name} 在{group_name}中的占比情况 =====")
            print(f"1. {group_name} 总人数：{group_total}人")
            print(f"2. {college_name} 在该小组的人数：{college_count}人")
            print(f"3. 占比：{ratio:.2f}%")
        else:
            print("未找到目标学院或小组，统计失败！")
