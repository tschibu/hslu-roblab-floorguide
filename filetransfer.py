import paramiko
import os

_CONFIG=None

class Filetransfer():
    def __init__(self, config):
        global _CONFIG
        _CONFIG = config

    @staticmethod
    def transfer_file_from_pepper_to_local(remote_path, local_path):
        if _CONFIG is not None:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(_CONFIG.Ip, username=_CONFIG.Username, password=_CONFIG.Password)
            sftp = ssh.open_sftp()
            sftp.get(remote_path, local_path)
            sftp.remove(remote_path)
            sftp.close()
            ssh.close()

    @staticmethod
    def transfer_file_from_local_to_pepper(local_path, remote_path):
        if _CONFIG is not None:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(_CONFIG.Ip, username=_CONFIG.Username, password=_CONFIG.Password)
            sftp = ssh.open_sftp()
            sftp.put(local_path, remote_path)
            sftp.close()
            ssh.close()
            os.remove(local_path)