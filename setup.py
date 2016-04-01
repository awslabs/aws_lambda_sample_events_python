from setuptools import setup

setup(name='aws_lambda_sample_events',
      version='1.0.0',
      description='A Python module for creating sample events to test AWS Lambda functions.',
      long_description='See README.md in source.',
      url='https://github.com/irlrobot/aws_lambda_sample_events_python',
      author='Josh Campbell',
      author_email='joshcb@amazon.com',
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
