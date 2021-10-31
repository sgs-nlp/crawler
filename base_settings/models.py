"""
base_settings.models.py
"""
APPLICATIONS = {
    # 'None': {
    #     'None': ['None', ],
    # },
    'FaceBook': {
        'Profile': ['Account', ],
        'Friends': ['Account', ],
        'Page Information': ['Account', ],
        'Group Information': ['Group', ],
        'Posts': ['Account', 'Group', ],
        'Photos': ['Account', ],
    },
    # 'LinkedIn': {
    #     'None': ['None', ],
    # }
}
