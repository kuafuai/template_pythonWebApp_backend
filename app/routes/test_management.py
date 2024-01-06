class TestManagement:
    def __init__(self):
        self.devices = []
        self.programs = []

    def record_device(self, device: Device) -> None:
        """
        Used to record testing devices.

        Args:
            device (Device): The device to be recorded.

        Returns:
            None
        """
        self.devices.append(device)

    def manage_program(self, program: Program) -> None:
        """
        Used to manage testing programs.

        Args:
            program (Program): The program to be managed.

        Returns:
            None
        """
        self.programs.append(program)

    def check_device_status(self, device_id: int) -> str:
        """
        Used to check the status of a device.

        Args:
            device_id (int): The ID of the device.

        Returns:
            str: The status of the device.
        """
        for device in self.devices:
            if device.id == device_id:
                return device.status
        return None

    def check_program_status(self, program_id: int) -> str:
        """
        Used to check the status of a program.

        Args:
            program_id (int): The ID of the program.

        Returns:
            str: The status of the program.
        """
        for program in self.programs:
            if program.id == program_id:
                return program.status
        return None
