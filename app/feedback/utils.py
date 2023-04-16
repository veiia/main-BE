from enum import Enum


class FeedbackThemes(str, Enum):
    PROJECTS = "Projects"
    SITES = "Sites"
    DOMAINS = "Domains"
    COMPLAINT = "Complaint"
    OTHER = "Other"
