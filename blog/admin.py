#from django.conf import global_setting
from django.contrib import admin, messages
from .models import Post,Comment,Image
from django.utils.translation import ugettext_lazy as _
from inline_actions.actions import DefaultActionsMixin, ViewAction
from inline_actions.admin import InlineActionsMixin, InlineActionsModelAdminMixin
from django.utils.html import format_html


#TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
 # 'django.core.context_processors.request',
#)


admin.site.register(Image)

#def make_published(modeladmin, request, queryset):
 #   queryset.update(status='p')
#make_published.short_description = "Mark selected stories as published"


class CommentTabularInline(admin.TabularInline):
    model = Comment
    extra = 1
   



class UnPublishActionsMixin(object):
    def get_inline_actions(self, request, obj=None):
        actions = super(UnPublishActionsMixin, self).get_inline_actions(request, obj)
        if obj:
            if obj.status == 'd':
                actions.append('publish')
            elif obj.status == 'p':
                actions.append('unpublish')
        return actions

    def publish(self, request, obj, parent_obj=None):
        obj.status = 'p'
        obj.save()
        messages.info(request, _("Post published."))
    publish.short_description = _("Publish")

    def unpublish(self, request, obj, parent_obj=None):
        obj.status = 'd'
        obj.save()
        messages.info(request, _("Post unpublished."))
    unpublish.short_description = _("Unpublish")


class PostAdmin(UnPublishActionsMixin,
                   ViewAction,
                   InlineActionsModelAdminMixin,admin.ModelAdmin):
    
    def cover_image(self, obj):
        return format_html('<img src="/media/{}" width = 100 height = 100/>'.format(obj.image_post))


    list_display = ['title', 'created_date', 'status','cover_image',]
    ordering = ['title']
    actions = ['make_published']
    list_filter = ['status','created_date']
    search_fields = ['title','text']
    readonly_fields = ['cover_image']


    
    inlines = [CommentTabularInline]



#def make_published(self, request, queryset):
#	rows_updated = queryset.update(status='p')
#	for post in queryset:
#		post.publish()
#	if rows_updated == 1:
#	    message_bit = "1 story was"
#	else:
#	    message_bit = "%s stories were" % rows_updated
#	self.message_user(request,"%s successfully marked published." % message_bit)



#class PostAdmin(admin.ModelAdmin):
	#list_display = ['title']
	#list_filter = ['status']
   # inlines = [CommentAdminInline]

#    def created_date(self,obj):
 #       return obj.get_value()


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

 