from django.contrib import admin
from .models import *   

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):    
    list_display = ('id', 'full_name')
    
    @admin.display(description='nombre completo')
    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name} {obj.second_last_name}'.upper()         
    
@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'question', 'attempts', 'duration')