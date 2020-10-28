class Episode:
    def __init__(self, number:str, name:str, release_date:str):
        self.number = number
        self.name = name
        self.release_date = release_date
    
    def __str__(self):
        return f'Номер: {self.number}, Название: {self.name}, Дата выхода: {self.release_date}'
    
    def __repr__(self):
        return self.__str__()

class Schedule:
    def __init__(self, name:str, episodes:list):
        self.name = name
        self.episodes = episodes
    
    def __str__(self):
        return self.name + '\n' + '\n'.join(str(episode) for episode in self.episodes)
        

    def addEpisode(self, episode:Episode):
        self.episodes.append(episode)