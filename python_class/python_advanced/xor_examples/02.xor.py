# 바이너리 파일의 구조

signatures = {
    b'\xFF\xD8\xFF\xE0': 'JPEG 이미지',
    b'\x89PNG\r\n\x1A\n': 'PNG 이미지',
    b'GIF87a': 'GIF 이미지 (87a)',
    b'GIF89a': 'GIF 이미지 (89a)',
    b'%PDF': 'PDF 문서',
    b'PK\x03\x04': 'ZIP 아카이브'
}

def get_file_type(filename):
    try:
        # 파일의 처음 8바이트를 읽음
        with open(filename, 'rb') as file:
            header = file.read(8)
        
        # 각 시그니처와 비교
        for signature, file_type in signatures.items():
            if header.startswith(signature):
                return file_type
        
        return "알 수 없는 파일 형식"
        
    except Exception as e:
        return f"파일 검사 중 오류 발생: {e}"

# 예시
# print(get_file_type('example.jpg'))