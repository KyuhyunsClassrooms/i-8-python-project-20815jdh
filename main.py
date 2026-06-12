# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20815 정덕현
# 프로젝트 주제: 용액 농도 계산기
def print_header(title):
    print("\n" + "=" * 40)
    print(f"{title:^38}")
    print("=" * 40)


def calculate_molarity(info_list):
    print_header("1. 몰농도 (M) 계산")
    
    data = []
   
    for item in info_list:
        user_input = input(item[0])
        data.append(item[1](user_input))

    solute_name, chemical_formula, formula_weight, solute_mass, water_volume_L = data

  
    solute_moles = solute_mass / formula_weight
    molarity = solute_moles / water_volume_L

    print("\n[계산 결과]")
    print(f"- 용액 정보: {solute_name} ({chemical_formula})")
    print(f"- 용질의 몰수: {solute_moles:.4f} mol")
    print(f"- 몰농도: {molarity:.4f} M")



def calculate_percent(info_list):
    print_header("2. 퍼센트 농도 (%) 계산")
    
    data = []
   
    for item in info_list:
        data.append(item[1](input(item[0])))

    solute_name, solute_mass, water_volume_L = data

  
    water_mass = water_volume_L * 1000
    solution_mass = solute_mass + water_mass
    percent_concentration = (solute_mass / solution_mass) * 100

    print("\n[계산 결과]")
    print(f"- 용액 정보: {solute_name} 수용액")
    print(f"- 용액의 총 질량: {solution_mass:.2f} g")
    print(f"- 퍼센트 농도: {percent_concentration:.2f} %")


def main():
    menu_list = [
        ["1", "몰농도(M) 계산하기"],
        ["2", "퍼센트 농도(%) 계산하기"],
        ["3", "프로그램 종료"]
    ]

    molarity_inputs = [
        ["▶ 용질의 이름 (예: 수산화나트륨): ", str],
        ["▶ 화학식 (예: NaOH): ", str],
        ["▶ 용질의 화학식량(g/mol): ", float],
        ["▶ 사용할 용질의 질량(g): ", float],
        ["▶ 물(용매)의 부피(L): ", float]
    ]

    percent_inputs = [
        ["▶ 용질의 이름 (예: 염화나트륨): ", str],
        ["▶ 용질의 질량(g): ", float],
        ["▶ 물(용매)의 부피(L): ", float]
    ]

    while True:
        print_header("용액 농도 계산 도우미 (용매: 물)")
        
        for menu in menu_list:
            print(f" {menu[0]}. {menu[1]}")
        print("-" * 40)
        
        choice = input("원하는 작업의 번호를 선택하세요: ").strip()

        if choice == menu_list[0][0]: # "1"
            
            calculate_molarity(molarity_inputs)
            input("\n계산이 완료되었습니다. 엔터를 누르면 시작 화면으로 돌아갑니다...")
            
        elif choice == menu_list[1][0]: # "2"
            
            calculate_percent(percent_inputs)
            input("\n계산이 완료되었습니다. 엔터를 누르면 시작 화면으로 돌아갑니다...")
            
        elif choice == menu_list[2][0]: # "3"
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("\n❌ 잘못된 번호입니다. 다시 선택해 주세요.")

if __name__ == "__main__":
    main()