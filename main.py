import psutil


class ProcessController(object):
    def __init__(self):
        # The index of first process data
        self.process_info_list = []

    @staticmethod
    def list_all_process_info_by_tasklist():
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
            except psutil.NoSuchProcess:
                pass
            else:
                print(pinfo)

    def kill_process_by_name(self, process_name):
        print "Input Process Name : %s" % process_name
        print "================== Stopped Process List =================="

        self.__create_process_info_list()
        process_counter = 0

        for process_info in self.process_info_list:
            if process_name in process_info[0]:
                process_counter += 1
                print "%s. Stop Process : %s \n" % (str(process_counter), process_info[0])
                process = psutil.Process(process_info[1])
                process.terminate()

    def __create_process_info_list(self):
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
            except psutil.NoSuchProcess:
                pass
            else:
                self.process_info_list.append([pinfo['name'], pinfo['pid']])


def main():
    control = ProcessController()
    control.kill_process_by_name("notepad")

if __name__ == "__main__":
    main()
