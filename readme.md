#install
sudo apt-get install ipython-notebook python-numpy python-scipy python-pandas python-matplotlib
virtualenv .shadow-env
source .shadow-env/bin/activate 
pip install ipython[notebook] numpy scipy pandas matplotlib scikit-learn

#run
source .shadow-env/bin/activate 
jupyter notebook  # ipython notebook --pylab inline

#stop
deactivate