from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=250, help_text="Short summary shown on the main homepage card")
    description = models.TextField(help_text="Full detailed description shown on the project page")
    technology = models.CharField(max_length=200, help_text="e.g. Django, PHP Laravel, React, Python")
    thumbnail = models.FileField(upload_to='projects/thumbnails/', help_text="Cover picture or GIF for the home page card")
    demo_url = models.URLField(blank=True, null=True, help_text="Live demo or website link (optional)")
    github_url = models.URLField(blank=True, null=True, help_text="GitHub repository link (optional)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ProjectMedia(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image or GIF'),
        ('video', 'Video (MP4)'),
    )
    project = models.ForeignKey(Project, related_name='media_files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='projects/gallery/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='image')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.project.title} - {self.get_media_type_display()} ({self.id})"