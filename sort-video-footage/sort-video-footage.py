import os, time, datetime
import pathlib
file_names = os.listdir('./to-sort')


def is_gh5_name(name):
    return name.startswith('P')


def is_iPhone_name(name):
    return not name.startswith('P')


print(file_names)

# os.rename(r'file path\OLD file name.file type', r'file path\NEW file name.file type')


for name in file_names:
    modified = os.path.getmtime('./to-sort/' + name)
    print("Date modified: "+time.ctime(modified))
    print("Date modified:",datetime.datetime.fromtimestamp(modified))
    year,month,day,hour,minute,second=time.localtime(modified)[:-3]
    new_name = '{0}-{1}-{2}--{3}-{4}-{5}'.format(str(year), str(month), str(day), str(hour), str(minute), str(second))
    if is_iPhone_name(name):
        new_name = new_name + '--iPhone.mov'
    if is_gh5_name(name):
        new_name = new_name + '--gh5.mov'
    print(new_name)
    os.rename('./to-sort/' + name, './to-sort/' + new_name)

