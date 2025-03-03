{
    "name": "Hostel Management",  # Module title
    "summary": "Manage Hostel easily",  # Module subtitle phrase
    "description": "Efficiently manage the entire residential facility in the school.",  # Supports reStructuredText(RST) format (description is Deprecated)
    "version": "17.0.1.0.0",
    "author": "Trishan Fernando",
    "category": "Tools",
    # "website": "http://www.serpentcs.com",
    "license": "AGPL-3",
    "depends": ["base"],
    "data": [
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "views/hostel.xml",
        "data/data.xml",
        "views/hostel_room_views.xml",
        "views/hostel_student_views.xml",
        "views/hostel_amenities_views.xml",
        "views/hostel_category_views.xml",
        "views/hospital_doctor_views.xml"
    ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
    "installable": True,
}