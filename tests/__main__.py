import unittest
import inspect
from engine import *

class EsceneTest(unittest.TestCase):
    def setUp(self):
        self.scene = Scene()

    def test_empty(self):
        """
        nice to test
        """
        total_entities = len(self.scene.get_all())
        self.assertEqual(total_entities, 0)
    
    def test_single_add(self):
        new_entity = 5
        new_scene = self.scene.add(new_entity, 'dummie')
        self.assertEqual(len(new_scene.get_all()), 1)
    
    def test_single_remove(self):
        new_scene = self.scene.remove('dummie')
        self.assertEqual(len(new_scene.get_all()), 0)

class EntityTest(unittest.TestCase):
    def setUp(self):
        self.fixture = "Rectangle"
        self.initial_position = (0, 0)
        self.color = "blue"
        self.entity = Entity(self.fixture, self.initial_position, self.color)

    def test_update_color(self):
        new_color = "red"
        expected_entity = Entity(self.fixture, self.initial_position, new_color)
        new_entity = self.entity.set_color(new_color)
        self.assertEqual(new_entity.get_color(), expected_entity.get_color())
    
    def test_update_position(self):
        new_position = (10, 10)
        expected_entity = Entity(self.fixture, new_position, self.color)
        new_entity = self.entity.set_position(new_position)
        self.assertEqual(new_entity.get_position(), expected_entity.get_position())

    def test_render(self):
        new_entity = self.entity.render()
        self.assertIsInstance(new_entity, Entity)

class GameEngineTest(unittest.TestCase):
    def setUp(self):
        self.fps = 60
        self.size = (600, 800)
        self.engine = GameEngine(self.fps, self.size)
    
    def test_add_scene():
        scene_name = "home"
        scene_self = "<>"
        new_instance = self.engine.add_scene(scene_name, scene_self)
        self.assertEqual(len(new_instance.all_scenes()), 1)
    
    def test_show_scene():
        scene_name = "home"
        current_scene = self.engine.show_scene('home')
        self.assertEqual(self.engine.current_scene(), current_scene)
    
    def test_replace_scene():
        sceneA = "main_menu"
        sceneB = "level_1"
        current_scene = self.engine.replace_scene(sceneA, sceneB)
        self.assertEqual(self.engine.current_scene(), sceneB)

if __name__ == '__main__':
    unittest.main()