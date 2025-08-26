# XOR 암호화를 사용한 파일 암호화/복호화

def xor_encrypt_decrypt(input_file, output_file, key):
    # XOR 연산을 사용해 파일을 암호화하거나 복호화
    # XOR 암호화는 같은 키로 두 번 수행하면 원래 데이터로 돌아오는 특징이 있음
    
    try:
        # 입력 파일 읽기
        with open(input_file, 'rb') as infile:
            data = infile.read()
        
        # XOR 연산으로 암호화/복호화
        key_bytes = key.encode() if isinstance(key, str) else bytes([key])
        # # 키가 문자열이면 바이트로 변환, 숫자면 바이트 리스트로 변환
        
        key_len = len(key_bytes)
        
        # 각 바이트에 XOR 연산 적용
        encrypted_data = bytearray(len(data))
        for i in range(len(data)):
            encrypted_data[i] = data[i] ^ key_bytes[i % key_len]        # data의 길이가 100, index 0 ~ 99
                                                                        # encrypted_data의 길이가 100
                                                                        # mykey123의 길이가 8, index 0 ~ 7
                                                                        # 주어진 index 90
                                                                        # 90 % 8 = 2
                                                                        # 91 & 8 = 3
        # 결과 파일에 쓰기
        with open(output_file, 'wb') as outfile:
            outfile.write(encrypted_data)
        
        print(f"파일 처리 완료: {input_file} -> {output_file}")
        return True
    
    except Exception as e:
        print(f"오류 발생: {e}")
        return False
        
# 암호화
xor_encrypt_decrypt('example.txt', 'secret.enc', 'mykey123')

# 복호화 (같은 키를 사용)
xor_encrypt_decrypt('secret.enc', 'decrypted.txt', 'mykey123')