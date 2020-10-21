Name:           uflash
Version:        1.2.1
Release:        8%{?dist}
Summary:        A module and utility to flash Python onto the BBC micro:bit
License:        MIT
URL:            https://github.com/ntoll/uflash
Source0:        %pypi_source

# For tests, they don't have tags
%define hash    d493b9f027e65a2551bb46407432723b73cf78b4
Source1:        https://github.com/ntoll/uflash/archive/%{hash}.tar.gz
BuildRequires:  python3-pytest

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nudatus

Requires:       python3-setuptools
Recommends:     python3-nudatus

BuildArch:      noarch

# Other tools are using this as a module, so provide also the python3- name
Provides:       python3-%{name} == %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description
A utility for flashing the BBC micro:bit with Python scripts and the
MicroPython runtime. You pronounce the name of this utility "micro-flash". ;-)
It provides two services. A library of functions to programatically create a
hex file and flash it onto a BBC micro:bit.  A command line utility called
uflash that will flash Python scripts onto a BBC micro:bit.


%prep
%setup -q


%build
%py3_build

%install
%py3_install

%check
tar -xf %{SOURCE1}
mv %{name}-%{hash}/tests .
rm -rf %{name}-%{hash}

py.test-3 -vv

%files
%doc README.rst CHANGES.rst
%license LICENSE
%{_bindir}/uflash
%{python3_sitelib}/uflash*
%{python3_sitelib}/__pycache__/uflash*



%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-7
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-1
- Update to 1.2.1 (#1605196)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-1
- Update to 1.2.0 (#1594545)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-4
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-3
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-2
- BR and recommend nudatus

* Tue Apr 10 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-1
- Update to 1.1.2
- Provide python3-uflash

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuild for Python 3.6

* Tue Aug 16 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-1
- Update to 1.0.3
- Use new %%py3_ macros for build and install
- Update source URL
- Include LICENSE and CHANGES.rst
- Require setuptools for entrypoints
- Add tests

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18b0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jan 18 2016 Kushal Das <kushal@fedoraprojects.org> - 0.9.18b0-1
- Initial package creation
