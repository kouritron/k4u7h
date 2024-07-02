alias xpp='export PYTHONPATH=$(pwd) && echo "PYTHONPATH now:" && echo $PYTHONPATH'
alias nmbin='export PATH=$(npm bin):$PATH'

alias gst='git status'
alias ga='git add '
alias gc='git commit -m '
alias gpl='git pull'
alias gpsh='git push'


# ----- clear screen
alias cls='clear'

# ----- repo root
alias cdrrt='cd $(git rev-parse --show-toplevel)'


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----- we can abuse this file a bit for non-login shell as its sourced by bashrc

export PS1="\$? $ "


