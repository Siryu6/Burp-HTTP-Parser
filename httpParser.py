import json
import re

class HttpParser:
    def __init__(self, raw_req):
        self.raw_req = raw_req.replace('\r\n', '\n')
        self.method = self.raw_req.split(' ')[0]
        self.host = (self.raw_req.split('Host: '))[1].split('\n')[0]
        self.path = self.raw_req.split(' ')[1]
        self.headers = self.preParse()[0]
        self.raw_params = self.preParse()[1]
        self.params = self.parseParam()
    
    def preParse(self):
        header_line = True
        first_line = True
        raw_params = ""
        headers = {}
        for line in self.raw_req.split('\n'):
            # Skipping first line
            if first_line is True:
                first_line = False
            else:
                # Getting headers
                if header_line is True:
                    if line == '':
                        header_line = False
                    else :
                        headers[line.split(': ')[0]] = line.split(': ')[1]
                else :
                    if not raw_params:
                        raw_params = raw_params + line
                    else:
                        raw_params = raw_params + '\n' + line
        return([headers, raw_params])
    
    def parseParam(self):
        parsed_params = {}
        if self.raw_params:
            # "multipart/form-data Form"
            if "multipart/form-data" in self.headers["Content-Type"]:
                boundary = "--" + self.headers["Content-Type"].split('boundary=')[1]
                for param in self.raw_params.split(boundary):
                    if param == "--\n" or param == "": # Stop at the end and escape split()[0] which is empty 
                        pass
                    else:
                        param_info = param.split('\n')[1]
                        param_name = re.search('Content-Disposition: form-data; name="(.*?)"', param_info).group(1)
                        param_value = param.split(param_info+"\n")[1][1:-1]
                        parsed_params[param_name]=param_value
            # "application/json" Form
            elif "application/json" in self.headers["Content-Type"]:
                parsed_params=json.loads(self.raw_params)
            # Insert elif to add new content type 
            #"application/x-www-form-urlencoded" Form
            else: 
                for param in self.raw_params.split('&'):
                    parsed_params[param.split('=')[0]] = param.split('=')[1]
        return(parsed_params)