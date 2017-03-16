pipeline {
  agent {
    node {
      label 'naf'
    }
    
  }
  stages {
    stage('Preparation') {
      steps {
        echo 'Start with preparations'
        mattermostSend(message: 'Start with preparations', channel: 'harrendorf-devel', icon: 'https://wiki.jenkins-ci.org/download/attachments/2916393/headshot.png?version=1&modificationDate=1302753947000')
      }
    }
    stage('Start script') {
      steps {
        echo 'Start script'
        node(label: 'naf') {
          catchError() {
            sh '''#!/bin/zsh -l

#--------------------------------------------------------------------------------

# Variables
export JENKINSUSERDIR=$USERNAME
export JENKINSWORKDIR="/nfs/dust/cms/user/"$JENKINSUSERDIR"/jenkins/ntuple_conversion"
echo $JENKINSWORKDIR
export JENKINSVIRTUALENVDIR="python_virtualenv"
echo $JENKINSVIRTUALENVDIR


# clean old virtual environment before creating new one
mkdir -p $JENKINSWORKDIR
cd $JENKINSWORKDIR
rm -rf $JENKINSVIRTUALENVDIR


# create virtual environment
module load python
module load root
virtualenv --system-site-packages $JENKINSVIRTUALENVDIR
source $JENKINSVIRTUALENVDIR/bin/activate
pip install rootpy
NOTMVA=1 pip2 install --upgrade root_numpy

#--------------------------------------------------------------------------------
'''
          }
          
        }
        
      }
    }
    stage('Deploy') {
      steps {
        echo 'Finishing...'
        mattermostSend(message: 'Finished with jog', channel: 'harrendorf-devel', color: 'green')
      }
    }
  }
}
