import pandas as pd
import os
import subprocess

filelist = []
#목표 path 적어넣기
for (path, dir, files) in os.walk(os.getcwd()):
    for filename in files:
        #끄트머리에 dup.ba 포함한 파일 경로 검색
        if '.qc.metrices.tx' == filename[-16:-1]:
            filelist.append('%s/%s' % (path, filename))

qcres = pd.DataFrame()
for target in filelist:
    temp = pd.read_csv(target, sep='\t', index_col=0).T
    index='%s' %(target.split('/')[-1].split('.')[0])
    temp.index = [index]
    qcres = qcres.append(temp)

qcres['Average depth'] = qcres['Average depth'].apply(lambda x: str(x).replace("x",""))
qcres = qcres[['Total bases (bam)',
       'Average depth', 
       'On target', 
       '% Covered (>100x pi)', 
       '% Covered (>200x pi)', 
       '% Covered (>300x pi)', 
       '% Covered (>500x pi)', 
       '% Covered (>1000x pi)',
       'Unique Pi / exon',
       'Median, Pi duplicates']]

qcres.to_csv('./qcres.csv')
