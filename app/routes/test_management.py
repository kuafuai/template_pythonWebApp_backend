class TestManagement:
    def __init__(self):
        self.devices = []
        self.programs = []

    def record_device(self, device):
        self.devices.append(device)

    def manage_program(self, program):
        self.programs.append(program)

    def check_device_status(self, device_id):
        for device in self.devices:
            if device.id == device_id:
                return device.status
        return None

    def check_program_status(self, program_id):
        for program in self.programs:
            if program.id == program_id:
                return program.status
        return None
