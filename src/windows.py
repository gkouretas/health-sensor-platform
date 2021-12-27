from typing import NewType
import tools
from buttons import *

def createHome(root):
    home = tools.Window(root, 450, 450)
    
    title = 'Health Sensor UI'

    home.createWindow(
        title=title,
        size='450x450', 
        resize=[True, True])

    home.createGrid(
        rows={'count': 4,
              'weight': [1, 1, 1, 1]},
        cols={'count': 1,
              'weight': [1]},
        orientation='single'
    )

    home.windowBody(
        main=('Health Sensor UI', (0,0)),
        body=('This is a description', (0,1)),
    )

    home.addButton(
        name='New User',
        pos=(0,2),
        color='blue',
        command=newUser,
        args=[home],
        wait=False
    )

    home.addButton(
        name='Existing User',
        pos=(0,3),
        color='blue',
        command=newUser,
        args=[home],
        wait=False
    )

def createUser(new_user):
    title = 'Health Sensor UI'

    new_user.createFrame(
        orientation='half'
    )

    new_user.createGrid(
        rows={'count': 5,
              'weight': [1, 1, 1, 1, 1]},
        cols={'count': 3,
              'weight': [1, 1, 1]},
        orientation='single'
    )

    new_user.createGrid(
        rows={'top': 
                {
                    'count': 4,
                    'weight': [1, 1, 1, 1]
                },
              'bottom':
                {
                   'count': 1,
                   'weight': [1] 
                }
             },
        cols={'top': 
                {
                'count': 2,
                'weight': [1, 1]
                },
              'bottom':
                {
                   'count': 3,
                   'weight': [1, 1, 1] 
                }
             },
        orientation='half'
    )

    new_user.windowBody(
        main=None,
        body=('First Name', (0,0)),
        frame='top'
    )

    new_user.windowBody(
        main=None,
        body=('Last Name', (0,1)),
        frame='top'
    )

    new_user.windowBody(
        main=None,
        body=('Gender', (0,2)),
        frame='top'
    )

    new_user.windowBody(
        main=None,
        body=('Age', (0,3)),
        frame='top'
    )

    new_user.addButton(
        name='Submit',
        pos=(1,0),
        color='blue',
        command=newUser,
        args=[new_user],
        frame='bottom',
        wait=False
    )
