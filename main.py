import psutil


class ProcessController(object):
    def __init__(self):
        self.process_info_list = []

    def __create_process_info_list(self):
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
            except psutil.NoSuchProcess:
                pass
            else:
                self.process_info_list.append([pinfo['name'], pinfo['pid']])

    def kill_process_by_name(self, process_name):
        print "[Action Start]"
        print "\tAction : Kill process by name"
        print "\tInput Process Name : %s" % process_name
        print "================== Stopped Process List =================="

        self.__create_process_info_list()
        process_counter = 0

        for process_info in self.process_info_list:
            if process_name in process_info[0]:
                process_counter += 1
                process = psutil.Process(process_info[1])
                process.terminate()
                print "%s. Stop Process : %s" % (str(process_counter), process_info[0])

        print "[Action End]"

    @staticmethod
    def list_all_process_info():
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
            except psutil.NoSuchProcess:
                pass
            else:
                print(pinfo)


def main():
    control = ProcessController()
    control.kill_process_by_name("notepad")

if __name__ == "__main__":
    main()
