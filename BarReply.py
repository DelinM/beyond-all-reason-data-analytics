



class BarReply:

    def __init__(self, replay_path: str) -> None:

        if not self._is_valid_spring_path(replay_path):
            raise ValueError('Invalid replay path: Please check if provided file with sdfz extension')

        self.replay_path = replay_path


    def _is_valid_spring_path(self, replay_path: str) -> bool:
        if replay_path.split('.')[-1] != 'sdfz':
            return False
        return True

