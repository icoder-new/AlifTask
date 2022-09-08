from cli import cli

# In this case checks like if __name__ == '__main__' are useless
# Why? Because __main__ module starts only when package started as program directly from python.exe
# For example:
#       $ python package_name
#
# So, call cli() for starting our CLI interface.
cli()
