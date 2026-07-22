from django.contrib import admin
from .models import Project, ProjectMedia

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1  # Provides an extra empty row to upload files right away

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at')
    inlines = [ProjectMediaInline]

admin.site.register(ProjectMedia)