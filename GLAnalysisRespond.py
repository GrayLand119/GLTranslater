import binascii
import json
import io, os, sys


def getTranslateWithResponse(res: bytes):
    if res is None:
        return ""
    dic = json.loads(res.decode())
    translated = dic["translation"][0]
    return translated

def analysisTest():
    data = b'{"tSpeakUrl":"http://openapi.youdao.com/ttsapi?q=%E6%88%91%E5%8F%AA%E6%98%AF%E6%83%B3%E7%BB%99%E4%BD%A0%E4%BB%AC%E4%B8%80%E4%BA%9B%E5%AE%9E%E9%99%85%E7%9A%84%E7%89%A9%E7%90%86%E4%BD%93%E9%AA%8C%0A%E5%9C%A860%E5%B9%B4%E4%BB%A3%E5%92%8C70%E5%B9%B4%E4%BB%A3%E8%BF%9E%E6%8E%A5%E3%80%81%E9%80%9A%E4%BF%A1%E5%92%8C%E8%AE%A1%E7%AE%97%E3%80%82&langType=zh-CHS&sign=74A57EE9515F4ED92B882EB2A8A27965&salt=1566813256737&voice=4&format=mp3&appKey=5fd6c2bacd54b38f","query":"I just wanted to give you sort of a sense of the actual physical experience of\\nconnecting and communicating and computing in the 60s and the 70s.","translation":["\xe6\x88\x91\xe5\x8f\xaa\xe6\x98\xaf\xe6\x83\xb3\xe7\xbb\x99\xe4\xbd\xa0\xe4\xbb\xac\xe4\xb8\x80\xe4\xba\x9b\xe5\xae\x9e\xe9\x99\x85\xe7\x9a\x84\xe7\x89\xa9\xe7\x90\x86\xe4\xbd\x93\xe9\xaa\x8c\\n\xe5\x9c\xa860\xe5\xb9\xb4\xe4\xbb\xa3\xe5\x92\x8c70\xe5\xb9\xb4\xe4\xbb\xa3\xe8\xbf\x9e\xe6\x8e\xa5\xe3\x80\x81\xe9\x80\x9a\xe4\xbf\xa1\xe5\x92\x8c\xe8\xae\xa1\xe7\xae\x97\xe3\x80\x82"],"errorCode":"0","dict":{"url":"yddict://m.youdao.com/dict?le=eng&q=I+just+wanted+to+give+you+sort+of+a+sense+of+the+actual+physical+experience+of%0Aconnecting+and+communicating+and+computing+in+the+60s+and+the+70s."},"webdict":{"url":"http://m.youdao.com/dict?le=eng&q=I+just+wanted+to+give+you+sort+of+a+sense+of+the+actual+physical+experience+of%0Aconnecting+and+communicating+and+computing+in+the+60s+and+the+70s."},"l":"en2zh-CHS","speakUrl":"http://openapi.youdao.com/ttsapi?q=I+just+wanted+to+give+you+sort+of+a+sense+of+the+actual+physical+experience+of%0Aconnecting+and+communicating+and+computing+in+the+60s+and+the+70s.&langType=en&sign=3747F6AF3523B144DD45F9198A02D165&salt=1566813256737&voice=4&format=mp3&appKey=5fd6c2bacd54b38f"}'

    dic = json.loads(data.decode())
    translate = dic["translation"][0]
    print(translate)

def getSentencesWithFile(filePath: str):
    fileName = filePath.rsplit('/', 1)[1]
    tName = fileName.rsplit(".", 1)[0]
    fRead = open(filePath, 'r')

    buffer = ""
    sentences = []
    while 1:

        line = fRead.readline()
        isEOF = False
        if line == '':
            isEOF = True
        else:
            line = line.rsplit('...')[0]
            buffer += line
        if buffer[-1:] == '\n':
            buffer = buffer.replace('\n', ' ')
            continue
        ele: list = buffer.split(".")

        if len(buffer) == 0:
            break
        sentence = ""
        while len(sentence) < 60:
            if len(ele) > 0:
                sentence_c: str = ele[0]
                if sentence_c[-1:] == '\n':
                    sentenceP = sentence_c.replace("\n", " ")
                else:
                    sentenceP = sentence_c + '.'
                if sentenceP != '':
                    sentence += sentenceP
                ele.remove(sentence_c)
                buffer = ".".join(ele)
            else:
                break
        # print(sentence)
        sentences.append(sentence)
    fRead.close()
    return sentences

    # fWrite.close()


# curDir = os.getcwd() + "/"
# fileDir = curDir + "WaitToTranslate/"
# fileList = os.listdir(fileDir)
# print(fileList)
#
# filePath = fileDir + fileList[0]
#
# sentences = getSentencesWithFile(filePath)
# print(sentences)
