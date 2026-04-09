# 통상임금 계산기
# 한국 노동법에 따른 통상임금 계산

def calculate_regular_wage(base_salary, bonus, work_days_per_month):
    """
    통상임금을 계산합니다.
    - base_salary: 월 기본급
    - bonus: 연간 상여금
    - work_days_per_month: 월 근무일수
    """
    monthly_bonus = bonus / 12
    total_monthly_wage = base_salary + monthly_bonus
    # 월 소정근로시간: 근무일수 * 8시간 (가정)
    monthly_work_hours = work_days_per_month * 8
    regular_wage_per_hour = total_monthly_wage / monthly_work_hours
    return regular_wage_per_hour

if __name__ == "__main__":
    print("통상임금 계산기")
    base_salary = float(input("월 기본급을 입력하세요: "))
    bonus = float(input("연간 상여금을 입력하세요: "))
    work_days = float(input("월 근무일수를 입력하세요: "))
    
    regular_wage = calculate_regular_wage(base_salary, bonus, work_days)
    print(f"시간당 통상임금: {regular_wage:.2f} 원")