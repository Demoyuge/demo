import os
import shutil
import  multiprocessing
import time
def copy_file(file_name, src_dir, dst_dir):
    # 源文件的路径
    src_file_path = src_dir + "/" + file_name
    # 目标文件的路径
    dst_dir_path = dst_dir + "/" + file_name
    # 显示当前进程对象
    print(multiprocessing.current_process())
    # 创建或者打开文件写入文件数据
    with open(dst_dir_path, "wb") as dst_file:
        # 打开源文件获取原文件数据
        with open(src_file_path, "rb") as src_file:
            # 循环读取文件中的数据
            while True:
                file_data = src_file.read(1024)
                if file_data:
                    # 把源文件的数据写入到目标文件中
                    dst_file.write(file_data)
                else :
                    break

    if __name__ == '__main__':
        # 源目录
        src_dir = "test"
        # 目标目录
        dst_dir = "/home/python/Desktop/test"

        #判断文件是否在指定目录上
        if os.path.exists(dst_dir):
            # 删除目标目录
            shutil.rmtree(dst_dir)

        # 创建目标文件夹
        os.mkdir(dst_dir)
        # 获取源目录下的文件列表信息
        file_list = os.listdir(src_dir)

        # 创建进程池
        pool = multiprocessing.Pool(3)

        for file_name in file_list:
            pool.apply_async(copy_file,(file_name,src_dir,dst_dir))
    # 关闭进程池不再接收其它任务
    pool.close()
    # 主进程等待进程池执行完成以后程序再退出
    pool.join()
