%undefine __cmake_in_source_build

Name:       csmock
Version:    2.6.0
Release:    1%{?dist}
Summary:    A mock wrapper for Static Analysis tools

License:    GPLv3+
URL:        https://github.com/kdudka/%{name}
Source0:    https://github.com/kdudka/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: help2man

%if !(0%{?fedora} >= 19 || 0%{?rhel} >= 7)
BuildRequires: python-argparse
BuildRequires: python-importlib
%endif

# force using Python 3 Fedora 23+
%global force_py3 ((7 < 0%{?rhel}) || (22 < 0%{?fedora}))
%if %{force_py3}
BuildRequires: python3-GitPython
BuildRequires: python3-devel
%global csmock_python_executable %{__python3}
%global csmock_python_sitelib %{python3_sitelib}
%else
BuildRequires: GitPython
BuildRequires: python2-devel
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif
%global csmock_python_executable %{__python2}
%global csmock_python_sitelib %{python2_sitelib}
%endif

Requires: csmock-common                 >= %{version}-%{release}
Requires: csmock-plugin-clang           >= %{version}-%{release}
Requires: csmock-plugin-cppcheck        >= %{version}-%{release}
Requires: csmock-plugin-shellcheck      >= %{version}-%{release}

BuildArch: noarch

%description
This is a metapackage pulling in csmock-common and basic csmock plug-ins.

%package -n csbuild
Summary: Tool for plugging static analyzers into the build process
%if %{force_py3}
Requires: csmock-common(python3)
Requires: python3-GitPython
%else
Requires: GitPython
%endif
Requires: cscppc
Requires: csclng
Requires: csdiff >= 1.5.0
Requires: cswrap
Requires: csmock-common > 2.1.1

%description -n csbuild
Tool for plugging static analyzers into the build process, free of mock.

%package -n csmock-common
Summary: Core of csmock (a mock wrapper for Static Analysis tools)
Requires: csdiff > 1.8.0
Requires: csgcca
Requires: cswrap >= 1.3.1
Requires: mock
%if !(0%{?fedora} >= 19 || 0%{?rhel} >= 7)
Requires: python-argparse
Requires: python-importlib
%endif
%if %{force_py3}
Provides: csmock-common(python3) = %{version}-%{release}
%endif

%description -n csmock-common
This package contains the csmock tool that allows to scan SRPMs by Static
Analysis tools in a fully automated way.

%package -n csmock-plugin-bandit
Summary: csmock plug-in providing the support for Bandit.
Requires: csmock-common >= 1.8.0
%if %{force_py3}
Requires: csmock-common(python3)
%endif

%description -n csmock-plugin-bandit
This package contains the bandit plug-in for csmock.

%package -n csmock-plugin-clang
Summary: csmock plug-in providing the support for Clang
Requires: csclng
Requires: csmock-common >= 1.7.1
%if %{force_py3}
Requires: csmock-common(python3)
%endif

%description -n csmock-plugin-clang
This package contains the clang plug-in for csmock.

%package -n csmock-plugin-cppcheck
Summary: csmock plug-in providing the support for Cppcheck
Requires: cscppc >= 1.0.4
Requires: csmock-common
%if %{force_py3}
Requires: csmock-common(python3)
%endif

%description -n csmock-plugin-cppcheck
This package contains the cppcheck plug-in for csmock.

%package -n csmock-plugin-pylint
Summary: csmock plug-in providing the support for Pylint.
Requires: csmock-common >= 1.8.0
%if %{force_py3}
Requires: csmock-common(python3)
%endif

%description -n csmock-plugin-pylint
This package contains the pylint plug-in for csmock.

%package -n csmock-plugin-shellcheck
Summary: csmock plug-in providing the support for ShellCheck.
Requires: csmock-common >= 1.8.0
%if %{force_py3}
Requires: csmock-common(python3)
%endif

%description -n csmock-plugin-shellcheck
This package contains the shellcheck plug-in for csmock.

%package -n csmock-plugin-smatch
Summary: csmock plug-in providing the support for smatch
Requires: csdiff > 1.4.0
Requires: csmatch
Requires: csmock-common
Requires: cswrap > 1.4.0
%if %{force_py3}
Requires: csmock-common(python3)
%endif

%description -n csmock-plugin-smatch
This package contains the smatch plug-in for csmock.

