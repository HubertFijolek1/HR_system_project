from rest_framework import viewsets
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    
    @action(detail=False, methods=["get"], url_path="export-pdf")
    def export_pdf(self, request):
        from .reports.pdf_report import generate_candidate_report
        candidates = self.get_queryset()
        pdf_data = generate_candidate_report(candidates)
        from django.http import HttpResponse
        response = HttpResponse(pdf_data, content_type="application/pdf")
        response["Content-Disposition"] = "attachment; filename=candidate_report.pdf"
        return response

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