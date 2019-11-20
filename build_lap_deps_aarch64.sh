#!/bin/bash -l

pushd /usr/projects/artab/users/hpp/spack

COMPILER="gcc@9.2.0"
CONFIG="-C etc/spack/aarch64_gnu"

. share/spack/setup-env.sh

# spack $CONFIG install gcc@9.1.0 % gcc@4.8.5

spack $CONFIG install --no-checksum papi@5.6.0 % $COMPILER
if [ $? -ne 0 ]
then
   echo "papi install failed"
   exit -1
fi

spack $CONFIG install calico@1.7.0 % $COMPILER
if [ $? -ne 0 ]
then
   echo "calico install failed"
   exit -1
fi

spack $CONFIG install cashdsd@16.11.21 build_type=Debug % $COMPILER
if [ $? -ne 0 ]
then
   echo "cashsd install failed"
   exit -1
fi

spack $CONFIG install dsd@1.0.0beta5 build_type=Debug % $COMPILER
if [ $? -ne 0 ]
then
   echo "dsd install failed"
   exit -1
fi

spack $CONFIG install eospac@6.4.0beta.2 % $COMPILER
if [ $? -ne 0 ]
then
   echo "eospac6 install failed"
   exit -1
fi

spack $CONFIG install fftw@3.3.8 % $COMPILER
if [ $? -ne 0 ]
then
   echo "fftw install failed"
   exit -1
fi

spack $CONFIG install gandolf@190807 % $COMPILER
if [ $? -ne 0 ]
then
   echo "gandolf install failed"
   exit -1
fi

spack $CONFIG install gmp@6.1.2 % $COMPILER
if [ $? -ne 0 ]
then
   echo "gmp install failed"
   exit -1
fi

spack $CONFIG install hdf5@1.10.1 % $COMPILER
if [ $? -ne 0 ]
then
   echo "hdf5 install failed"
   exit -1
fi

spack $CONFIG install hypre@2.11.2 % $COMPILER
if [ $? -ne 0 ]
then
   echo "hypre install failed"
   exit -1
fi

spack $CONFIG install ndi@2.2.0 % $COMPILER
if [ $? -ne 0 ]
then
   echo "ndi install failed"
   exit -1
fi

spack $CONFIG install silo@4.10.2-bsd % $COMPILER
if [ $? -ne 0 ]
then
   echo "silo install failed"
   exit -1
fi

spack $CONFIG install rewrite@180313 % $COMPILER
if [ $? -ne 0 ]
then
   echo "rewrite install failed"
   exit -1
fi

spack $CONFIG install parmetis@4.0.3 % $COMPILER
if [ $? -ne 0 ]
then
   echo "parmetis install failed"
   exit -1
fi

spack $CONFIG install intergrid@180717 build_type=Debug % $COMPILER
if [ $? -ne 0 ]
then
   echo "intergrid install failed"
   exit -1
fi

spack $CONFIG install perflib@180621 % $COMPILER
if [ $? -ne 0 ]
then
   echo "perflib install failed"
   exit -1
fi

spack $CONFIG install zoltan@3.8 % $COMPILER
if [ $? -ne 0 ]
then
   echo "zoltan install failed"
   exit -1
fi

spack $CONFIG install r3d@2019-04-24 % $COMPILER
if [ $? -ne 0 ]
then
   echo "r3d install failed"
   exit -1
fi

spack $CONFIG install gandolf@develop % $COMPILER
if [ $? -ne 0 ]
then
   echo "gandolf install failed"
   exit -1
fi

spack $CONFIG install shapo@171108 % $COMPILER
if [ $? -ne 0 ]
then
   echo "shapo install failed"
   exit -1
fi

spack $CONFIG install paraview@5.6.0 % $COMPILER
if [ $? -ne 0 ]
then
   echo "paraview install failed"
   exit -1
fi

spack $CONFIG install eospac5@develop % $COMPILER
if [ $? -ne 0 ]
then
   echo "eospac5 install failed"
   exit -1
fi

