import os
from snowsql.const.messages import log_message

class FileLogger:
    def __init__(self, base_dir, log_dir):
        self.base = base_dir
        self.log = log_dir
        self.full_dir = os.path.join(base_dir, log_dir)
        
    def create_folder(self):
        if not os.path.exists(
            self.full_dir
        ):
            os.makedirs(self.full_dir)
            
    def write_log(self, file_name, content, is_error):
        log_file_path = os.path.join(self.full_dir, file_name)
        if os.path.exists(
            log_file_path
        ):
            mode = 'a'
        else:
            mode = 'w'
        
        with open(log_file_path, mode = mode) as file:
            if mode == 'w':
                file.write(self.format_log(content, is_error))
            if mode == 'a':
                file.append(self.format_log(content, is_error))
            else:
                raise Exception("Invalid Mode.")
    """
    Decide on a format:
    
    1. Error Case
    {timestamp}: Error with deprication
    <Function Name>: Arguments
    <Error Message - detail>: Multiple lines
    
    2. Success Case
    {timestamp}: Success with deprication
    <Function Name>: Arguments
    <Success Result>
    
    3. Syntatic Deprication:
    <File Name>
    <Warning Message>
    """
    
    """
    Database Logging
    NoSQL -> JSON based logging 
    SQL -> Table based log
    """