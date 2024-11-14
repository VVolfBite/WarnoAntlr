import streamlit as st

class Weapon:
    def __init__(self, name, ammo_type, damage, range):
        self.name = name
        self.ammo_type = ammo_type
        self.damage = damage
        self.range = range

    # 简略展示方法
    def display_summary(self):
        # 点击名称直接跳转，通过查询参数来传递名称
        link = f"[**Weapon:** {self.name} - {self.ammo_type}](?weapon={self.name})"
        st.markdown(link, unsafe_allow_html=True)

    # 详细展示方法
    def display_details(self):
        st.write(f"### {self.name} 详细信息")
        st.write(f"**弹药类型:** {self.ammo_type}")
        st.write(f"**伤害:** {self.damage}")
        st.write(f"**射程:** {self.range}")
        st.write("---")  # 分隔线

# 初始化武器对象字典
all_weapons = {
    "Cannon": Weapon("Cannon", "AP_23mm", damage=50, range=1000),
    "Missile": Weapon("Missile", "HE_35mm", damage=150, range=2000)
}

# Streamlit 主展示逻辑
def display_main():
    st.title("武器展示")
    
    # 读取查询参数
    query_params = st.query_params()
    selected_weapon_name = query_params.get("weapon", [None])[0]

    # 若未选中武器，则显示简略展示
    if not selected_weapon_name:
        for weapon in all_weapons.values():
            weapon.display_summary()
    else:
        # 若选中了武器，则显示详细展示
        weapon = all_weapons.get(selected_weapon_name)
        if weapon:
            weapon.display_details()
            # 返回到简略展示
            if st.button("返回"):
                st.query_params()

display_main()
