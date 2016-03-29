from setuptools import setup

# Get the long description by reading the README
try:
    readme_content = open("README.md").read()
except:
    readme_content = ""

setup(name='lambda_sample_events',
      version='1.0.0',
      description='Python module for creating sample events to test AWS Lambda functions.',
      long_description=readme_content,
      url='https://github.com/irlrobot/python_lambda_sample_events',
      author='Josh Campbell',
      author_email='josh@userdel.com',
      maintainer='Josh Campbell',
      maintainer_email='josh@userdel.com',
      license='Apache 2.0',
      keywords=["aws", "lambda"],
      packages=['lambda_sample_events'],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
      ],
      include_package_data=True,
      tests_require=['pytest'],
      zip_safe=False)
