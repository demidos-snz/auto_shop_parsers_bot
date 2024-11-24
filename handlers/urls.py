from settings import SERVER_ADDRESS

GET_VENDOR_CODES_URL: str = f'{SERVER_ADDRESS}/api/vendor_code'
POST_VENDOR_CODE_URL: str = f'{SERVER_ADDRESS}/api/vendor_code/create'
DELETE_VENDOR_CODE_URL: str = f'{SERVER_ADDRESS}/api/vendor_code/' + '{0}'
PARSERS_URL: str = f'{SERVER_ADDRESS}/parsers'
RUN_ALL_URL: str = f'{SERVER_ADDRESS}/run_all'
RUN_URL: str = f'{SERVER_ADDRESS}/run'
RUN_ALL_PAIR_DATA_URL: str = f'{SERVER_ADDRESS}/run_all_pair_data'
