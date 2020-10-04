import os

os.chdir(os.path.join(os.getcwd(), 'files'))
content_list = []
class File:
    def __init__(self, file_name, number_str, str_list):
        self.file_name = file_name
        self.number_str = number_str
        self.str_list = str_list
quantity = 0
for root, dirs, files in os.walk(".", topdown = False):
   for name in files:
      with open(name, encoding='utf-8') as file:
          tmp = file.read()
          tmp_list = tmp.split('\n')
          if quantity < len(tmp_list):
              quantity = len(tmp_list)
          tmp_dict = {'file_name': name, 'string_digital': len(tmp_list), 'strings': tmp_list}
          content_list.append(tmp_dict)
i = 0
for item in content_list:
    if quantity > item['string_digital']:
        quantity = item['string_digital']
        if i > 0:
            content_list[i], content_list[i-1] = content_list[i-1], content_list[i]
    i += 1
for result_item in content_list:
    print(result_item['file_name'])
    print(result_item['string_digital'])
    for result_str in result_item['strings']:
        print(result_str)

