def test_logger():
    """Test logger.

    :return: test result.
    :rtype: bool
    """
    from src import mylogger
    try:
        m = mylogger.get_logger('test', '/home/u1000/da_design_server/log')
        m.debug('hi, debug')
    except Exception as e:
        print(e)
        return False
    return True

if __name__ == '__main__':
    ret = test_logger()
    if not ret:
        raise Exception('Error when test_logger')
    print('Success - test_logger')

