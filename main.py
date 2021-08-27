try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa
from tfc_client import TFCClient
from tfc_client.enums import (
    RunStatus,
    NotificationTrigger,
    NotificationsDestinationType,
)
from tfc_client.models import VCSRepoModel
import datetime
import os
from pprint import pprint
from dateutil.relativedelta import relativedelta

print('################')
startProgram = datetime.datetime.now()
print(f'[INFO] Program started running at {startProgram}')

URL = os.environ['URL']
TOKEN = os.environ['TOKEN']
MONTHS = int(os.environ['MONTHS'])
ORGANIZATION = os.environ['ORGANIZATION']


def getStartDate(months):
    return datetime.datetime.today() + relativedelta(months=-months)


# Instantiate the client
client = TFCClient(
    url=URL, token=TOKEN)

# Retreive any object type by ID from the client
my_org = client.get("organization", id=ORGANIZATION)


def loopRuns(months, ws):
    successfulAppliesCount = 0
    # To retreive all runs of a workspace:
    for run in ws.runs:
        if run.status == 'applied' and datetime.datetime.strptime(run.attributes['status-timestamps']['applied-at'].split('T')[0], '%Y-%m-%d') > getStartDate(months):
            successfulAppliesCount += 1
    return successfulAppliesCount


def loopWorkspaces(months):
    allWorkspaces = []
    successfulAppliesCountTotal = 0
    counter = 0
    # To retreive all workspaces:
    for ws in my_org.workspaces:
        counter += 1
        successfulAppliesCount = loopRuns(months, ws)
        print(
        f'[INFO] {successfulAppliesCount} successful applies for workspace {ws.name} for the last {months} month(s) | {counter} out of {len(list(my_org.workspaces))} workspaces completed')
        successfulAppliesCountTotal += successfulAppliesCount
        allWorkspaces.append({'workspaceID': ws.id, 'workspaceName': ws.name,
                              'successfulAppliesCount': successfulAppliesCount
                              })
    return allWorkspaces, successfulAppliesCountTotal

allWorkspaces, successfulAppliesCountTotal = loopWorkspaces(MONTHS)

print('[INFO] SUMMARY:')
pprint(allWorkspaces)
pprint({'Totals': {'Total Workspaces': len(allWorkspaces),
                   'successfulAppliesCountTotal': successfulAppliesCountTotal}, 'Period': f"Last {MONTHS} month(s)"})

endProgram = datetime.datetime.now()
print(f'[INFO] Program completed running at {endProgram}')
print(f'[INFO] Program took {endProgram-startProgram} time to run')
