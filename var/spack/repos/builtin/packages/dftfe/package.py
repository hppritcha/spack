# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class Dftfe(CMakePackage):
    """Real-space DFT calculations using Finite Elements"""

    homepage = "https://sites.google.com/umich.edu/dftfe/"
    url = "https://github.com/dftfeDevelopers/dftfe/archive/0.5.1.tar.gz"

    maintainers("rmsds")

    version("1.0.2", sha256="7988938f0b56daa47debd7f5f3909524f71792fe0fb6ce8e9532388871a68178")
    version("0.6.0", sha256="66b633a3aae2f557f241ee45b2faa41aa179e4a0bdf39c4ae2e679a2970845a1")
    version("0.5.2", sha256="9dc4fa9f16b00be6fb1890d8af4a1cd3e4a2f06a2539df999671a09f3d26ec64")
    version("0.5.1", sha256="e47272d3783cf675dcd8bc31da07765695164110bfebbbab29f5815531f148c1")
    version("0.5.0", sha256="9aadb9a9b059f98f88c7756b417423dc67d02f1cdd2ed7472ba395fcfafc6dcb")

    variant(
        "scalapack",
        default=True,
        description="Use ScaLAPACK, strongly recommended for problem sizes >5000 electrons",
    )
    variant(
        "build_type",
        default="Release",
        description="The build type to build",
        values=("Debug", "Release"),
    )
    variant(
        "fp_type"
        default="real",
        description="Floating point type",
        values=("real", "complex"),
    )
    variant(
        "gpu_lang"
        default="none",
        description="GPU language",
        values=("none", "cuda", "hip"),
    )
    variant(
        "gpu_vendor"
        default="none",
        description="GPU vendor",
        values=("none", "amd", "nvidia"),
    )

    variant("dccl", default=False, description="Enable use of DCCL library - GPU builds only")
    variant("testing", default=False, description="Build tests")
    variant("minimal_compile", default=False, description="Select minimal build")
    variant("higherquadpsp", default=False, description="Option to compile with default or higher order quadrature for storing pseudopotential data")
    variant("mdi", default=False, description="Use MDI")

    depends_on("mpi")
    depends_on("dealii+p4est+petsc+slepc+int64+scalapack+mpi")
    depends_on("dealii+p4est+petsc+slepc+int64+scalapack+mpi@9.0.0:", when="@0.5.1:")
    depends_on("scalapack", when="+scalapack")
    depends_on("alglib")
    depends_on("libxc")
    depends_on("spglib")
    depends_on("libxml2")
    depends_on("elpa")

    conflicts("+dccl", when="gpu_lang=none", msg="dccl only supported with GPU builds")

    def cmake_args(self):
        spec = self.spec
        args = [
            "-DCMAKE_CXX_STANDARD=14",
            "-DCMAKE_C_COMPILER={0}".format(spec["mpi"].mpicc),
            "-DCMAKE_CXX_COMPILER={0}".format(spec["mpi"].mpicxx),
            "-DALGLIB_DIR={0}".format(spec["alglib"].prefix),
            "-DLIBXC_DIR={0}".format(spec["libxc"].prefix),
            "-DXML_LIB_DIR={0}/lib".format(spec["libxml2"].prefix),
            "-DXML_INCLUDE_DIR={0}/include".format(spec["libxml2"].prefix),
            "-DSPGLIB_DIR={0}".format(spec["spglib"].prefix),
            "-DDEAL_II_DIR={0}".format(spec["dealii"].prefix),
            "-DCMAKE_SHARED_LINKER_FLAGS={0}".format("-L$MPICH_DIR/lib -lmpich"),
            "-DWITH_GPU_AWARE_MPI=0",
        ]

        if "build_type=Debug" in spec:
            args.append("-DCMAKE_BUILD_TYPE=Debug");
        else
            args.append("-DCMAKE_BUILD_TYPE=Release");

        if "fp_type=real" in spec:
            args.append("-DWITH_COMPLEX=OFF");
        else:
            args.append("-DWITH_COMPLEX=ON");

        if "gpu_lang=cuda" in spec:
            args.append("-DWITH_GPU=1");
            args.append("-DGPU_LANG=cuda");
            args.extend(["-DCMAKE_CUDA_FLAGS=%s" % "-I$MPICH_DIR/include -arch=sm_80"]);
            args.extend(["-DCMAKE_CUDA_ARCHITECTURES=%s" % "-I$MPICH_DIR/include -arch=sm_80"]);
        elif "gpu_lang=hip" in spec:
            args.append("-DWITH_GPU=1");
            args.append("-DGPU_LANG=hip");
        else
            args.append("-DWITH_GPU=0");

        if "gpu_vendor=amd" in spec:
            args.append("-DGPU_VENDOR=amd");
        elif "gpu_vendor=nvidia" in spec:
            args.append("-DGPU_VENDOR=nvidia");

        if "+testing" in spec:
            args.append("-DWITH_TESTING=1")
        else:
            args.append("-DWITH_TESTING=0")

        if "+minimal_compile" in spec:
            args.append("-DMINIMAL_COMPILE=1")
        else:
            args.append("-DMINIMAL_COMPILE=0")

        if "+higherquadpsp" in spec:
            args.append("-DHIGHERQUAD_PSP=1")
        else:
            args.append("-DHIGHERQUAD_PSP=0")

        if "+mdp" in spec:
            # TODO: need to have mdpath included ?
            args.append("-DWITH_MDI=1")
        else:
            args.append("-DWITH_MDI=0")


        if spec.satisfies("^intel-mkl"):
            args.append("-DWITH_INTEL_MKL=ON")
        else:
            args.append("-DWITH_INTEL_MKL=OFF")

        if spec.satisfies("%gcc"):
            args.append("-DCMAKE_C_FLAGS=-fpermissive")
            args.extend(["-DCMAKE_CXX_FLAGS=%s" % "-fpermissive -march=znver3 -fPIC"])
            args.extend(["-DCMAKE_CXX_FLAGS_RELEASE=%s" % "-fPIC -target-accel=nvidia80 -I$MPICH_DIR/include"])

        return args

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.lib64)
        install(join_path(self.build_directory, "main"), join_path(prefix.bin, "dftfe"))
        install(join_path(self.build_directory, "libdftfe.so"), prefix.lib64)
