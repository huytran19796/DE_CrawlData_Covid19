import re

def get_date(input_time): # Get information about (date, month, year)
    arr = input_time.split('T')
    if len(arr) == 2:
        detail_arr = arr[0].split('-')
        return int(detail_arr[2]), int(detail_arr[1]), int(detail_arr[0])
    else:
        return -1, -1, -1
        
def get_newCase(paragraph): # Get total new case covid-19 per date
    pattern = r'ghi nhận ([\d,.]+) ca nhiễm mới'
    match = re.search(pattern, paragraph)
    cases = 0
    if match:
        try:
            cases = int(match.group(1).replace(',', '').replace('.', ''))
        except:
            cases = 0
    return cases

def get_detail_newCase(paragraph): # Get new cases covid-19 per date by each locations in VietNam
    pattern = r'(\b[A-Za-z\s]+)\s\((\d+)\)'
    match = re.findall(pattern, no_accent_vietnamese(paragraph))
    result = []
    for detail in match:
        content = {}
        content['province'] = detail[0]
        content['case'] = int(detail[1])
        result.append(content)
    return result

def no_accent_vietnamese(s): # Remove all accent vietnamees in paragraph
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s