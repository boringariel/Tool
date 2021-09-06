import os
import subprocess

filelist = []
#목표 path 적어넣기
for (path, dir, files) in os.walk("/media/dxome/Backup/Piseq_Backup/WGS_Project/Benign"):
    for filename in files:
        #끄트머리에 dup.ba 포함한 파일 경로 검색
        if 'dup.ba' == filename[-7:-1]:
            filelist.append('%s/%s' % (path, filename))

#report.txt 파일에 목표 파일 경로 저장
with open('report.txt', 'w') as f:
    for fl in filelist:
        f.write(fl+'\n')

#bedtools 이용한 intersect region 확인
#offtarget 폴더에 결과물 저장. 없을 경우 미리 생성해야 함
#끄트머리에 -v 옵션이 있는 경우 offtarget 대상으로 변경됨
for i in filelist:
    temp = subprocess.check_output(
        'bedtools intersect -a '+filelist[0]+' -b /media/src/target/ovary.ctdna.exon.bed >offtarget/'+filelist[0].split('/')[-1]+'_filtered.bam -v', shell=True)
