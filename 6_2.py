import zipfile
import os
import shutil
import datetime
import click
"""
лучше использовать в одной папке с файлом, и следить чтобы там не было папки temp_archive
"""
@click.command()
@click.option("-n","--new_arc",required=True)
@click.option("-th","--third_fl",required=True)
def main(new_arc,third_fl):

    new_arc_name = new_arc
    filename_3 = third_fl
    if not (new_arc_name.endswith('.zip')):
        new_arc_name += ".zip"
    if not (filename_3.endswith('.txt')):
        filename_3 += '.txt'
    filename_3 = "./temp_archive/"+filename_3
    #print(filename_3)
    archive_name = 'sample.zip'
    FIO = 'Суденко Данила Романович'
    group = 'ИБI-2б'
    with zipfile.ZipFile(archive_name,'r') as z:
        if os.path.exists('./temp_archive'):
            shutil.rmtree('temp_archive')
        os.mkdir('temp_archive')
        containment= z.namelist()
        z.extractall('./temp_archive')
    
        filename_1 = './temp_archive/01.txt'
        with open(filename_1,'w') as file1:
            file1.write('')
        filename_2 = './temp_archive/02.txt'
        with open(filename_2, 'r', encoding='cp1251') as file2:
            file2_inners = file2.readlines()
        file2_symb= (lambda ll: [el for lst in ll for el in lst])([list(x) for x in list(file2_inners)])
        while '\n' in file2_symb:
            file2_symb.remove('\n')
        while ' ' in file2_symb:
            file2_symb.remove(' ')
        file2len = len(file2_symb)
        for i,item in enumerate(containment):
            file2_inners.append(f'\nФайл {i+1}: {item}')
        file2_inners.append(f'\nКоличество символов: {file2len}')
        os.remove(filename_2)
        with open(filename_2,'w+',encoding='utf-8') as file2:
            for i in file2_inners:
                file2.writelines(i)
        #filename_3 = './temp_archive/03.txt'
        with open(filename_3,'w+',encoding='utf-8') as file3:
            file3.write(f'ФИО: {FIO}')
            file3.write(f'\nГруппа: {group}')
            now = (datetime.datetime.now()).strftime('%H:%M %d.%m.%Y')
            file3.write(f'\nВремя: {now}')
        #new_arc_name = 'new.zip'
        files = [filename_1, filename_2, filename_3]
        if os.path.exists(f"./{new_arc_name}"):
            os.remove(new_arc_name)
        with zipfile.ZipFile(new_arc_name,'w') as lastf:
            for i in files:
                lastf.write(i,i.replace('./temp_archive/',''))
        shutil.rmtree('temp_archive')

main()
