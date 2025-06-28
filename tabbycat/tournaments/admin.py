from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from utils.admin import ModelAdmin

from .models import Round, ScheduleEvent, Tournament


# ==============================================================================
# Tournament
# ==============================================================================

@admin.register(Tournament)
class TournamentAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'seq', 'short_name', 'current_round', 'active')
    ordering = ('seq', )


# ==============================================================================
# Round
# ==============================================================================

@admin.register(Round)
class RoundAdmin(ModelAdmin):
    list_display = ('name', 'tournament', 'seq', 'abbreviation', 'stage',
                    'draw_type', 'draw_status', 'feedback_weight', 'silent',
                    'motions_released', 'starts_at', 'completed')
    list_editable = ('feedback_weight', 'silent', 'motions_released', 'completed')
    list_filter = ('tournament', )
    search_fields = ('name', 'seq', 'abbreviation', 'stage', 'draw_type', 'draw_status')
    ordering = ('tournament__slug', 'seq')

    def get_queryset(self, request):
        from django.contrib import messages
        messages.warning(request, _("WARNING: make sure to refresh the page if any "
                                    "changes (e.g. generating a draw) have been made to "
                                    "the round since you last loaded the page. "
                                    "Not doing this can risk catastrophic data loss."))
        return super().get_queryset(request)


@admin.register(ScheduleEvent)
class ScheduleEventAdmin(ModelAdmin):
    list_display = ('tournament', 'title', 'type', 'start_time', 'end_time', 'round')
    list_filter = ('tournament', 'type')
    search_fields = ('title',)
    ordering = ('tournament', 'start_time')
