from setuptools import find_packages,setup


def get_requirements(filepath):

    '''this function helps to extract the data from requirements.txt file'''
    
    requirements=[]

    with open(filepath) as file_obj:

        requirements=file_obj.readlines()

        requirements=[i.replace('\n',' ') for i in requirements]

        if '-e .' in requirements:

            requirements.remove('-e .')
    
    return requirements

setup(

    name='practice',
    
    version='0.0.1',

    packages=find_packages(),

    install_requires=get_requirements('requirements.txt')
    
)
