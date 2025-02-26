from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_candidate_report(candidates):
    """
    Generate a PDF report for a list of candidates.
    :param candidates: A queryset or list of candidate objects.
    :return: PDF data as bytes.
    """
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica", 12)
    p.drawString(50, height - 50, "Candidate Report")
    y = height - 80
    for candidate in candidates:
        line = f"{candidate.first_name} {candidate.last_name} - {candidate.email}"
        p.drawString(50, y, line)
        y -= 20
        if y < 50:
            p.showPage()
            y = height - 50

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
