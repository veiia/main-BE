from enum import Enum


class FeedbackThemes(str, Enum):
    PROJECTS = "Projects"
    SITES = "Sites"
    DOMAINS = "Domains"
    COMPLAINT = "Complaint"
    OTHER = "Other"

    @classmethod
    def to_dict(cls) -> dict[str, str]:
        return {k.lower(): k for k in cls}
