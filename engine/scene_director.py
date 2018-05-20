import sys

class SceneDirector(object):
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        if SceneDirector.__instance == None:
            SceneDirector()
        return SceneDirector.__instance

    def __init__(self):
        self.scenes = {}
        self.current_scene = None

        if SceneDirector.__instance != None:
            raise Exception("SceneDirector is a Singleton class!!")
        else:
            SceneDirector.__instance = self

    def add_scene(self, name, scene_self):
        self.scenes[name] = scene_self

    def go_scene(self, name):
        if name in self.scenes:
            self.current_scene = self.scenes[name]
        else:
            raise Exception("Don't exists escene with name: ", name)

    def show_default_scene(self):
        if len(self.scenes) > 0:
            scene_name = list(self.scenes.keys())[0]
            self.go_scene(scene_name)
            return self.get_current_scene()
        else:
            sys.exit("Needs register an scene with name and isntance Ex: {'my_scene': my_scene}")

    def get_current_scene(self):
        return self.current_scene
    
    def exists_current_scene(self):
        return self.current_scene != None