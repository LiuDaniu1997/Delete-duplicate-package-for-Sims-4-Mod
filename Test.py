import os
from collections import Counter

all_file_full_path_list = []
all_file_name_list = []


def get_all_files(path):
    all_file_list = os.listdir(path)
    for file in all_file_list:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            get_all_files(file_path)
        elif os.path.isfile(file_path):
            all_file_full_path_list.append(file_path)
            all_file_name_list.append(file)
    return all_file_full_path_list, all_file_name_list


def test(path):
    path_list, file_list = get_all_files(path)
    b = dict(Counter(file_list))
    duplicate_list = [key for key, value in b.items() if value > 1]
    target_path = ''
    # Here you can define the document you want to check with
    target_item_list = os.listdir(target_path)
    to_delete_item = [x for x in duplicate_list if x in target_item_list]
    print('duplicate_list: ', len(duplicate_list))
    print('target_item_list: ', len(target_item_list))
    print(to_delete_item)
    for item in to_delete_item:
        to_delete_path = target_path + '/' + item
        os.remove(to_delete_path)



test() #Hier you can set the mod path for sims 4
