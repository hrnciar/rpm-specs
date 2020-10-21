# Charliecloud fedora package spec file
#
# Contributors:
#    Dave Love           @loveshack
#    Michael Jennings    @mej
#    Jordan Ogas         @jogas
#    Reid Priedhorksy    @reidpr

# Don't try to compile python3 files with /usr/bin/python.
%{?el7:%global __python %__python3}

Name:          charliecloud
Version:       0.19
Release:       1%{?dist}
Summary:       Lightweight user-defined software stacks for high-performance computing
License:       ASL 2.0
URL:           https://hpc.github.io/%{name}/
Source0:       https://github.com/hpc/%{name}/releases/downloads/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc rsync /usr/bin/python3
Patch0:        lib64.patch
%if 0%{?el7}
Patch1:        el7-pkgdir.patch
%endif

%description
Charliecloud uses Linux user namespaces to run containers with no privileged
operations or daemons and minimal configuration changes on center resources.
This simple approach avoids most security risks while maintaining access to
the performance and functionality already on offer.

Container images can be built using Docker or anything else that can generate
a standard Linux filesystem tree.

For more information: https://hpc.github.io/charliecloud/

%package       doc
Summary:       Charliecloud html documentation
License:       BSD and ASL 2.0
BuildArch:     noarch
Obsoletes:     %{name}-doc < %{version}-%{release}
%if 0%{?el7}
BuildRequires: python36-sphinx
BuildRequires: python36-sphinx_rtd_theme
%else
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
%endif

%description doc
Html and man page documentation for %{name}.

%package   test
Summary:   Charliecloud test suite
License:   ASL 2.0
Obsoletes: %{name}-test < %{version}-%{release}
Requires:  %{name} bash /usr/bin/bats /usr/bin/python3

%description test
Test fixtures for %{name}.

%prep
%setup -q

%patch0 -p1
%if 0%{?el7}
%patch1 -p1
%endif

%build
# Use old inlining behavior, see:
# https://github.com/hpc/charliecloud/issues/735
CFLAGS=${CFLAGS:-%optflags -fgnu89-inline}; export CFLAGS
%configure --docdir=%{_pkgdocdir} \
           --with-python=/usr/bin/python3 \
%if 0%{?el7}
           --with-sphinx-build=%{_bindir}/sphinx-build-3.6
%else
           --with-sphinx-build=%{_bindir}/sphinx-build
%endif

%install
%make_install

cat > README.EL7 <<EOF
For RHEL7 you must increase the number of available user namespaces to a non-
zero number (note the number below is taken from the default for RHEL8):

  echo user.max_user_namespaces=3171 >/etc/sysctl.d/51-userns.conf
  sysctl -p /etc/sysctl.d/51-userns.conf

Note for versions below RHEL7.6, you will also need to enable user namespaces:

  grubby --args=namespace.unpriv_enable=1 --update-kernel=ALL
  reboot

Please visit https://hpc.github.io/charliecloud/ for more information.
EOF

# Remove bundled sphinx bits.
%{__rm} -rf %{buildroot}%{_pkgdocdir}/html/_static/css
%{__rm} -rf %{buildroot}%{_pkgdocdir}/html/_static/fonts
%{__rm} -rf %{buildroot}%{_pkgdocdir}/html/_static/js

# Use Fedora package sphinx bits.
sphinxdir=%{python3_sitelib}/sphinx_rtd_theme/static
ln -s "${sphinxdir}/css"   %{buildroot}%{_pkgdocdir}/html/_static/css
ln -s "${sphinxdir}/fonts" %{buildroot}%{_pkgdocdir}/html/_static/fonts
ln -s "${sphinxdir}/js"    %{buildroot}%{_pkgdocdir}/html/_static/js

# Remove prefix installed license and readme (prefer %license and %doc).
%{__rm} -f %{buildroot}%{_pkgdocdir}/LICENSE
%{__rm} -f %{buildroot}%{_pkgdocdir}/README.rst

