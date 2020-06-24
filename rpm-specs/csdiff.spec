# python3 is not available on RHEL <= 7
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%else
%bcond_with python3
%endif

# python2 is not available on RHEL > 7 and not needed on Fedora > 29
%if 0%{?rhel} > 7 || 0%{?fedora} > 29
%bcond_with python2
%else
%bcond_without python2
%endif

Name:       csdiff
Version:    1.7.2
Release:    3%{?dist}
Summary:    Non-interactive tools for processing code scan results in plain-text

License:    GPLv3+
URL:        https://github.com/kdudka/csdiff
Source0:    https://github.com/kdudka/csdiff/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: help2man

%description
This package contains the csdiff tool for comparing code scan defect lists in
order to find out added or fixed defects, and the csgrep utility for filtering
defect lists using various filtering predicates. 

%if %{with python2}
%package -n python2-%{name}
Summary:        Python interface to csdiff for Python 2
Conflicts:      %{name} <= 1.2.3
%if 0%{?fedora} > 28
BuildRequires:  boost-python2-devel
%endif
BuildRequires:  python2-devel
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
This package contains the Python 2 binding for the csdiff tool for comparing
code scan defect lists to find out added or fixed defects.

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif
%endif

%if %{with python3}
%package -n python3-%{name}
Summary:        Python interface to csdiff for Python 3
BuildRequires:  boost-python3-devel
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package contains the Python 3 binding for the csdiff tool for comparing
code scan defect lists to find out added or fixed defects.
%endif

%prep
%setup -q

%build
make version.cc
mkdir csdiff_build
cd csdiff_build
%cmake .. -DBUILD_PYCSDIFF=OFF
make %{?_smp_mflags} VERBOSE=yes

%if %{with python2}
mkdir ../csdiff_build_py2
cd ../csdiff_build_py2
%cmake .. -DPYTHON_EXECUTABLE=%{__python2}
make %{?_smp_mflags} VERBOSE=yes
%endif

%if %{with python3}
mkdir ../csdiff_build_py3
cd ../csdiff_build_py3
%cmake .. \
    -DPYTHON_EXECUTABLE=%{__python3} \
    -DBOOST_PYTHON_LIB_NAME=boost_python%{python3_version_nodots}
make %{?_smp_mflags} VERBOSE=yes pycsdiff
%endif

%install
%if %{with python2}
mkdir -vp %{buildroot}%{python2_sitearch}
install -vm0644 csdiff_build_py2/pycsdiff.so %{buildroot}%{python2_sitearch}
%endif

%if %{with python3}
mkdir -vp %{buildroot}%{python3_sitearch}
install -vm0644 csdiff_build_py3/pycsdiff.so %{buildroot}%{python3_sitearch}
%endif

cd csdiff_build
make install DESTDIR="$RPM_BUILD_ROOT"

%check
cd csdiff_build
ctest %{?_smp_mflags} --output-on-failure

%files
%{_bindir}/csdiff
%{_bindir}/csgrep
%{_bindir}/cshtml
%{_bindir}/cslinker
%{_bindir}/cssort
%{_bindir}/cstrans-df-run
%{_mandir}/man1/csdiff.1*
%{_mandir}/man1/csgrep.1*
%{_mandir}/man1/cshtml.1*
%{_mandir}/man1/cslinker.1*
%{_mandir}/man1/cssort.1*
%{_mandir}/man1/cstrans-df-run.1*
%doc COPYING README

%if %{with python2}
%files -n python2-%{name}
%{python2_sitearch}/pycsdiff.so
%doc COPYING
%endif

%if %{with python3}
%files -n python3-%{name}
%{python3_sitearch}/pycsdiff.so
%doc COPYING
%endif

%changelog
* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-3
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-2
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Kamil Dudka <kdudka@redhat.com> 1.7.2-1
- update to latest upstream release

* Tue Mar 31 2020 Kamil Dudka <kdudka@redhat.com> 1.7.1-1
- update to latest upstream release