%prep
%setup -q

# force using Python 3 Fedora 23+
%if %{force_py3}
sed -e '1s/python$/python3/' -i py/cs{build,mock}
%endif

%build
%cmake \
    -DVERSION='%{name}-%{version}-%{release}' \
    -DPYTHON_EXECUTABLE='%{csmock_python_executable}' \
    %{nil}
%cmake_build

%install
%cmake_install

# needed to create the csmock RPM
%files

%files -n csbuild
%{_bindir}/csbuild
%{_mandir}/man1/csbuild.1*
%{_datadir}/csbuild/scripts/run-scan.sh
%doc COPYING

%files -n csmock-common
%dir %{_datadir}/csmock
%dir %{_datadir}/csmock/scripts
%dir %{csmock_python_sitelib}/csmock
%dir %{csmock_python_sitelib}/csmock/plugins
%{_bindir}/csmock
%{_mandir}/man1/csmock.1*
%{_datadir}/csmock/cwe-map.csv
%{_datadir}/csmock/scripts/chroot-fixups
%{_datadir}/csmock/scripts/patch-rawbuild.sh
%{csmock_python_sitelib}/csmock/__init__.py*
%{csmock_python_sitelib}/csmock/common
%{csmock_python_sitelib}/csmock/plugins/__init__.py*
%{csmock_python_sitelib}/csmock/plugins/gcc.py*
%if %{force_py3}
%{csmock_python_sitelib}/csmock/__pycache__/__init__.*
%{csmock_python_sitelib}/csmock/plugins/__pycache__/__init__.*
%{csmock_python_sitelib}/csmock/plugins/__pycache__/gcc.*
%endif
%doc COPYING README

%files -n csmock-plugin-bandit
%{_datadir}/csmock/scripts/run-bandit.sh
%{csmock_python_sitelib}/csmock/plugins/bandit.py*
%if %{force_py3}
%{csmock_python_sitelib}/csmock/plugins/__pycache__/bandit.*
%endif

%files -n csmock-plugin-clang
%{csmock_python_sitelib}/csmock/plugins/clang.py*
%if %{force_py3}
%{csmock_python_sitelib}/csmock/plugins/__pycache__/clang.*
%endif

%files -n csmock-plugin-cppcheck
%{csmock_python_sitelib}/csmock/plugins/cppcheck.py*
%if %{force_py3}
%{csmock_python_sitelib}/csmock/plugins/__pycache__/cppcheck.*
%endif

%files -n csmock-plugin-pylint
%{_datadir}/csmock/scripts/run-pylint.sh
%{csmock_python_sitelib}/csmock/plugins/pylint.py*
%if %{force_py3}
%{csmock_python_sitelib}/csmock/plugins/__pycache__/pylint.*
%endif

%files -n csmock-plugin-shellcheck
%{_datadir}/csmock/scripts/run-shellcheck.sh
%{csmock_python_sitelib}/csmock/plugins/shellcheck.py*
%if %{force_py3}
%{csmock_python_sitelib}/csmock/plugins/__pycache__/shellcheck.*
%endif

%files -n csmock-plugin-smatch
%{csmock_python_sitelib}/csmock/plugins/smatch.py*
%if %{force_py3}
%{csmock_python_sitelib}/csmock/plugins/__pycache__/smatch.*
%endif

%changelog
* Tue Oct 20 2020 Kamil Dudka <kdudka@redhat.com> 2.6.0-1
- update to latest upstream release

* Wed Aug 19 2020 Kamil Dudka <kdudka@redhat.com> 2.5.0-1
- update to latest upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.9

* Wed Feb 05 2020 Kamil Dudka <kdudka@redhat.com> 2.4.0-1
- update to latest upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kamil Dudka <kdudka@redhat.com> 2.3.0-1
- update to latest upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Kamil Dudka <kdudka@redhat.com> 2.2.1-1
- update to latest upstream release

* Thu Oct 18 2018 Kamil Dudka <kdudka@redhat.com> 2.2.0-1
- update to latest upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-2
- Rebuilt for Python 3.7

