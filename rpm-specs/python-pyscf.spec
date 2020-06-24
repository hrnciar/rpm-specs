# Omit internal libraries from dependency generation. We can omit all
# the provides
%global __provides_exclude_from ^%{python3_sitearch}/pyscf/lib/.*\\.so$
# but since we still need to pick up the dependencies for libcint,
# libxc, etc, we just have to filter out the internal libraries
%global __requires_exclude ^(libao2mo\\.so|libcgto\\.so|libcvhf\\.so|libfci\\.so|libnp_helper\\.so).*$

Name:           python-pyscf
Version:        1.7.3
Release:        1%{?dist}
Summary:        Python module for quantum chemistry
License:        ASL 2.0
URL:            https://github.com/pyscf/pyscf/
Source0:        https://github.com/pyscf/pyscf/archive/v%{version}/pyscf-%{version}.tar.gz

# Disable rpath
Patch1:         pyscf-1.7.0-rpath.patch

# ppc64 doesn't appear to have floats beyond 64 bits, so ppc64 is
# disabled as per upstream's request as for the libcint package.
ExcludeArch:    %{power64}

BuildRequires:  openblas-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-h5py
BuildRequires:  libxc-devel
BuildRequires:  libcint-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++

# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov

%description
Python‐based simulations of chemistry framework (PySCF) is a
general‐purpose electronic structure platform designed from the ground
up to emphasize code simplicity, so as to facilitate new method
development and enable flexible computational workflows. The package
provides a wide range of tools to support simulations of finite‐size
systems, extended systems with periodic boundary conditions,
low‐dimensional periodic systems, and custom Hamiltonians, using
mean‐field and post‐mean‐field methods with standard Gaussian basis
functions. To ensure ease of extensibility, PySCF uses the Python
language to implement almost all of its features, while
computationally critical paths are implemented with heavily optimized
C routines. Using this combined Python/C implementation, the package
is as efficient as the best existing C or Fortran‐based quantum
chemistry programs.

%package -n python3-pyscf
Summary:        Python 3 module for quantum chemistry
# These are needed at runtime
Requires:  python3-numpy
Requires:  python3-scipy
Requires:  python3-h5py

%description -n python3-pyscf
Python‐based simulations of chemistry framework (PySCF) is a
general‐purpose electronic structure platform designed from the ground
up to emphasize code simplicity, so as to facilitate new method
development and enable flexible computational workflows. The package
provides a wide range of tools to support simulations of finite‐size
systems, extended systems with periodic boundary conditions,
low‐dimensional periodic systems, and custom Hamiltonians, using
mean‐field and post‐mean‐field methods with standard Gaussian basis
functions. To ensure ease of extensibility, PySCF uses the Python
language to implement almost all of its features, while
computationally critical paths are implemented with heavily optimized
C routines. Using this combined Python/C implementation, the package
is as efficient as the best existing C or Fortran‐based quantum
chemistry programs.

%prep
%setup -q -n pyscf-%{version}
%patch1 -p1 -b .rpath

# Remove shebangs
find pyscf -name \*.py -exec sed -i '/#!\/usr\/bin\/env /d' '{}' \;
find pyscf -name \*.py -exec sed -i '/#!\/usr\/bin\/python/d' '{}' \;

%build
cd pyscf/lib
mkdir objdir
cd objdir
%cmake .. -DBUILD_LIBXC=OFF -DENABLE_XCFUN=OFF -DBUILD_XCFUN=OFF -DBUILD_LIBCINT=OFF -DBLAS_LIBRARIES="-lopenblaso" -DCMAKE_SKIP_BUILD_RPATH=1
%make_build

%install
# Package doesn't have an install command, so we do this by hand.
# Install all python sources
for f in $(find pyscf -name \*.py); do
    install -D -p -m 644 $f %{buildroot}%{python3_sitearch}/$f
done
# Install data files (mostly basis sets)
for f in $(find pyscf -name \*.dat); do
    install -D -p -m 644 $f %{buildroot}%{python3_sitearch}/$f
done
# Install compiled libraries
for f in $(find pyscf -name \*.so); do
    install -D -p -m 755 $f %{buildroot}%{python3_sitearch}/$f
done

%check
export PYTHONPATH=$PWD
## While the program has tests, they take forever and won't ever finish
##on the build system.
#pytest

%files -n python3-pyscf
%license LICENSE
%doc CHANGELOG CONTRIBUTING.md FEATURES NOTICE README.md
%{python3_sitearch}/pyscf/

%changelog
* Thu Jun 11 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.3-1
- Update to 1.7.3.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-2
- Rebuilt for Python 3.9

* Thu May 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2.

* Mon Apr 20 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.1-2
- Patch for libxc 5.

* Tue Mar 24 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1.

* Sun Feb 02 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.0-6
- Build against libopenblaso not libopenblas as the latter yields incorrect results.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.0-4
- Switch buildrequire to libcint and disable build on ppc64.

* Thu Jan 23 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.0-3
- Filter provides and requires.

* Wed Jan 22 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.0-2
- Remove shebangs and rpath.

* Tue Jan 07 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.0-1
- First release.
