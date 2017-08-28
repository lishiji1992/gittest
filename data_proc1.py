import os,sys
import re
dir = r'/home/liaozhaopo/下载/parsed'
list = os.listdir(dir)
list.sort()
#print(list)
file_pair = [(list[i],list[i+1]) for i in range(0,len(list),2)]
#print(file_pair)
print(len(file_pair))
html_pattern =  re.compile('(<[^>]+>)|(&nbsp)') #re.compile(r'(</?.*/?>){1}')

#split_pattern = re.compile(r'(##)|(@@)|(@#<br/>)')#|(\n)

def process_file_1(file):
    with open(dir+ '/'+ file,'r',errors='ignore',encoding='utf-8') as content:
        buf = content.read()
        paragraphs = []
        paragraphs.extend(re.split('(##)',buf))#buf.split(split_pattern)

        i=0
        for item in paragraphs:
            if item not in ['##','\n',None,'']:#,'$$'
                #paragraphs[i] = re.sub(html_pattern,'',str(item))
                paragraphs[i] = str(item)
                paragraphs[i] = paragraphs[i].strip()
                '''if re.match(r'^[\(（].*[）\)]$',paragraphs[i]) and i>0:
                    paragraphs[i-1] += paragraphs[i]
                    paragraphs[i] = ''
                    i -= 1'''
                i+=1
        paragraphs = paragraphs[:i]

        i=0
        for item in paragraphs:
            if item != '': # and item !='$$'and not re.match(r'^[,./;]',item):
                paragraphs[i] = item
                i += 1
        paragraphs = paragraphs[:i]
    return paragraphs

def process_file2(paragraph):
    after_split = []
    #for sentence in paragraph:
    sub_para = re.split('(@#<br/>)',paragraph)
    i=0
    for item in sub_para:
        if item not in ['##', '@@', '@#<br/>', '\n', None, '']:
            sub_para[i] = re.sub(html_pattern, '', str(item))
            sub_para[i] = re.sub(r'&#39;','\'',sub_para[i])
            sub_para[i] = sub_para[i].strip()
            i+=1
    sub_para = sub_para[:i]
    return sub_para

def process_article(article):
    after_split = []
    #for sentence in paragraph:
    sub_para = re.split('@@',article)

    i=0
    for item in sub_para:
        if item not in ['##', '@@', '@#<br/>', '\n', None, '']:
            #sub_para[i] = re.sub(html_pattern, '', str(item))
            sub_para[i] = sub_para[i].strip()
            i+=1
    sub_para = sub_para[:i]
    #after_split.append(sub_para)
    return sub_para
if __name__=='__main__':
    f_total = open('/home/liaozhaopo/下载/atman/align1.txt','w')
    for file1, file2 in file_pair:
        p1=process_file_1(file1)
        p2=process_file_1(file2)

        '''for i in zip(p1,p2):
            print(i[0],'\n',i[1],'\n')
            print('end1')'''

        paragraph_len = min(len(p1), len(p2))


        for i in range(paragraph_len):
            #print(p1[i],'\n',p2[i],'\n','end')
            article1 = process_article(p1[i])
            article2 = process_article(p2[i])
            article_len = min(len(article1),len(article2))
            for j in range(article_len):
                sens1 = process_file2(article1[j])
                sens2 = process_file2(article2[j])
                print(sens1,'\n',sens2,'\n',file1)
                sentence_len = min(len(sens1),len(sens2))
                for k in range(sentence_len):
                    f_total.write(sens1[k])
                    f_total.write('\t')
                    f_total.write(sens2[k])
                    f_total.write('\t')
                    #f_total.write(file1)
                    f_total.write('\n')
        #p1 = process_file2(p1)
        #p2 = process_file2(p2)


        '''minlen = min(len(p1), len(p2))
        p2p = []
        filename = '/home/liaozhaopo/下载/atman/' + file1 + '.txt'
        sentences = open(filename, 'w')
        for i in range(minlen):
            for item in zip(p1[i], p2[i]):
                p2p.append(item)
                sentences.write(item[0])
                sentences.write('\t')
                sentences.write(item[1])
                sentences.write('\n')
                f_total.write(item[0])
                f_total.write('\t')
                f_total.write(item[1])
                f_total.write('\t')
                f_total.write(file1)
                f_total.write('\n')

        sentences.close()'''


    f_total.close()