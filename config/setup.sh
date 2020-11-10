# Update and upgrade linux package requirements
sudo apt-get update && sudo apt-get upgrade
echo "Successfully installed updated package list"

# Install git if not already installed
sudo apt install git
echo "Successfully installed git"

# Install conda (change link to most recent version)
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
bash Anaconda3-2020.07-Linux-x86_64.sh
rm Anaconda3-2020.07-Linux-x86_64.sh
echo "export PATH=~/anaconda3/bin:\$PATH" >> ~/.bashrc
echo "Successfully installed Conda for linux version: $(conda -V)"

# Create conda envs
conda env create -f all_purpose_ml.yml
conda env create -f sci_informatics.yml
conda env create -f web_dev.yml
echo "Successfully created the following environments: $(conda env list)"

# Install zsh and oh-my-zsh
sudo apt install zsh
echo "Successfully installed zsh version $(zsh --version)"
# Optionally, you can make zsh the default shell with chsh -s $(which zsh) and check with $(echo $SHELL)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install tmux and associated packages
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
cat "set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'

# Other examples:
# set -g @plugin 'github_username/plugin_name'
# set -g @plugin 'git@github.com:user/plugin'
# set -g @plugin 'git@bitbucket.com:user/plugin'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'" >> ~/.tmux.conf
tmux source ~/.tmux.conf
# To add a new plugin, use set -g @plugin '...' and hit prefix-key + I to install
echo "set -g @plugin 'tmux-plugins/tmux-resurrect'" >> ~/.tmux.conf
echo "Successfully installed tmux (version: $(tmux -V)) and plugins"
