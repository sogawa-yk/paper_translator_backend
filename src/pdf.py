import fitz
from urllib import request
import re
import glob
import time

def insert_space(obj_text, uri):
    text_list = []
    save_name = '/app/paper_translator_backend/tmp/'+str(uri.split('/')[-1])
    if not save_name in glob.glob('/app/paper_translator_backend/tmp/*'):
        try:
            request.urlretrieve(uri, save_name)
        except:
            return 'ERROR'

    doc = fitz.open(save_name)

    for page in range(len(doc)):
        text = doc[page].get_text()
        text = text.replace('\n', '')
        text = text.replace('.', '. ')
        text_list = text_list + re.split('[ ]+', text)

    no_space_text = '' # スペースなしの文
    check_points = [] # 単語の区切り場所を覚えておく
    idx = 0

    for text in text_list:
        no_space_text += text
        idx += len(text)
        check_points.append(idx)

    no_space_text = no_space_text.replace('ﬁ', '2')
    start_idx = no_space_text.find(obj_text)
    end_idx = start_idx + len(obj_text)

    res = []
    for idx, point in enumerate(check_points):
        if start_idx < point <= end_idx:
            res.append(text_list[idx])

    print('###CONVERTED###')
    print(' '.join(res))
    print('--------------')

    return ' '.join(res)
