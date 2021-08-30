import pytest
import os

if __name__ == '__main__':
    pytest.main(['-sq'])
    # 运行结果目录  报告存放目录
    # os.system(r"allure generate allure-results -o allure-report --clean")
    # os.system('allure open allure-report')
