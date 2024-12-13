import psutil
import requests
import time
from datetime import datetime
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 서버 설정
TARGET_IP = "192.168.0.167"  # 기본값, 실제 서버 IP로 변경 필요
API_URL = f"http://{TARGET_IP}:8000/cpu-monitor"

def get_cpu_usage():
    """CPU 사용량을 퍼센트로 반환"""
    return psutil.cpu_percent(interval=1)

def send_cpu_data(cpu_usage):
    """CPU 데이터를 서버로 전송"""
    data = {
        "timestamp": datetime.now().isoformat(),
        "cpu_usage": cpu_usage
    }
    
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            logging.info(f"데이터 전송 성공: CPU 사용량 {cpu_usage}%")
        else:
            logging.error(f"서버 에러: {response.status_code}")
    except requests.exceptions.ConnectionError:
        logging.error("서버 연결 실패. 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        logging.error(f"예상치 못한 에러 발생: {str(e)}")

def main():
    logging.info("CPU 모니터링 클라이언트 시작")
    
    while True:
        cpu_usage = get_cpu_usage()
        send_cpu_data(cpu_usage)
        time.sleep(5)  # 5초 간격으로 데이터 전송

if __name__ == "__main__":
    main()