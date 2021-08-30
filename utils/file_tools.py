def writer_file(filepath, content):
    """
    :param filepath: 文件的路径
    :param content: 要写入的内容
    :return:空
    """
    with open(file=filepath, mode='w', encoding='utf-8') as f:
        f.write(content)

def read_file(filepath):
    with open(file=filepath, mode='r', encoding='utf-8') as f:
        f.read()