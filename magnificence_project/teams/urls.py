from django.urls import path
from .views import MagnificentSevenView, MagnificentSevenTeamView, ApiHomeView, TeamsListView

urlpatterns = [
    path('', ApiHomeView.as_view(), name='api_home'),  # Serves the front page at /api/
    path('magnificent-seven/', MagnificentSevenView.as_view(), name='magnificent_seven'),
    path('magnificent-seven/team/<str:team_name>/', MagnificentSevenTeamView.as_view(), name='magnificent_seven_team'),
    path('teams/', TeamsListView.as_view(), name='teams_list'),  # Endpoint to list all teams
]
