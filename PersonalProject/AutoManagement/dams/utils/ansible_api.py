# coding: utf-8
from AutoManagement.AutoManagement.settings import BASE_DIR
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible import constants


class ANSRunner(object):
    def __init__(self):
        self.passwords = dict()
        self.loader = DataLoader()
        self.inventory = InventoryManager(loader=self.loader, sources=['%s/ansibleAuto/mysql/inventory/hosts' % BASE_DIR])
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        self.__initializeData()

    def __initializeData(self):
        """初始化ansible"""
        Options = namedtuple('Options',
                             ['connection',
                              'remote_user',
                              'ask_sudo_pass',
                              'verbosity',
                              'ack_pass',
                              'module_path',
                              'forks',
                              'become',
                              'become_method',
                              'become_user',
                              'check',
                              'listhosts',
                              'listtasks',
                              'listtags',
                              'syntax',
                              'sudo_user',
                              'sudo',
                              'diff'])
        self.options = Options(connection='smart',  # 表示连接远端机器 local代表本地
                          remote_user=None,
                          ack_pass=None,
                          sudo_user=None,
                          forks=5,  # 并发为5线程
                          sudo=None,
                          ask_sudo_pass=False,
                          verbosity=5,
                          module_path=None,
                          become=None,
                          become_method=None,
                          become_user=None,
                          check=False,
                          diff=False,
                          listhosts=None,
                          listtasks=None,
                          listtags=None,
                          syntax=None)

    def run(self):
        playbook = PlaybookExecutor(playbooks=['%s/ansibleAuto/mysql/mysql.yml' % BASE_DIR],  # 可接收多个yml文件
                                    inventory=self.inventory,
                                    variable_manager=self.variable_manager,
                                    loader=self.loader,
                                    options=self.options,
                                    passwords=self.passwords)
        playbook.run()






if __name__ == '__main__':
    constants.HOST_KEY_CHECKING = False
    ans = ANSRunner()
    ans.run()