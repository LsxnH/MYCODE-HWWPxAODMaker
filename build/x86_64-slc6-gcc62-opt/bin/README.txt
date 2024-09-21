Here, we show how to run (with higgs production role) a grid job production.

First, set up everything according to:
https://twiki.cern.ch/twiki/bin/view/AtlasProtected/HWWxAODCode#1_Setup

Second, make sure that you can run successfully on a local test sample (even the
grid job submission requires this local sample to be present).

Thirds, set up the grid environment. On the same shell that you ran the athena
HWW job, load the panda client setup and get a valid grid proxy (assuming you
have a valid grid certificate). The one shown here assumes you have higgs group
roles. You don't really need that. But if you don't have this, then your output
will be names user.USERNAME... instead of group.phys-higgs... and it won't be
stored on a higgs group disk space.

localSetupPandaClient
voms-proxy-init --voms atlas:/atlas/phys-higgs/Role=production

Then, go to the run directory that we described before:

cd $TestArea/run


In order to get familiar with the grid submission script
(which is in: PhysicsxAODConfig/scripts/submitGridJobs.py)
let's first see what options are available:

submitGridJobs.py --help


To decide that you want to run on a range of dataset IDs, you can run this command:

submitGridJobs.py --inDSIDs 110070-110075,167740-167757,167923


Note that the above command will NOT submit actual grid jobs! It will just print
to the screen which submission commands it would run.
Also, note that by default, you would run a TEST job, i.e., the output dataset
name would get a different version suffix, for example, the suffix ".v4" would
become the suffix ".TEST_v4".
To get rid of this testing behavior, add the --prod option:

submitGridJobs.py --inDSIDs 110070-110075,167740-167757,167923 --prod

If you have higgs group rights, you can in addition use the
--official
option. That way, the output will be named group.phys-higgs... instead of user.USERNAME...
and it will be stored on a higgs group disk space.

In case you want to run over all listed datasets, you can simply omit the --inDSIDs, e.g.:

submitGridJobs.py --prod


The default submission mode is to run only the nominal jobs, i.e., without
calculating systematic variations. If you want to run with systematic variations
calculated, add the -s option (or --doSystematics). That way, also the suffix
'sys' will be added to the version name.

submitGridJobs.py --prod --doSystematics


If you have many jobs to submit and you don't want to wait that long, you can
try to use the multiprocessing feature to submit jobs in parallel. Note that you
should NOT set the number of processes that run simultaneously too high.
The default 0 means that no multiprocessing is attempted.
Let's start trying with 10, e.g.:

submitGridJobs.py --prod --nProcs 10


ONLY IF YOU ARE FULLY SATISFIED WITH WHAT YOU SEE, you can go ahead and actually
submit the grid jobs. For this, add the additional flag: --run

submitGridJobs.py --inDSIDs 110070-110075,167740-167757,167923 --prod --run
