import wget


def Download_wget_OS(url):#单个文件下载
    #判断url是否存在
    try:        
        url_opener = urllib2.urlopen(url)
    except:
        print ('open url error')
        return 'url error'
    #判断内容是否为空
    file_name = wget.filename_from_url(url)## 获取文件名 就是链接最后一串
    print('The size of '+file_name+' is '+url_opener.headers['Content-Length'])
    if not url_opener.headers['Content-Length']:
        print ('no content length')
        return 'no Content'
    
    #status_subprocess = subprocess.call('wget -c %s'  %(url),shell=True)
    name = 'wget '+url
    print(name)
    status_subprocess = os.system(name)
    #等同于在shell中直接运行命令
    
    if status_subprocess == 0:
        print ('[%s]:download complete!' % (file_name))
        return 'download complete'
    else:
        print ('[%s]:download failed !' % (file_name))
        return 'download failed'




url_Apollo16 = 'https://data.darts.isas.jaxa.jp/pub/apollo/ase/Apollo16/'

for i in range(22):
    url_file = url_Apollo16 + 'Shot\ {}_apollo_16.segy'.format(str(i))
    print(url_file)
    Download_wget_OS(url_file)

