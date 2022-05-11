from django.contrib import admin

# Register your models here.
from .models import Category, Post, Tag, Sidebar

admin.site.register(Category)
# admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Sidebar)


class PostAdmin(admin.ModelAdmin):
    """文章详情管理"""
    list_display = ('id', 'title', 'category', 'tags', 'pv', 'mod_date', )
    # list_filter = ('author', )
    list_filter = ('category', )
    search_fields = ('title', 'desc')
    # list_editable = ('pv',)
    list_display_links = ('id', 'title', )

    # 引入富文本编辑器
    class Media:
        # 引入样式
        css = {
            'all': ('ckeditor/cked.css',)
        }
        # 引入js
        js = (
            # jquery
            'users/js/jquery-3.6.0.min.js',
            # 'https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js',
            # 关键js
            'ckeditor/ckeditor.js',
            # 配置文件
            'ckeditor/config.js',
            # 语言支持
            'ckeditor/translations/zh.js',
        )


admin.site.register(Post, PostAdmin)