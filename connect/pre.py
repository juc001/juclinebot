

def prepare_record(text):
    text_list = text.split('\n')
    record_list = []
    for i in text_list[1:]:
        temp_list = i.split(' ')
        temp_id = temp_list[0]
        temp_name = temp_list[1]
        temp_gender = temp_list[2]
        temp_grade = temp_list[3]
        record = (temp_id, temp_name, temp_gender, temp_grade)
        record_list.append(record)
        
    return record_list