import psutil

def check_process_status(process_name):
    """
    Return status of process based on process name.
    """
    process_status = [ proc for proc in psutil.process_iter() if proc.name() == process_name ]
    if process_status:
        for current_process in process_status:
            print("Process id is %s, name is %s, staus is %s"%(current_process.pid, current_process.name(), current_process.status()))
    else:
        print("Process name not valid", process_name)