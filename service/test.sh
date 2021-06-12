if [ $# -lt 1 ]; then
        echo 'give 1 argument'
else
        if [ $1 = 'login' ]; then
                curl -H "Content-type: application/json" -X POST -d '{"user_id":"iam","passwd":“1111"}' http://118.67.135.152:8080/login >> ret
        elif [ $1 = 'favorite' ]; then
                curl -H "Content-type: application/json" -X POST -d '{"session_id":"xxxxxxxx"}' http://118.67.135.152:8080/favorite >> ret
        fi
fi

