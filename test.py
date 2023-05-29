import unittest
from avatar_generator import generate_cartoon_avatar

class AvatarGeneratorTestCase(unittest.TestCase):
    def test_generate_cartoon_avatar(self):
        # 测试生成卡通头像的函数是否正常工作
        avatar = generate_cartoon_avatar(300)
        self.assertEqual(avatar.size, (300, 300))
        # 在这里可以添加更多的断言，验证生成的卡通头像是否符合预期

if __name__ == '__main__':
    unittest.main()
