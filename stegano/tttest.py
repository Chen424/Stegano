from PIL import Image

# 將檔案內容轉換為二進位串
def read_file_as_bits(file_path):
    """
    將檔案內容轉換為二進位字串表示。
    :param file_path: 要轉換的檔案路徑
    :return: 二進位字串
    """
    with open(file_path, "rb") as f:
        content = f.read()  # 以二進位模式讀取檔案
    return ''.join(format(byte, '08b') for byte in content)  # 每個字節轉為 8 位二進位

# 隱藏數據到圖片中
def hide_data_in_png(image_path, output_path, data_bits):
    """
    將數據以 LSB 隱寫術方式嵌入 PNG 圖片。
    :param image_path: 原始圖片路徑
    :param output_path: 輸出圖片路徑
    :param data_bits: 要嵌入的二進位數據
    """
    img = Image.open(image_path)
    img = img.convert("RGBA")  # 確保圖片有四個通道
    pixels = list(img.getdata())  # 取得所有像素值
    
    # 確認容量足夠
    total_pixels = len(pixels) * 3  # 每個像素有 R、G、B 三個 LSB 可用
    if len(data_bits) + 16 > total_pixels:  # +16 是為了結束碼
        raise ValueError("訊息太大，無法嵌入。")
    
    # 將結束碼 (例如 16 個 1) 加到尾端
    data_bits += "1111111111111110"
    
    new_pixels = []
    bit_index = 0
    
    for pixel in pixels:
        r, g, b, a = pixel  # 考慮 Alpha 通道
        if bit_index < len(data_bits):
            r = (r & ~1) | int(data_bits[bit_index])  # 修改 R 分量的 LSB
            bit_index += 1
        if bit_index < len(data_bits):
            g = (g & ~1) | int(data_bits[bit_index])  # 修改 G 分量的 LSB
            bit_index += 1
        if bit_index < len(data_bits):
            b = (b & ~1) | int(data_bits[bit_index])  # 修改 B 分量的 LSB
            bit_index += 1
        
        new_pixels.append((r, g, b, a))  # 添加修改後的像素，保留 Alpha 通道
    
    img.putdata(new_pixels)  # 將新像素寫回圖片
    img.save(output_path)
    print("已將惡意腳本嵌入圖片中：", output_path)

# 示範使用
if __name__ == "__main__":
    # 將檔案轉換為二進位
    data_bits = read_file_as_bits("malicious.bat")
    
    # 將二進位數據嵌入圖片
    hide_data_in_png("don.png", "output.png", data_bits)
