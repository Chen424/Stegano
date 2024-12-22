from PIL import Image

def extract_data_from_png(image_path):
    """
    從 PNG 圖片中提取隱藏數據。
    :param image_path: 嵌入數據的圖片路徑
    :return: 提取出的數據
    """
    img = Image.open(image_path)
    pixels = list(img.getdata())
    binary_data = ""
    
    for pixel in pixels:
        for color in pixel[:3]:  # R, G, B 分量
            binary_data += str(color & 1)  # 提取 LSB
            
            # 檢查結束碼
            if binary_data.endswith("1111111111111110"):  # 結束符
                # 去掉結束符
                binary_data = binary_data[:-16]
                
                # 將二進位轉為字節
                byte_array = bytearray(
                    int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)
                )
                return byte_array
    raise ValueError("未找到有效的隱藏數據！")

# 提取數據示範
extracted_data = extract_data_from_png("output.png")
with open("extracted_malicious.bat", "wb") as f:
    f.write(extracted_data)
print("已提取並保存數據到 extracted_malicious.bat")
