# Application Import:
from ..models import Scheduler

def scheduler_creator():
    # Collect all schedules:
    schedules = Scheduler.objects.all()
    # All schedules dictionary:
    schedules_dict = {}

    # Iterate thru all schedules:
    for schedule in schedules:
        # Single schedule dictionary:
        schedule_dict = {}
        schedule_dict['task'] = 'management.tasks.active_devices_check'
        schedule_dict['task'] = schedule.seconds
        schedules_dict[schedule.name] = schedule_dict

    return schedules_dict