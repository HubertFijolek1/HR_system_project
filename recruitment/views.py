from rest_framework import viewsets
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    from django_filters.rest_framework import DjangoFilterBackend
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["last_name"]
    pagination_class = None
    
    from rest_framework.decorators import action
    from rest_framework.response import Response
    
    @action(detail=False, methods=["get"], url_path="reports")
    def reports(self, request):
        total_candidates = self.get_queryset().count()
        report = {
            "total_candidates": total_candidates,
            # Further report calculations can be added here
        }
        return Response(report)

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer