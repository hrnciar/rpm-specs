# https://fedoraproject.org/wiki/Packaging:DistTag?rd=Packaging/DistTag#Conditionals
# http://rpm.org/user_doc/conditional_builds.html
%if 0%{?fedora} >= 30
# disabled by default
%bcond_with py2
%else
%bcond_without py2 0
%endif

# No tests included in package
# and since they use versioneer, I'm unable to figure out what git commit this
# release comes from
%bcond_with tests

%global srcname efel

%global desc %{expand: \
The Electrophys Feature Extraction Library (eFEL) allows neuroscientists to
automatically extract features from time series data recorded from neurons
(both in vitro and in silico). Examples are the action potential width and
amplitude in voltage traces recorded during whole-cell patch clamp experiments.
The user of the library provides a set of traces and selects the features to be
calculated. The library will then extract the requested features and return the
values to the user.

The core of the library is written in C++, and a Python wrapper is included. At
the moment we provide a way to automatically compile and install the library as
a Python module.}

Name:           python-%{srcname}
Version:        3.0.66
Release:        4%{?dist}
Summary:        Electrophys Feature Extraction Library

License:        LGPLv3
URL:            http://efel.readthedocs.io/
Source0:        %pypi_source
# Upstream does not include these. Issue filed:
# https://github.com/BlueBrain/eFEL/issues/144
Source1:        https://github.com/BlueBrain/eFEL/raw/master/LICENSE.txt
Source2:        https://github.com/BlueBrain/eFEL/raw/master/LGPL.txt

BuildRequires:  gcc-c++
%{?python_enable_dependency_generator}

%description
%{desc}

%if %{with py2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{desc}
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

cp -v %{SOURCE1} LICENSE
cp -v %{SOURCE2} LGPL

%build
%py3_build

%if %{with py2}
%py2_build
%endif

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
# If, however, we're installing separate executables for python2 and python3,
# the order needs to be reversed so the unversioned executable is the python2 one.
%if %{with py2}
%py2_install
%endif

%py3_install

# Remove headers. We won't provide them here.
rm -rf %{buildroot}/%{python2_sitearch}/%{srcname}/cppcore
rm -rf %{buildroot}/%{python3_sitearch}/%{srcname}/cppcore

%check
%if %{with tests}
%if %{with py2}
%{__python2} setup.py test
%endif
%{__python3} setup.py test
%endif

%if %{with py2}
%files -n python2-%{srcname}
%license LGPL
%doc README.md LICENSE
%{python2_sitearch}/%{srcname}-%{version}-py2.?.egg-info
%{python2_sitearch}/%{srcname}
%endif

%files -n python3-%{srcname}
%license LGPL
%doc README.md LICENSE
%{python3_sitearch}/%{srcname}-%{version}-py3.?.egg-info
%{python3_sitearch}/%{srcname}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.66-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.66-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 31 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.66-1
- Update to 3.0.66

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.58-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.58-1
- Update to 3.0.58

* Wed Apr 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.56-1
- Update to 3.0.56

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.22-1
- Initial build