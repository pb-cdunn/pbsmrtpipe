qsub -pe smp ${NPROC} -S /bin/bash -V -q default -N ${JOB_ID} \
    -o ${STDOUT_FILE}\
    -e ${STDERR_FILE}\
    ${CMD}