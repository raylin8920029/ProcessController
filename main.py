import os
import subprocess


class ProcessController(object):
    def __init__(self):
        # The index of first process data
        self.TASKLIST_PROCESS_INFO_START_INDEX = 3

        # The list of process
        self.process_list = []

    def kill_process_by_name(process_name):
        try:
            killed = os.system('taskkill /fi "WINDOWTITLE eq %s"' % process_name)
        except Exception, e:
            killed = 0
        return killed

    @staticmethod
    def list_all_process_info():
        try:
            print subprocess.check_output('tasklist')
        except subprocess.CalledProcessError as grepexc:
            print "Called Process Error Exception Is Raised!!"
            print "Error code :", grepexc.returncode, grepexc.output
        except Exception:
            print "Unexpected Exception Is Raised!!"

    def __create_process_list(self):
        self.process_list = subprocess.check_output('tasklist').split('\n')
        print self.process_list[self.TASKLIST_PROCESS_INFO_START_INDEX]


def main():
    control = ProcessController()
    control.list_all_process_info()

if __name__ == "__main__":
    main()
