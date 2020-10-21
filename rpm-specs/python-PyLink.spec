%global modname PyLink

Name:           python-PyLink
Version:        0.3.2
Release:        17%{?dist}
Summary:        Universal communication interface using File-Like API

License:        BSD
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        https://pypi.python.org/packages/source/P/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
Pylink offers a universal communication interface using File-Like API. For now,
only the TCP, UDP, Serial and GSM interfaces are supported.

The aim of this project is to allow any type of communication. It is best
suited for projects that have various ways of communicating including IP
remote or local serial communication.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-pylink}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-pyserial

%description -n python3-%{modname}
Pylink offers a universal communication interface using File-Like API. For now,
only the TCP, UDP, Serial and GSM interfaces are supported.

The aim of this project is to allow any type of communication. It is best
suited for projects that have various ways of communicating including IP
remote or local serial communication.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%check
# No network things available

%files -n python3-%{modname}
%license LICENSE
%doc AUTHORS CHANGES.rst README.rst
%{python3_sitelib}/%{modname}*.egg-info/
%{python3_sitelib}/pylink/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.2-10
- Subpackage python2-PyLink has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.2-1
- Initial package