* Thu May 03 2018 Kamil Dudka <kdudka@redhat.com> 2.1.1-1
- update to latest upstream release
- introduce the experimental bandit plug-in

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Kamil Dudka <kdudka@redhat.com> 2.1.0-1
- update to latest upstream release

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.4-3
- Build require Python 2 only when needed

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kamil Dudka <kdudka@redhat.com> 2.0.4-1
- update to latest upstream release

* Wed Feb 15 2017 Kamil Dudka <kdudka@redhat.com> 2.0.3-1
- update to latest upstream release
- update project URL and source URL

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-2
- Rebuild for Python 3.6

* Wed Nov 30 2016 Kamil Dudka <kdudka@redhat.com> 2.0.2-1
- update to latest upstream

* Wed Sep 14 2016 Kamil Dudka <kdudka@redhat.com> 2.0.1-1
- update to latest upstream

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 20 2016 Kamil Dudka <kdudka@redhat.com> 2.0.0-1
- update to latest upstream
- force using Python 3

* Thu Apr 28 2016 Kamil Dudka <kdudka@redhat.com> 1.9.2-1
- update to latest upstream

* Mon Mar 21 2016 Kamil Dudka <kdudka@redhat.com> 1.9.1-1
- update to latest upstream

* Wed Feb 03 2016 Kamil Dudka <kdudka@redhat.com> 1.9.0-1
- update to latest upstream

* Thu Jul 23 2015 Kamil Dudka <kdudka@redhat.com> 1.8.3-1
- update to latest upstream

* Mon Jul 13 2015 Kamil Dudka <kdudka@redhat.com> 1.8.2-1
- update to latest upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Kamil Dudka <kdudka@redhat.com> 1.8.1-1
- update to latest upstream

* Wed Apr 01 2015 Kamil Dudka <kdudka@redhat.com> 1.8.0-1
- update to latest upstream

* Tue Mar 03 2015 Kamil Dudka <kdudka@redhat.com> 1.7.2-1
- update to latest upstream

* Wed Feb 25 2015 Kamil Dudka <kdudka@redhat.com> 1.7.1-1
- update to latest upstream

* Wed Feb 18 2015 Kamil Dudka <kdudka@redhat.com> 1.7.0-1
- update to latest upstream

* Mon Jan 19 2015 Kamil Dudka <kdudka@redhat.com> 1.6.1-1
- update to latest upstream

* Wed Dec 17 2014 Kamil Dudka <kdudka@redhat.com> 1.6.0-1
- update to latest upstream (introduces the csbuild subpackage)

* Thu Dec 11 2014 Michael Scherer <misc@zarb.org> 1.5.1-2
- fix the description of the csmock-plugin-shellcheck subpackage (#1173134)

* Thu Nov 06 2014 Kamil Dudka <kdudka@redhat.com> 1.5.1-1
- update to latest upstream

* Fri Sep 19 2014 Kamil Dudka <kdudka@redhat.com> 1.5.0-1
- update to latest upstream

* Fri Sep 05 2014 Kamil Dudka <kdudka@redhat.com> 1.4.1-1
- update to latest upstream

* Wed Sep 03 2014 Kamil Dudka <kdudka@redhat.com> 1.4.0-1
- update to latest upstream

* Wed Aug 20 2014 Kamil Dudka <kdudka@redhat.com> 1.3.2-1
- update to latest upstream

* Fri Aug 01 2014 Kamil Dudka <kdudka@redhat.com> 1.3.1-1
- update to latest upstream
- install plug-ins to %%{python2_sitelib} instead of %%{python_sitearch}

* Thu Jul 17 2014 Kamil Dudka <kdudka@redhat.com> 1.2.3-1
- update to latest upstream

* Fri Jul 04 2014 Kamil Dudka <kdudka@redhat.com> 1.2.2-1
- update to latest upstream

* Thu Jun 19 2014 Kamil Dudka <kdudka@redhat.com> 1.1.1-1
- update to latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Kamil Dudka <kdudka@redhat.com> 1.0.7-1
- update to latest upstream

* Tue Feb 25 2014 Kamil Dudka <kdudka@redhat.com> 1.0.3-2
- further spec file improvements per Fedora Review Request (#1066029)

* Mon Feb 24 2014 Kamil Dudka <kdudka@redhat.com> 1.0.3-1
- update to new upstream release
- abandon RHEL-5 compatibility per Fedora Review Request (#1066029)

* Wed Feb 19 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-1
- packaged for Fedora
