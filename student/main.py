from implementation import University, HengshanPiTeam, College, TeamGroup, TeamFreshmanManager

def show_menu():
    print("          南华大学衡山π战队新生管理系统        ")
    print("1. 添加普通学生（学院）")
    print("2. 添加战队新生（小组+学院）")
    print("3. 淘汰战队成员（保留学院学籍）")
    print("4. 查看指定学院所有学生")
    print("5. 查看指定战队小组成员")
    print("6. 统计学院在小组的人数占比")
    print("7. 查看全校总学生数")
    print("8. 比较两个战队小组的人数")
    print("0. 退出系统")
    
    return input("请输入功能编号（0-8）：")

def main():
    manager = TeamFreshmanManager()
    manager.init_system()
    while True:
        choice = show_menu()
        if not choice.isdigit():
            print("\n输入错误！请输入0-8之间的数字编号～")
            input("按任意键返回菜单...")
            continue
        choice = int(choice)
        if choice == 0:
            print("\n感谢使用南华大学衡山π战队新生管理系统，再见！")
            break
        try:
            if choice == 1:
                college_name = input("请输入学院名称（如：计算机学院）：")
                student_id = input("请输入学生学号：")
                name = input("请输入学生姓名：")
                manager.add_common_student(college_name, student_id, name)
            elif choice == 2:
                group_name = input("请输入小组名称（视觉组/机械组/电控组/宣传组）：")
                college_name = input("请输入学生所属学院名称：")
                student_id = input("请输入学生学号：")
                name = input("请输入学生姓名：")
                manager.add_team_student(group_name, college_name, student_id, name)
            elif choice == 3:
                group_name = input("请输入小组名称：")
                student_id = input("请输入要淘汰成员的学号：")
                manager.delete_team_member(group_name, student_id)
            elif choice == 4:
                college_name = input("请输入学院名称：")
                manager.show_college_students(college_name)
            elif choice == 5:
                group_name = input("请输入小组名称：")
                manager.show_group_members(group_name)
            elif choice == 6:
                college_name = input("请输入学院名称：")
                group_name = input("请输入小组名称：")
                manager.show_college_ratio_in_group(college_name, group_name)
            elif choice == 7:
                total = University.get_total_student_count()
                print(f"南华大学当前总学生数：{total}人")
            elif choice == 8:
                group1_name = input("请输入第一个小组名称：")
                group2_name = input("请输入第二个小组名称：")
                group1 = None
                group2 = None
                for g in manager.team_groups:
                    if g.get_group_name() == group1_name:
                        group1 = g
                    if g.get_group_name() == group2_name:
                        group2 = g
                if group1 and group2:
                    count1 = group1.get_group_total_count()
                    count2 = group2.get_group_total_count()
                    print(f"\n{group1_name}人数：{count1}人")
                    print(f"{group2_name}人数：{count2}人")
                    if group1 > group2:
                        print(f"{group1_name}的人数多于{group2_name}")
                    elif group1 == group2:
                        print(f"{group1_name}和{group2_name}人数相同")
                    else:
                        print(f"{group1_name}的人数少于{group2_name}")
                else:
                    print("未找到目标小组，比较失败！")
            else:
                print("\n输入错误！请输入0-8之间的数字编号～")
        except Exception as e:
            print(f"\n操作出错：{str(e)}")
        input("\n按任意键返回菜单...")

if __name__ == "__main__":
    main()
