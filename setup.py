from setuptools import setup

setup(name='aws_lambda_sample_events',
      version='1.0.1',
      description='A Python module for creating sample events to test AWS Lambda functions.',
      long_description='See README.md in source.',
      url='https://github.com/awslabs/aws_lambda_sample_events_python',
      author='Amazon Web Services',
      maintainer='Josh Campbell',
      maintainer_email='joshcb@amazon.com',
      license='Apache 2.0',
      keywords=["aws", "lambda"],
      packages=['aws_lambda_sample_events'],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
      ],
      include_package_data=True,
      tests_require=['pytest'],
      zip_safe=False)
