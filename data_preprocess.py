import gzip


import os
import os.path as osp 

import cv2
import csv
from urllib import request
import asyncio
def read_csv(file_name):
    data_list = []
    with open(file_name, "r") as fp :
        datas = list(csv.reader(fp,delimiter="\t"))
        keys = datas[0]
        for data in datas[1:]:
            data_wrap = {}
            for key, data in zip(keys, data):
                data_wrap[key] = data
            data_list.append(data_wrap)
            if not data :
                break 

    return keys, data_list
    

async def load_img_from_url(url, save_pth):
    _, msg = request.urlretrieve(url, save_pth)
    print(save_pth)
    return msg


async def preprocess(*dir_names):
    """
        dir_names : list of (src, dest)
    """
    def url_and_name_filter(k):
        return  (k.get(keys[0]), k.get(keys[1]))
    


    for dir_name, dest_dir_name in dir_names:
        keys, data_list = read_csv(dir_name)
        print(keys)

        url_list = map(url_and_name_filter, data_list)
        # print(len(list(url_list)))
        if not osp.exists(dest_dir_name):
            os.makedirs(dest_dir_name)
        print("preprocess")
        fts = [asyncio.ensure_future(load_img_from_url(url, osp.join(dest_dir_name , str(i)+"_"+name + ".jpg"))) for i, (url, name) in enumerate( url_list) ]
        r = await asyncio.gather(fts)




if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(preprocess(("./data/kbvt_lfpw_v1_train.csv", "preprop_data/train"), ("./data/kbvt_lfpw_v1_test.csv","preprop_data/test")))
    loop.close()
    