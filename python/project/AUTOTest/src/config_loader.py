import os
import configparser
from pathlib import Path


class ConfigLoader:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation(),
            allow_no_value=True
        )
        self.config.optionxform = str  # 保持键的大小写
        self.config.read(self._get_config_path(config_file))

        # 初始化路径（自动创建目录）
        self._init_paths()

    def _get_config_path(self, filename):
        """处理配置文件路径"""
        config_path = Path(__file__).parent / filename
        if not config_path.exists():
            raise FileNotFoundError(f"配置文件 {filename} 不存在")
        return config_path

    def _init_paths(self):
        """自动创建所需目录"""
        paths_section = self.config['Paths']
        for key in paths_section:
            path = Path(paths_section[key])
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)

    def get(self, section, option, fallback=None):
        """安全获取配置项"""
        try:
            return self.config.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return fallback

    @property
    def database_config(self):
        """获取数据库配置字典"""
        return {
            'host': self.config.get('Database', 'host'),
            'port': self.config.getint('Database', 'port'),
            'user': self.config.get('Database', 'user'),
            'password': self.config.get('Database', 'password'),
            'database': self.config.get('Database', 'database'),
            'auto_reconnect': self.config.getboolean('Database', 'auto_reconnect')
        }

    @property
    def webdriver_config(self):
        """获取浏览器驱动配置字典"""
        return {
            'browser': self.config.get('WebDriver', 'browser'),
            'headless': self.config.getboolean('WebDriver', 'headless'),
            'timeout': self.config.getint('WebDriver', 'timeout'),
            'download_dir': self.config.get('WebDriver', 'download_dir')
        }


# 使用示例
if __name__ == "__main__":
    loader = ConfigLoader()

    # 获取基础配置
    print(f"项目名称: {loader.get('Project', 'name')}")
    print(f"当前环境: {loader.get('Project', 'env')}")

    # 获取数据库配置
    db_config = loader.database_config
    print(f"\n数据库连接信息: {db_config}")

    # 获取浏览器配置
    driver_config = loader.webdriver_config
    print(f"\n浏览器配置: {driver_config}")