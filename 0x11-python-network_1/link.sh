
    sudo apt-get -y install expect

    git config --global user.email findtamilore
    git config --global user.name tami-cp0
    git config --global credential.helper store

    username=$"$1"
    repository=$"$2"
    personal_token=$"$3"

    git clone "https://github.com/$username/$repository.git" && wait
    touch "$repository/test" && echo "test file created"

    function push() {
        git add "$1" && git commit -a -m "$2" && git push
    }

    
    cd "$repository" && wait
    # Run expect script
expect << SCRIPT
    spawn bash
    expect "$ "
    send "push 'test' 'testing'\r"
    expect "Username:"
    send "$username\r"
    expect "Password:"
    send "$personal_token\r"
    expect "$ "
    send "rm test\r"
    send "push 'test' 'remove test file'\r"
    send "exit\r"
    expect eof
SCRIPT
    echo "\n[100%] Git Setup Complete..."