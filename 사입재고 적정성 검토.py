# 재무관리실 자동화 프로젝트 첫 번째 코드
import os

def check_file():
    target_file = "사입재고 검토절차 문서_SL_업데이트완료_수기조작금지.xlsx"
    
    if os.path.exists(target_file):
        print(f"✅ 확인 완료: '{target_file}' 파일이 저장소에 존재합니다.")
    else:
        print("❌ 경고: 엑셀 파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    check_file()