%files
%license LICENSE
%doc README.rst %{?el7:README.EL7}
%{_mandir}/man1/ch*
%{_pkgdocdir}/examples

# Library files.
%{_libdir}/%{name}/base.sh
%{_libdir}/%{name}/build.py
%{_libdir}/%{name}/charliecloud.py
%{_libdir}/%{name}/contributors.bash
%{_libdir}/%{name}/misc.py
%{_libdir}/%{name}/version.py
%{_libdir}/%{name}/version.sh
%{_libdir}/%{name}/version.txt

# Binary files.
%{_bindir}/ch-*
%exclude %{_bindir}/ch-test

# Exclude test artifacts
%exclude %{_libexecdir}/%{name}/test

%files doc
%license LICENSE
%{_pkgdocdir}/html

%files test
%license LICENSE
%{_libexecdir}/%{name}/test
%{_bindir}/ch-test
%{_mandir}/man1/ch-test.1*

%changelog
* Tue Sep 22 2020 <jogas@lanl.gov> - 0.19-1
- package build.py and misc.py
- remove unnecessary patch
- New release
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 <jogas@lanl.gov> - 0.15-1
- Add test suite package
- Update spec for autoconf
- New release
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Wed Sep 04 2019 <jogas@lanl.gov> - 0.10-1
- Patch doc-src/conf.py for epel
- Fix doc-src/dev.rst
- Fix libexec and doc install path for 0.10 changes
- Tidy comments
- New release
* Thu Aug 22 2019 <jogas@lanl.gov> - 0.9.10-12
- Upate doc subpackage obsoletes
* Mon Aug 19 2019 Dave love <loveshack@fedoraproject.org> - 0.9.10-11
- Use canonical form for Source0
- remove main package dependency from doc, and make it noarch
* Fri Aug 02 2019 <jogas@lanl.gov> 0.9.10-10
- Tidy comments; fix typo
* Thu Jul 25 2019 <jogas@lanl.gov> 0.9.10-9
- Use python site variable; fix doc file reference
* Tue Jul 23 2019 <jogas@lanl.gov> 0.9.10-8
- Remove bundled js, css, and font bits
* Mon Jul 22 2019 <jogas@lanl.gov 0.9.10-7
- Fix prep section to handle warnings
- Move documentation dependencies to doc package
* Fri Jul 19 2019 <jogas@lanl.gov> 0.9.10-6
- Temporarily remove test suite
* Wed Jul 10 2019 <jogas@lanl.gov> 0.9.10-5
- Revert test and example install path change
- Update test readme
* Wed Jul 3 2019 <jogas@lanl.gov> 0.9.10-4
- Add doc package
* Tue Jul 2 2019 <jogas@lanl.gov> 0.9.10-3
- Tidy comments
- Update source URL
- Build html documentation; add rsync dependency
- Add el7 conditionals for documentation
- Remove libexecdir definition
- Add test suite README.TEST
* Wed May 15 2019  <jogas@lanl.gov> 0.9.10-2
- Fix comment typo
- Move test suite install path
* Tue May 14 2019  <jogas@lanl.gov> 0.9.10-1
- New version
- Fix README.EL7 sysctl command instruction
- Add pre-built html documentation
- Fix python dependency
- Remove temporary test-package readme
- Fixed capitalization of change log messages
* Tue Apr 30 2019  <jogas@lanl.gov> 0.9.9-4
- Move global python declaration
* Mon Apr 29 2019  <jogas@lanl.gov> 0.9.9-3
- Match bin files with wildcard
* Mon Apr 29 2019  <jogas@lanl.gov> 0.9.9-2
- Update macro comment
- Fix release tag history
* Tue Apr 16 2019  <jogas@lanl.gov> 0.9.9-1
- New version
- Move temp readme creation to install segment
- Fix spec file macro
* Tue Apr 02 2019  <jogas@lanl.gov> 0.9.8-2
- Remove python2 build option
* Thu Mar 14 2019  <jogas@lanl.gov> 0.9.8-1
- Add initial Fedora/EPEL package
