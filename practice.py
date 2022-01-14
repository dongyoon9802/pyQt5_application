name = "마린"
hp = 40
damage = 5

print(f"{name}유닛이 생성됨")
print(f"체력{hp},공격력 {damage}\n")

tank = "탱크"
tank_hp = 150
tank_damage = 35

print(f"{tank}유닛이 생성됨")
print(f"체력{tank_hp},공격력 {tank_damage}\n")

def attack(name, location, damage):
    print(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력{damage}]")

attack(name,"1시",damage)
attack(tank,"1시",tank_damage)
