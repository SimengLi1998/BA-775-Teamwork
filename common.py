# -*- coding: utf-8 -*-

import random
import numpy as np

# col_types = {}
features = ["State", "Month", "Hour", "Weekday", "Weather", "Visibility", "Preciputation", "Windspead", "Temperature",
            "Junction", "Crossing", "Traffic_Signal"]


# for col in one_hot_encoder_cols:
#     col_types[col] = "string"
# col_types["Temp"] = "float"


def open_file(filename, mode='r'):
    return open(filename, mode, encoding='utf-8', errors='ignore')


def write_file(filename, content):
    open_file(filename, mode="w").write(content)


def random_sample(filename):
    with open_file(filename) as f_:
        lines = f_.readlines()
    random.shuffle(lines)
    len_test = int(len(lines) * 0.2)
    lines_test = lines[0:len_test]
    lines_train = lines[len_test:]
    train_w = open_file("data/ft.train.txt", mode="w")
    test_w = open_file("data/ft.test.txt", mode="w")
    for i in lines_train:
        train_w.write(i)
    for j in lines_test:
        test_w.write(j)

# turn the features into id
def feature_to_id(cate_list):
    cates = list(set(cate_list))
    cate_to_id = dict(zip(cates, range(len(cates))))
    return cates, cate_to_id


