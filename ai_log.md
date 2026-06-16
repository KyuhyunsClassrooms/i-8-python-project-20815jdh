# Gemini 활용 기록

> 이번 수행평가에서는 학교 계정 Gemini 사용을 허용합니다.  
> 단, Gemini가 만든 코드를 이해하지 못한 채 그대로 제출하면 안 됩니다.  
> 실제 개인정보, 친구 이름, 성적, 전화번호, 주소 등은 절대 입력하지 않습니다.

---

## 1차 Gemini 활용

- 사용 날짜: 6/11
- 사용 목적: 화학과 관련된 주제 중에서 수행평가 조건(2차원 리스트, 함수 분리)에 맞는 주제 추천을 요청함.
- 내가 입력한 프롬프트: 

```text
화학과 관련된 주제를 설정하고 싶어. 조건에 맞는 주제를 추천해줘
```

- Gemini가 제안한 내용 요약: 원소 퀴즈, 시약 재고 관리, 용액의 농도 계산, 화학 반응식 계수 맞추기 등 5가지 주제를 제안함
- 내가 반영한 부분: 3번 주제인 '용액의 농도 계산 및 희석 도우미'를 최종 주제로 채택함.
- 내가 수정하거나 사용하지 않은 부분: 희석 도우미 부분은 사용하지 않았음.
- 반영 위치: project_plan.md
---

## 2차 Gemini 활용

- 사용 날짜: 6/12
- 사용 목적: 2차원 리스트의 행과 열의 의미를 파악하고, 미리 지정된 데이터가 아니라 사용자가 직접 입력하는 방식으로 변경하고 싶다고 요청함.
- 내가 입력한 프롬프트:

```text solute 리스트는 사용자가 직접 입력하는 방식으로 만들어줘

```

- Gemini가 제안한 내용 요약: 프로그램 시작 시 빈 리스트로 두고, `add_solute()` 함수를 만들어 사용자가 입력한 데이터를 `.append()`로 추가하는 구조를 제안함.
- 내가 반영한 부분: 제미나이의 코드를 부분 사용함.
- 내가 수정하거나 사용하지 않은 부분: Gemini의 제안을 참고하되, 입력 부분의 코드를 더 효율적으로 줄이기 위해 `[안내문구, 자료형]`을 쌍으로 묶은 독창적인 2차원 리스트 구조를 스스로 고안하여 코드에 반영함
- 반영 위치: main.py

---

## 3차 Gemini 활용

- 사용 날짜: 6/16
- 사용 목적: 직접 구현한 2차원 리스트 기반 동적 입력 코드를 검토받고 피드백을 요청함.
- 내가 입력한 프롬프트:

```text 
def print_header(title):
    print("\n" + "=" * 40)
    print(f"{title:^38}")
    print("=" * 40)

def calculate_molarity():
    print_header("1. 몰농도 (M) 계산")
    solute_name = input("▶ 용질의 이름 (예: 수산화나트륨): ")
    chemical_formula = input("▶ 화학식 (예: NaOH): ")
    formula_weight = float(input("▶ 용질의 화학식량(g/mol): "))
    solute_mass = float(input("▶ 사용할 용질의 질량(g): "))
    water_volume_L = float(input("▶ 물(용매)의 부피(L): "))

    solute_moles = solute_mass / formula_weight

    molarity = solute_moles / water_volume_L

    print("\n[계산 결과]")
    print(f"- 용액 정보: {solute_name} ({chemical_formula})")
    print(f"- 용질의 몰수: {solute_moles:.4f} mol")
    print(f"- 몰농도: {molarity:.4f} M")


def calculate_percent():
    print_header("2. 퍼센트 농도 (%) 계산")
    solute_name = input("▶ 용질의 이름 (예: 염화나트륨): ")
    solute_mass = float(input("▶ 용질의 질량(g): "))
    water_volume_L = float(input("▶ 물(용매)의 부피(L): "))


    water_mass = water_volume_L * 1000

    solution_mass = solute_mass + water_mass
 
    percent_concentration = (solute_mass / solution_mass) * 100

    print("\n[계산 결과]")
    print(f"- 용액 정보: {solute_name} 수용액")
    print(f"- 용액의 총 질량: {solution_mass:.2f} g (물: {water_mass:.2f}g)")
    print(f"- 퍼센트 농도: {percent_concentration:.2f} %")


def main():
    while True:
        print_header("용액 농도 계산 도우미 (용매: 물)")
        print(" 1. 몰농도(M) 계산하기")
        print(" 2. 퍼센트 농도(%) 계산하기")
        print(" 3. 프로그램 종료")
        print("-" * 40)
        
        choice = input("원하는 작업의 번호를 선택하세요: ").strip()

        if choice == '1':
            calculate_molarity()
            input("\n계산이 완료되었습니다. 엔터를 누르면 시작 화면으로 돌아갑니다...")
        elif choice == '2':
            calculate_percent()
            input("\n계산이 완료되었습니다. 엔터를 누르면 시작 화면으로 돌아갑니다...")
        elif choice == '3':
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("\n❌ 잘못된 번호입니다. 1, 2, 3 중에서 다시 선택해 주세요.")

if __name__ == "__main__":
    main()

내가 코드를 이렇게 짜봤는데 문제가 있을까?

```

- Gemini가 제안한 내용 요약: 코드의 창의성은 훌륭하나, 사용자가 물의 부피나 질량에 '0'을 입력했을 때 멈추는 에러(ZeroDivisionError) 가능성을 지적하며 예외 처리 추가를 제안함
- 내가 반영한 부분: 다른 수를 입력했을 때 오류가 나타나지 않도록 수정함.
- 내가 수정하거나 사용하지 않은 부분: x
- 반영 위치: main.py

---

## AI 활용 성찰

Gemini가 도움이 된 점: 잘못된 점을 빠르게 찾을 수 있고, 코드 인터뷰를 보다 편하게 준비할 수 있었음.


Gemini의 제안을 그대로 쓰지 않고 내가 판단하거나 수정한 점: 제미나이의 제안으로 만든 주제를 일부 수정하여 다시 주제를 설정함.


다음에 AI를 사용할 때 주의해야 할 점: AI를 사용하여 만든 코드를 검토하는 과정없이 복사, 붙여넣기 하는 행위를 주의해야한다.

