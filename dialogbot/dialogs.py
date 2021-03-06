
def category_form(resolution_times, types, categories):
    """Slack interactive category form"""
    def options(items):
        return [{"label": item, "value": item} for item in items]

    return {
        "callback_id": 'category',
        "title": 'Category Dialog',
        "submit_label": 'Submit',
        "elements": [
            {
                "label": "Description",
                "name": "description",
                "placeholder": "Description",
                "type": "text",
            },
            {
                "label": "Resolution Time(Hours)",
                "name": "resolution_time",
                "type": "select",
                "placeholder": "Resolution Time in hours",
                "options": options(resolution_times)
            },
            {
                "label": "Type",
                "name": "type",
                "type": "select",
                "placeholder": "Type",
                "options": options(types)
            },
            {
                "label": "Category 1",
                "name": "category_1",
                "type": "select",
                "placeholder": "List of Categories",
                "options": options(categories)
            },
            {
                "label": "Category 2",
                "name": "category_2",
                "type": "select",
                "placeholder": "List of Categories",
                "options": options(categories)
            },
        ]
    }
