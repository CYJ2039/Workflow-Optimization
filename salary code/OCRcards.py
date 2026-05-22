import cv2
import pytesseract
import re

# 告訴 Python 大腦在哪裡 (請確認這行路徑符合您的電腦)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ==========================================
# 關卡：全圖智慧掃描與抓取
# ==========================================
def smart_find_times(image_path):
    # 1. 讀取並轉黑白
    img = cv2.imread(image_path)
    if img is None:
        print("錯誤：找不到圖片，請確認 test_card.png 是否在同一個資料夾內！")
        return []
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    print("正在對整張圖片進行全圖掃描 (這可能需要幾秒鐘)...")
    text = pytesseract.image_to_string(thresh)
    
    # 2. 使用 Regex 雷達：抓出所有符合「00:00」格式的文字
    time_pattern = r'\d{2}:\d{2}'
    found_times = re.findall(time_pattern, text)
    
    return found_times

# ==========================================
# 🚀 總指揮官（主程式）
# ==========================================
if __name__ == "__main__":
    MY_IMAGE = "test_card.png"  # 您剛剛下載的測試圖
    
    print("【啟動智慧抓取模式】")
    times = smart_find_times(MY_IMAGE)
    
    if times:
        print(f"\n太神啦！電腦自己在整張圖片中找到了 {len(times)} 個時間：")
        print(times)
    else:
        print("\n沒有找到任何時間格式的文字。")