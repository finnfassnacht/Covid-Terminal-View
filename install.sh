mkdir /usr/bin/py_n_c
cp covid.py /usr/bin/py_n_c/
cd /usr/bin/
touch covid
echo "python3 /usr/bin/py_n_c/covid.py" >> covid
chmod 777 covid
echo "covid has been installed as a command"
echo "open a new terminal and type covid"

