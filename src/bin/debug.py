from streamlit.web import bootstrap

real_script = 'src/bin/app.py'
bootstrap.run(real_script, f'debug.py {real_script}', [], {})
