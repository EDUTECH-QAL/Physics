from django.urls import path
from . import views

urlpatterns = [
    path('', views.module_home, name='module_home'),
    path('work/', views.work_calculator, name='work'),
    path('kinetic/', views.kinetic_energy_calculator, name='kinetic'),
    path('gpe/', views.gpe_calculator, name='gpe'),
    path('elastic/', views.elastic_calculator, name='elastic'),
    path('power/', views.power_calculator, name='power'),
    path('efficiency/', views.efficiency_calculator, name='efficiency'),
    path('work_energy/', views.work_energy_theorem, name='work_energy'),
    path('friction_work/', views.friction_work_calculator, name='friction_work'),
    path('energy_conservation/', views.energy_conservation_solver, name='energy_conservation'),
]
