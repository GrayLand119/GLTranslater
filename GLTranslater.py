import sys
import uuid
import requests
import hashlib
import time
import os, io
import GLAnalysisRespond as gla
import shutil

# reload(sys)
# sys.setdefaultencoding('utf-8')

YOUDAO_URL = 'http://openapi.youdao.com/api'
APP_KEY = '5fd6c2bacd54b38f'
APP_SECRET = 'mNwKLRJudytga3k6RZZBZ0qx6j7vcwOR'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def translateWithSentence(sentence: str):
    if len(sentence) == 0:
        return ''

    data = {}
    data['from'] = 'EN'
    data['to'] = 'zh-CHS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(sentence) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = sentence
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    # print(response.content)
    return response.content



if __name__ == '__main__':
    curDir = os.getcwd() + "/"
    proccessedDir = curDir + "Proccessed/"
    translatedDir = curDir + "Transalted/"
    fileDir = curDir + "WaitToTranslate/"
    fileList = os.listdir(fileDir)
    print(fileList)

    # fileNameW = tName + "_t.txt"
    # fWrite = open(fileDir + fileNameW, 'w')
    for tFile in fileList:
        if tFile[-3:] != 'txt':
            continue
        filePath = fileDir + tFile
        sentences = gla.getSentencesWithFile(filePath)
        if len(sentences) == 0:
            continue

        fileShortName = tFile.rsplit('.', 1)[0]
        wFileFullname = fileShortName + "_processed.txt"
        wFilePath = fileDir + wFileFullname
        fWrite = open(wFilePath, 'wt')
        fWrite.seek(0)
        totalCount = len(sentences)
        print("Total sentences count is {0}".format(totalCount))
        testCount = 0
        for tSentence in sentences:
            print("Processing {0}/{1}".format(testCount, totalCount))
            res = translateWithSentence(tSentence)
            trans_s = gla.getTranslateWithResponse(res)
            testCount+=1
            fWrite.write(tSentence + '\n')
            fWrite.write(trans_s + '\n')
        fWrite.close()
        shutil.move(wFilePath, translatedDir + wFileFullname)
        shutil.move(filePath, proccessedDir + tFile)

