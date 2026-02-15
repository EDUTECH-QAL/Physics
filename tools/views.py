from django.shortcuts import render, redirect
from math import cos, radians, sqrt

def module_home(request):
    return render(request, 'tools/module_home.html')

def set_lang(request, code):
    if code not in ('ar', 'en'):
        code = 'ar'
    request.session['lang'] = code
    next_url = request.META.get('HTTP_REFERER') or '/'
    return redirect(next_url)

def _f(x, default=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default

def work_calculator(request):
    result = None
    if request.method == 'POST':
        F = _f(request.POST.get('F'))
        d = _f(request.POST.get('d'))
        theta = _f(request.POST.get('theta'), 0.0)
        if F is not None and d is not None and theta is not None:
            result = F * d * cos(radians(theta))
    return render(request, 'tools/work.html', {'result': result})

def kinetic_energy_calculator(request):
    result = None
    if request.method == 'POST':
        m = _f(request.POST.get('m'))
        v = _f(request.POST.get('v'))
        if m is not None and v is not None and m >= 0:
            result = 0.5 * m * v * v
    return render(request, 'tools/kinetic.html', {'result': result})

def gpe_calculator(request):
    result = None
    if request.method == 'POST':
        m = _f(request.POST.get('m'))
        g = _f(request.POST.get('g'), 9.8)
        h = _f(request.POST.get('h'))
        if m is not None and h is not None and g is not None and m >= 0:
            result = m * g * h
    return render(request, 'tools/gpe.html', {'result': result})

def elastic_calculator(request):
    result = None
    if request.method == 'POST':
        k = _f(request.POST.get('k'))
        x = _f(request.POST.get('x'))
        if k is not None and x is not None and k >= 0:
            result = 0.5 * k * x * x
    return render(request, 'tools/elastic.html', {'result': result})

def power_calculator(request):
    result = None
    mode = request.POST.get('mode') if request.method == 'POST' else 'wt'
    if request.method == 'POST':
        if mode == 'wt':
            W = _f(request.POST.get('W'))
            t = _f(request.POST.get('t'))
            if W is not None and t is not None and t != 0:
                result = W / t
        else:
            F = _f(request.POST.get('F'))
            v = _f(request.POST.get('v'))
            theta = _f(request.POST.get('theta'), 0.0)
            if F is not None and v is not None and theta is not None:
                result = F * v * cos(radians(theta))
    return render(request, 'tools/power.html', {'result': result, 'mode': mode})

def efficiency_calculator(request):
    result = None
    if request.method == 'POST':
        input_value = _f(request.POST.get('input_value'))
        output_value = _f(request.POST.get('output_value'))
        if input_value is not None and output_value is not None and input_value != 0:
            result = (output_value / input_value) * 100.0
    return render(request, 'tools/efficiency.html', {'result': result})

def work_energy_theorem(request):
    result = None
    if request.method == 'POST':
        m = _f(request.POST.get('m'))
        vi = _f(request.POST.get('vi'))
        vf = _f(request.POST.get('vf'))
        if m is not None and vi is not None and vf is not None and m >= 0:
            result = 0.5 * m * (vf * vf - vi * vi)
    return render(request, 'tools/work_energy.html', {'result': result})

def friction_work_calculator(request):
    result = None
    if request.method == 'POST':
        mu = _f(request.POST.get('mu'))
        m = _f(request.POST.get('m'))
        g = _f(request.POST.get('g'), 9.8)
        d = _f(request.POST.get('d'))
        if None not in (mu, m, g, d) and m >= 0 and mu >= 0 and d >= 0:
            result = -mu * m * g * d
    return render(request, 'tools/friction_work.html', {'result': result})

def energy_conservation_solver(request):
    result = None
    solved_for = None
    mode = request.POST.get('mode') if request.method == 'POST' else 'grav_vf'
    if request.method == 'POST':
        if mode == 'grav_vf':
            m = _f(request.POST.get('m'))
            g = _f(request.POST.get('g'), 9.8)
            h = _f(request.POST.get('h'))
            vi = _f(request.POST.get('vi'), 0.0)
            if None not in (m, g, h, vi) and m >= 0:
                vf_sq = vi * vi + 2 * g * h
                result = sqrt(vf_sq) if vf_sq >= 0 else None
                solved_for = 'v_f'
        elif mode == 'spring_vf':
            m = _f(request.POST.get('m'))
            k = _f(request.POST.get('k'))
            x = _f(request.POST.get('x'))
            vi = _f(request.POST.get('vi'), 0.0)
            if None not in (m, k, x, vi) and m > 0 and k >= 0:
                vf_sq = vi * vi + (k * x * x) / m
                result = sqrt(vf_sq)
                solved_for = 'v_f'
    return render(request, 'tools/energy_conservation.html', {'result': result, 'mode': mode, 'solved_for': solved_for})

# Create your views here.
