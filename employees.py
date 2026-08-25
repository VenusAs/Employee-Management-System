import json
import os

# --- 数据文件配置 ---
DATA_FILE = "employees.json"

# --- 核心功能函数 ---

def load_data():
    """从 JSON 文件加载员工数据，如果文件不存在则返回空列表"""
    if not os.path.exists(DATA_FILE):
        return []                                     # 文件不存在 返回空列表
    try:
        with open(DATA_FILE,'r',encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError , IOError) as e:       # 解码失败或者IO出错时报错
        print(f"⚠数据加载失败：{e}")
        return []


def save_data(employees):
    """将员工列表保存到 JSON 文件"""
    with open(DATA_FILE,'w',encoding='utf-8') as f:
        json.dump(employees,f,ensure_ascii=False,indent=2)
    print("√数据已保存到文件。")
    
def show_menu():
    """显示命令行交互菜单"""
    print("\n" + "="*30)
    print("      员工信息管理系统")
    print("="*30)
    print("1. 增加员工")
    print("2. 删除员工")
    print("3. 修改员工")
    print("4. 查询员工")
    print("5. 显示全部员工")
    print("0. 退出并保存")
    print("="*30)

def add_employee(employees):
    """增加员工"""
    emp_id = input("请输入工号:").strip()
   # 检查工号是否存在
    for emp in employees:
        if emp_id == emp['id']:
            print("❌工号已存在，请重新输入")
            return
    name = input("请输入姓名：").strip()
    dept = input("请输入部门：").strip()
    employees.append({"id":emp_id,"姓名":name,"部门":dept})
    print("√员工添加成功")

def delete_employee(employees):
    """删除员工"""
    emp_id = input("请输入工号：").strip()
    for i,emp in enumerate(employees):
        if emp_id == emp['id']:
            employees.pop(i)
            print("√员工已删除")
            return
    print("❌员工未找到")

def update_employee(employees):
    """修改员工信息"""
    emp_id = input("请输入工号：").strip()
    for emp in employees:
        if emp_id == emp['id']:
            new_name = input(f"请输入新的姓名(原：{emp['姓名']})(直接回车则保留原姓名)：").strip()
            new_dept = input(f"请输入新的部门(原：{emp['部门']})(直接回车则保留原部门)：").strip()
            if new_name:    # 防止输入回车后把原来的值清空
                emp['姓名'] = new_name
            if new_dept:
                emp['部门'] = new_dept
            print("√员工信息已更新")
            return
    print("❌员工未找到")



def query_employee(employees):
    """查询员工"""
    emp_id = input("请输入工号：").strip()
    for emp in employees:
        if emp_id == emp['id']:
            print(f"\n工号:{emp['id']}\n姓名:{emp['姓名']}\n部门:{emp['部门']}")
            return
    print("❌员工未找到")

def show_all(employees):
    """显示全部员工"""
    if not employees:
        print("⚠当前没有员工数据")
        return
    print("\n当前员工列表:")
    print("-" * 40)
    print("工号\t姓名\t部门")
    print("-" * 40)
    for emp in employees:
        print(f"{emp['id']}\t{emp['姓名']}\t{emp['部门']}")
    print("-" * 40)

# --- 主程序入口 ---

def main():
    # 1. 加载数据
    employees = load_data()
    print(f"加载了{len(employees)}名员工数据")

    # 2. 主循环
    while True:
        show_menu()
        choice = input("请输入您的选择: ").strip()

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            delete_employee(employees)
        elif choice == '3':
            update_employee(employees)
        elif choice == '4':
            query_employee(employees)
        elif choice == '5':
            show_all(employees)
        elif choice == '0':
            save_data(employees)
            print("👋 已退出系统，再见！")
            break
        else:
            print("❌ 无效输入，请重新选择")

        # 每次操作后自动保存（确保数据不丢失）
        save_data(employees)

#运行
if __name__ == "__main__":
    main() 