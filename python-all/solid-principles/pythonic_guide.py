"""
    A Pythonic Guide to SOLID Design Principles
    
    https://dev.to/ezzy1337/a-pythonic-guide-to-solid-design-principles-4c8i
"""

# Single Responsibility Principle (SRP) - v2

class FTPClient:
  def __init__(self, host, port, FTPDriver):
    self._client = FTPDriver(host, port)
  
  def upload(self, file:bytes):
    self._client.upload(file)

  def download(self, target:str) -> bytes:
    return self._client.download(target)

class SFTPClient(FTPClient):
  def __init__(self, host, user, password, SFTPDriver):
    self._client = SFTPDriver(host, username=user, password=password)
  
  def upload(self, file:bytes):
    with self._client.Connection() as sftp:
      sftp.put(file)

  def download(self, target:str) -> bytes:
    with self._client.Connection() as sftp:
      return sftp.get(target)


# # Single Responsibility Principle (SRP) - v1

# class FTPClient:
#   def __init__(self, FTPDriver, SFTPDriver, **kwargs):
#     self._ftp_client = FTPDriver(kwargs['host'], kwargs['port'])
#     self._sftp_client = SFTPDriver(kwargs['sftp_host'], kwargs['user'], kwargs['pw'])

#   def upload(self, file:bytes, **kwargs):
#     is_sftp = kwargs['sftp']
#     if is_sftp:
#       with self._sftp_client.Connection() as sftp:
#         sftp.put(file)
#     else:
#       self._ftp_client.upload(file)

#   def download(self, target:str, **kwargs) -> bytes:
#     is_sftp = kwargs['sftp']
#     if is_sftp:
#       with self._sftp_client.Connection() as sftp:
#         return sftp.get(target)
#     else:
#       return self._ftp_client.download(target)