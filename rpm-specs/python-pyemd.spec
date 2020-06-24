# https://fedoraproject.org/wiki/Packaging:DistTag?rd=Packaging/DistTag#Conditionals
# http://rpm.org/user_doc/conditional_builds.html
%if 0%{?fedora} >= 30
# disabled by default
%bcond_with py2
%else
%bcond_without py2 0
%endif

%bcond_without tests

%global srcname pyemd

%global desc %{expand: \
PyEMD is a Python wrapper for Ofir Pele and Michael Werman’s implementation of
the Earth Mover’s Distance that allows it to be used with NumPy. If you use
this code, please cite the papers listed in the README.rst file.}

Name:           python-%{srcname}
Version:        0.5.1
Release:        7%{?dist}
Summary:        Fast EMD for Python


License:        MIT
URL:            https://github.com/wmayner/%{srcname}
Source0:        %pypi_source

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
%{desc}

%if %{with py2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  %{py2_dist Cython}
BuildRequires:  %{py2_dist pytest}
BuildRequires:  %{py2_dist numpy}
Requires:       %{py2_dist numpy}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{desc}
%endif

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  %{py3_dist Cython}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}
Requires:       %{py3_dist numpy}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
rm -rf .eggs

# Remove unneeded shebangs
sed -i '/^#!\/usr\/bin\/env python3/ d' pyemd/__about__.py
sed -i '/^#!\/usr\/bin\/env python3/ d' pyemd/__init__.py

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

%check
%if %{with tests}
# Remove this stuff so that the installed copy is used for tests
rm -rf %{srcname} %{srcname}.egg-info
%if %{with py2}
export PYTHONPATH=%{buildroot}/%{python2_sitearch}
pytest-%{python2_version} test
%endif

export PYTHONPATH=%{buildroot}/%{python3_sitearch}
pytest-%{python3_version} test
%endif

%if %{with py2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitearch}/%{srcname}
%{python2_sitearch}/%{srcname}-%{version}-py2.?.egg-info
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py3.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.1-1
- Initial package
- use {buildroot}
- BRs one per line
