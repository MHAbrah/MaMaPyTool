from socket import *

class MayaConnection(object):
    """A representation of a connection to Maya,
    used to send python code to the Command Port of Maya."""

    def __init__(self, host='127.0.0.1', port=54321):
        self.address = (host, port)

    def send_script(self, file_path, verbose=True):
        """Sends the content of a file as Python code to Maya's Command Port."""
        with open(file_path, 'r') as script_file:
            if verbose:
                script_name = file_path
                greeting = "import sys\nsys.stdout.write(\"Receiving script '{0}'...\")".format(script_name)
                goodbye = "sys.stdout.write(\"Script '{0}' executed!\")".format(script_name)
                send_command(greeting)
                send_command(script_file.read())
                send_command(goodbye)
            else:
                send_command(script_file.read())


    def send_code(self, code):
        """Sends code to Maya through the Command Port. Multiple lines of code can be sent."""
        client = socket(AF_INET,  SOCK_STREAM)
        try:
            client.connect(self.address)
            client.send(code)
            response = client.recv(2048)
            client.close()
            print('Response: "{0}"'.format(response))
        except error:
            raw_input("Could not connect to Maya. Did you open a command port from Maya?")

if __name__ == '__main__':
    from datetime import datetime
    maya_connection = MayaConnection()
    maya_connection.send_code("import sys\nsys.stdout.write('MayaConnection test: ({0})')".format(datetime.now().time()))