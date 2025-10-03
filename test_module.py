import unittest
import medical_data_visualizer

class TestMedicalDataVisualizer(unittest.TestCase):
    def test_cat_plot(self):
        fig = medical_data_visualizer.draw_cat_plot()
        self.assertTrue(fig is not None)

    def test_heat_map(self):
        fig = medical_data_visualizer.draw_heat_map()
        self.assertTrue(fig is not None)

if __name__ == "__main__":
    unittest.main()