* Wed Feb 05 2020 Kamil Dudka <kdudka@redhat.com> 1.7.0-1
- update to latest upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Kamil Dudka <kdudka@redhat.com> 1.6.1-1
- make pycsdiff build with Python 3.8 (#1705427)
- update to latest upstream release

* Mon Feb 04 2019 Kamil Dudka <kdudka@redhat.com> 1.6.0-1
- update to latest upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 1.5.0-2
- Rebuilt and patched for Boost 1.69

* Thu Oct 18 2018 Kamil Dudka <kdudka@redhat.com> 1.5.0-1
- update to latest upstream release

* Mon Oct 01 2018 Kamil Dudka <kdudka@redhat.com> 1.4.0-5
- rebuild without the python2-csdiff subpackage (#1634690)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.7

* Thu May 03 2018 Kamil Dudka <kdudka@redhat.com> 1.4.0-1
- update to latest upstream release
- make both python2 and python3 optional

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com> 1.3.3-4
- add explicit BR for the gcc-c++ compiler

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Kamil Dudka <kdudka@redhat.com> 1.3.3-2
- rebuild for Boost 1.66

* Mon Jan 15 2018 Kamil Dudka <kdudka@redhat.com> 1.3.3-1
- update to latest upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-2
- Rebuilt for Boost 1.64

* Wed Feb 15 2017 Kamil Dudka <kdudka@redhat.com> 1.3.2-1
- update to latest upstream release
- update project URL and source URL

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-4
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-3
- Rebuilt for Boost 1.63

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuild for Python 3.6

* Wed Sep 14 2016 Kamil Dudka <kdudka@redhat.com> 1.3.1-1
- update to latest upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 20 2016 Kamil Dudka <kdudka@redhat.com> 1.3.0-1
- update to latest upstream release
- introduce the python2- and python3- subpackages

* Fri May 13 2016 Kamil Dudka <kdudka@redhat.com> 1.2.3-8
- rebuild against latest boost libs to fix linking errors at run time (#1331983)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.2.3-6
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.3-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.2.3-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Kamil Dudka <kdudka@redhat.com> 1.2.3-1
- update to latest upstream release

* Tue Apr 14 2015 Kamil Dudka <kdudka@redhat.com> 1.2.2-2
- rebuild against latest boost (missing symbol _ZN5boost15program_options3argE)

* Wed Apr 01 2015 Kamil Dudka <kdudka@redhat.com> 1.2.2-1
- update to latest upstream release

* Tue Mar 03 2015 Kamil Dudka <kdudka@redhat.com> 1.2.1-1
- update to latest upstream release

* Wed Feb 18 2015 Kamil Dudka <kdudka@redhat.com> 1.2.0-1
- update to latest upstream release

* Thu Feb 05 2015 Kamil Dudka <kdudka@redhat.com> 1.1.4-2
- rebuild for boost 1.57.0

* Wed Jan 28 2015 Kamil Dudka <kdudka@redhat.com> 1.1.4-1
- update to latest upstream release

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.1.3-2
- Rebuild for boost 1.57.0

* Mon Jan 19 2015 Kamil Dudka <kdudka@redhat.com> 1.1.3-1
- update to latest upstream

* Thu Dec 18 2014 Kamil Dudka <kdudka@redhat.com> 1.1.2-1
- update to latest upstream release
- package the pycsdiff python module

* Thu Nov 06 2014 Kamil Dudka <kdudka@redhat.com> 1.1.1-1
- update to latest upstream release

* Fri Sep 19 2014 Kamil Dudka <kdudka@redhat.com> 1.1.0-1
- update to latest upstream release

* Wed Aug 20 2014 Kamil Dudka <kdudka@redhat.com> 1.0.10-1
- update to latest upstream bugfix release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Kamil Dudka <kdudka@redhat.com> 1.0.9-1
- update to latest upstream bugfix release

* Thu Jul 17 2014 Kamil Dudka <kdudka@redhat.com> 1.0.8-1
- update to latest upstream bugfix release

* Thu Jun 19 2014 Kamil Dudka <kdudka@redhat.com> 1.0.6-1
- update to latest upstream bugfix release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.0.4-2
- Rebuild for boost 1.55.0

* Mon Mar 17 2014 Kamil Dudka <kdudka@redhat.com> 1.0.4-1
- update to latest upstream

* Thu Feb 20 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-2
- abandon RHEL-5 compatibility per Fedora Review Request (#1066027)

* Wed Feb 19 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-1
- packaged for Fedora
