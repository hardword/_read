### gosec fun (osx)

- set `$GOPATH` as recommended:
`$ export GOPATH=$HOME/go`
- install gosec (in `$GOPATH/bin/`): `$ go get github.com/securego/gosec/cmd/gosec/...`
- create and change to project dir: `$ mkdir $GOPATH/pjt && cd $GOPATH/pjt`
- copy your project: `$ git clone ssh://git@bitbucket.com/mypjt/mypjt.git`
- save original `$GOPATH`: `GOPATH_ORG=$GOPATH`
- change `$GOPATH` to project dir: `$ export GOPATH=$GOPATH/pjt/mypjt`

- run `gosec`: `$ $GOPATH_ORG/bin/gosec $GOPATH/src/...`

- dependencies handling
	- get error messages: `$ $GOPATH/../../bin/gosec $GOPATH/src/... 2> ./error`
	- grep dependent packages: `grep -E -o 'cannot find package ".*"' ./error | sort | uniq | cut -d'"' -f2 > ./dep`
	- `go get` them: `oldIFS=$IFS; IFS=$'\n'; for p in $(cat ./dep); do go get $p; done; IFS=$oldIFS`

- run `gosec` again: `$ $GOPATH/../../bin/gosec $GOPATH/src/...`

- set `$GOPATH` to original:
`$ export GOPATH=$GOPATH_ORG` 
