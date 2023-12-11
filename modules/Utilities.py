import os

class Utilities:
    '''
    '''
    @staticmethod
    def setup_path_files():
        '''
        '''
        list_of_paths = ['data']
        for path in list_of_paths:
            try:
                os.makedirs(path)
            except FileExistsError:
                print(f"File {path} already exist!")
            except Exception as err:
                print("Error: ",err)