from .api_data import ApiData  # Assuming your class is in api_data.py
from .data_manipulation import DataManipulator

def api_data_processor(request):
    api_data = ApiData()
    manipulator = DataManipulator()
    context = {
        'api_data': api_data.get_data(),
        'applications': api_data.get_application_list(),
        'resources': api_data.get_resource_list(),
        'specific_application': api_data.get_specifc_application('application_name'),
        'specific_resource': api_data.get_specific_resource('resource_name'),
        'consumed_per_day': api_data.consumption_per_day(),
        'highest_cost': manipulator.highest_cost_(),
        'lowest_cost': manipulator.lowest_cost(),
        'total_cost': manipulator.total_cost(),
        'earliest_date': manipulator.earliest_date(),
        'latest_date': manipulator.latest_date(),
        'location_statistics': manipulator.location_statistics('location', 'resource_group'),
        'location_map': manipulator.location_map(),

        # Add other methods as needed
    }
    return context
