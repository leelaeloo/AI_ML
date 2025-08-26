import os
import shutil
import datetime
import zipfile
from pathlib import Path

# 특정 디렉토리를 -> 백업 디렉토리에 저장
def backup_directory(source_dir, backup_dir=None, backup_name=None):

    # 소스 디렉토리 경로 객체
    source_path = Path(source_dir)
    
    # 소스 디렉토리 존재 확인
    if not source_path.exists() or not source_path.is_dir():
        print(f"오류: 소스 디렉토리 '{source_dir}'가 존재하지 않습니다.")
        return False

    # 백업 디렉토리 설정 (지정되지 않은 경우 현재 디렉토리)
    if backup_dir is None:
        backup_dir = Path.cwd()
    else:
        backup_dir = Path(backup_dir)
        # 백업 디렉토리 생성
        backup_dir.mkdir(parents=True, exist_ok=True)           # parent=True -> 부모 디렉토리가 없으면 자동으로 생성
                                                                # exist_ok=True -> 디렉토리가 이미 존재하면 오류를 발생시키지 않음

    # 백업 파일 이름 설정
    if backup_name is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{source_path.name}_backup_{timestamp}.zip"
    
    # 백업 파일 전체 경로
    backup_path = backup_dir / backup_name

    try:
        # ZIP 파일 생성
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 소스 디렉토리의 모든 파일 추가
            for root, _, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)        # 전체 file_path를 가져옴
                    
                    # ZIP 파일 내 상대 경로 계산
                    arc_name = os.path.relpath(file_path, os.path.dirname(source_dir))
                    zipf.write(file_path, arc_name)
                    print(f"추가: {file_path}")
        
        print(f"\n백업 완료: {backup_path}")
        print(f"백업 크기: {backup_path.stat().st_size / (1024*1024):.2f} MB")
        return True
    
    except Exception as e:
        print(f"\n백업 중 오류 발생: {e}")
        return False
        
# 사용 예시
# backup_directory('new_location', 'backups')