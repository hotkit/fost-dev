from configuration import *

FROM = ARGS.pop(0)
WITH = ARGS.pop(0)
def compare():
    for project, folder, configuration in projects():
        for lib in configuration.get('libs', []):
            print('{} {}'.format(project, lib))
            execute('diff', os.path.join(FROM, folder, lib, "ChangeLog"),
                os.path.join(WITH, folder, lib, "ChangeLog"))

ACTIONS.append(compare)
