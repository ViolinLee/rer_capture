# coding:utf-8

"""
1）监视磁盘空间：>=95%不启动/停止rer_record.py的进程
2）监视脚本进程：满足1）中磁盘空间<95%
"""

import os
import sys
import signal
import psutil
from apscheduler.schedulers.blocking import BlockingScheduler


def check_process(process_name):
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'cmdline'])
        except psutil.NoSuchProcess:
            pass
        else:
            if process_name in ''.join(pinfo['cmdline']):
                return pinfo['pid']


def monitor_job():
    # 1）磁盘空间扫描
    try:
        st = psutil.disk_usage('/data')
        used_percent = st.percent
    except FileNotFoundError:
        print('Space Not Found Error.')
        scheduler.remove_job(job_id='monitor')  # 移除任务
        scheduler.shutdown(wait=False)  # 关闭定时任务
        sys.exit(-3)

    # 2）录像进程监控
    main_pid = check_process("rer_record.py")
    if used_percent > 95:
        if isinstance(main_pid, int):
            print('No enough space.')
            os.killpg(main_pid, signal.SIGKILL)  # 杀掉进程
            sys.exit(-3)  # 退出程序
        scheduler.remove_job(job_id='monitor')
        scheduler.shutdown(wait=False)
    else:
        if not isinstance(main_pid, int):
            os.system('nohup python3 -u /home/pi/Downloads/rer_capture/rer_record.py &')


os.system('nohup python3 -u /home/pi/Downloads/rer_capture/rer_record.py &')

scheduler = BlockingScheduler(timezone='Asia/Shanghai')
scheduler.add_job(monitor_job, 'interval', id='monitor', minutes=1)
scheduler.start()
