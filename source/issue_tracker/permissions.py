def is_project_member(user, project):
    return project.users.filter(pk=user.pk).exists()

def is_manager(user):
    return user.groups.filter(name='Project Manager').exists()

def is_lead(user):
    return user.groups.filter(name='Team Lead').exists()

def is_developer(user):
    return user.groups.filter(name='Developer').exists()