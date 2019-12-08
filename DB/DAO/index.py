from DAO.sqlExecution import *


class Index(SqlExecution):
    @abstractmethod
    def select_index(self, url):
        pass  # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦
