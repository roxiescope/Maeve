import time
from Maeve_service import PythonService

class MointorImageService(PythonService):
    # Define the class variables
    _svc_name_ = "Maeve Service"
    _svc_display_name_ = "Maeve Service Display Name"
    _svc_description_ = "Runs in background of Maeve app to schedule reminders"
    _exe_name_ = 'C:Users\stein\Documents\sandbox\Maeve\Maeve_service.py'
    # Override the method to set the running condition
    def start(self):
        self.isrunning =True
    # Override the method to invalidate the running condition
    # When the service is requested to be stopped.
    def stop(self):
        self.isrunning =False
    # Override the method to perform the service function
    def main(self):
        while self.isrunning:
            time.sleep(5)
# Use this condition to determine the execution context.
if __name__ == '__main__':
    MointorImageService.parse_command_line()
