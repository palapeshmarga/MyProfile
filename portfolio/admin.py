from django.contrib import admin
from .models import Project, ProjectMedia

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 2

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at')
    inlines = [ProjectMediaInline]