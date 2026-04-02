from django.test import TestCase
from django.urls import reverse
from .models import PackingMachine

class MachineTests(TestCase):
    def setUp(self):
        # 初始化测试数据
        PackingMachine.objects.create(
            material_code="2021400001",
            drawing_no="DW001",
            machine_name="测试零件",
            model_type="XQD-19气动打包机"
        )

    def test_machine_list(self):
        # 测试列表页
        response = self.client.get(reverse('machine:machine_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "测试零件")

    def test_machine_add(self):
        # 测试添加物料
        data = {
            'drawing_no': 'DW002',
            'machine_name': '新增零件',
            'model_type': 'XQD-25气动打包机'
        }
        response = self.client.post(reverse('machine:machine_add'), data, follow=True)
        self.assertEqual(PackingMachine.objects.count(), 2)
        self.assertContains(response, "添加成功")