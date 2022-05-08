# Run tests here

import PYOBE

exampleHTML = '''<html>
<>
</html>
'''

class engine(PYOBE.Engine):
    @staticmethod
    def fetch_data(url: str) -> bytes:
        return exampleHTML.encode()
    

eng = engine()
engine.tick()