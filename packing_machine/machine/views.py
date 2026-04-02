from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import PackingMachine


def machine_list(request):
    """
    物料列表页面
    """
    model_type = request.GET.get("model_type")
    if model_type:
        machines = PackingMachine.objects.filter(model_type=model_type).order_by("material_code")
    else:
        machines = PackingMachine.objects.all().order_by('material_code')
    return render(request, 'machines/list.html', {
        'machines': machines,
        'current_model': model_type,
    })


def machine_detail(request, code):
    """物料详情页面"""
    machine = get_object_or_404(PackingMachine, material_code=code)
    return render(request, "machines/detail.html", {'machine': machine})


def machine_add(request):
    """
    添加物料（简易表单，无前端验证）
    """
    if request.method == "POST":
        #获取表单数据
        data = {
            'material_code': request.POST.get('material_code'),
            'drawing_no': request.POST.get('drawing_no').strip(),
            'standards': request.POST.get('standards').strip(),
            'machine_name': request.POST.get('machine_name').strip(),
            'purchase_price': request.POST.get('purchase_price',0),
            'selling_price': request.POST.get('selling_price'),
            'model_type': request.POST.get('model_type'),
            'image': request.FILES.get('image')
        }

        if not data['machine_name'] or not data['drawing_no']:
            messages.error(request, '零件名称和图号为必填项！')
        #创建物料
        try:
            PackingMachine.objects.create(**data)
            messages.success(request, f"物料{data['material_code']}添加成功!")
            return redirect('machines:machine_list')

        except Exception as e:
            messages.error(request, f"添加失败{str(e)}")

    return render(request, 'machines/add.html')


def machine_delete(request, code):
    """删除物料"""
    machine = get_object_or_404(PackingMachine, material_code=code)

    machine_name = machine.machine_name
    machine.delete()
    messages.success(request, f"物料{code}({machine_name})删除成功!")
    return redirect('machines:machine_list')


def machine_edit(request,code):
    machine = get_object_or_404(PackingMachine,material_code=code)

    if request.method == 'POST' :
        machine.drawing_no = request.POST.get('drawing_no').strip()
        machine.standards = request.POST.get('standards').strip()
        machine.machine_name = request.POST.get('machine_name').strip()
        machine.purchase_price = request.POST.get('purchase_price') or None
        machine.selling_price = request.POST.get('selling_price') or None
        machine.model_type = request.POST.get('model_type')
        if request.FILES.get('image'):
            machine.image = request.FILES.get("image")
        try:
            machine.save()
            messages.success(request,f'物料{code}修改成功！')
            return redirect('machine:machine_edit',code=code)
        except Exception as e :
            messages.error(request,f"修改失败:{str(e)}")
    return render(request,'machines/edit.html',{'machine':machine})
