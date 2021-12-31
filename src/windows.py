from typing import NewType
import tools
import os
from callbacks import *

def createHome(root):
    home = tools.Window(root, 450, 450)
    
    title = 'Health Sensor UI'

    home.createWindow(
        title=title,
        size='900x900', 
        resize=[True, True])

    home.createGrid(
        rows={'count': 4,
              'weight': [1, 1, 1, 1]},
        cols={'count': 1,
              'weight': [1]},
        orientation='single'
    )

    home.addLabel(
        text='Health Sensor UI', 
        coords=(0,0),
        head=True
    )
    
    home.addLabel(
        text='This is a description',
        coords=(0,1),
    )

    home.addButton(
        name='New User',
        pos=(0,2),
        color='blue',
        command=newUser,
        args=[home],
        wait=False
    )

    users = [user for user in os.listdir("./users")]
    if users: 
        home.addButton(
            name='Existing User',
            pos=(0,3),
            color='blue',
            command=existingUser,
            args=[home],
            wait=False
        )

def createUserPage(new_user):
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
                    'count': 5,
                    'weight': [1, 1, 1, 1, 1]
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

    new_user.addLabel(
        text='First Name',
        coords=(0,0),
        frame='top'
    )

    new_user.addLabel(
        text='Last Name',
        coords=(0,1),
        frame='top'
    )

    new_user.addLabel(
        text='Age', 
        coords=(0,2),
        frame='top'
    )

    new_user.addLabel(
        text='Gender', 
        coords=(0,3),
        frame='top'
    )

    new_user.addLabel(
        text='Ethnicity', 
        coords=(0,4),
        frame='top'
    )

    for i in range(3):
        new_user.addEntry(
            coords=(1,i),
            frame='top'
        )

    new_user.addDropDown(
        coords=(1,3),
        items=['Male', 'Female', 'Do not wish to specify'],
        frame='top',
        cmd=getGender
    )

    new_user.addDropDown(
        coords=(1,4),
        items=[
            'Black',
            'Chinese',
            'Indian',
            'White',
            'Mixed/multiple ethnic groups',
            'Other ethnic group'
        ],
        frame='top',
        cmd=getEthnicity
    )

    new_user.addButton(
        name='Submit',
        pos=(1,0),
        color='blue',
        command=addUser,
        args=[new_user],
        frame='bottom',
        wait=False
    )

def createExistingUserPage(existing_user):
    users = [user for user in os.listdir("./users")]
    existing_user.createGrid(
        rows={'count': 3,
              'weight': [1, 1, 1]},
        cols={'count': 1,
              'weight': [1]},
        orientation='single'
    )

    existing_user.addLabel(
        text='Select User',
        coords=(0,0)
    )

    existing_user.addDropDown(
        coords=(0,1),
        items=users,
        cmd=placeholder
    )

    existing_user.addButton(
        name='Submit',
        pos=(0,2),
        color='blue',
        command=placeholder,
        args=[existing_user],
        wait=False
    )

