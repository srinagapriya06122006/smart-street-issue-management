"""
Auto-escalation engine.
Call `run_auto_escalation()` periodically (e.g., every 60 seconds).
Complaints that have been sitting at a non-final level for >= 5 minutes
without being resolved are automatically escalated to the next level.
"""

from django.utils import timezone
from datetime import timedelta

from .models import (
    Complaint, ComplaintHistory,
    STATUS_PENDING, STATUS_ESCALATED, STATUS_RESOLVED,
    LEVEL_ORDER,
)

from django.conf import settings

SLA_MINUTES = getattr(settings, "COMPLAINT_SLA_MINUTES", 5)


def run_auto_escalation():
    cutoff = timezone.now() - timedelta(minutes=SLA_MINUTES)

    # Escalate PENDING complaints older than SLA that are not at final level
    pending_overdue = Complaint.objects.filter(
        status=STATUS_PENDING,
        created_at__lte=cutoff,
    ).exclude(current_level=LEVEL_ORDER[-1])

    # Escalate already-ESCALATED complaints that have been sitting for another SLA window
    escalated_overdue = Complaint.objects.filter(
        status=STATUS_ESCALATED,
        escalated_at__lte=cutoff,
    ).exclude(current_level=LEVEL_ORDER[-1])

    escalated_count = 0
    for c in list(pending_overdue) + list(escalated_overdue):
        if c.next_level is None:
            continue

        from_level = c.current_level
        to_level = c.next_level
        now = timezone.now()

        c.current_level = to_level
        c.status = STATUS_ESCALATED
        c.escalated_at = now
        c.escalation_reason = f"Auto-escalated: SLA of {SLA_MINUTES} minutes exceeded."
        c.save(update_fields=["current_level", "status", "escalated_at", "escalation_reason"])

        ComplaintHistory.objects.create(
            complaint=c,
            from_level=from_level,
            to_level=to_level,
            action=ComplaintHistory.ACTION_AUTO,
            reason=c.escalation_reason,
            timestamp=now,
        )
        escalated_count += 1

    return escalated_count
