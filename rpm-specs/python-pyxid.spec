%global modname pyxid
%global commit c84afe985c86b2b8cfa209d3eaf37b6d45fa1763
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        1.1
Release:        0.16.git%{shortcommit}%{?dist}
Summary:        Python library for interfacing with Cedrus XID and StimTracker devices

License:        BSD with advertising
URL:            https://github.com/cedrus-opensource/pyxid
Source0:        https://github.com/cedrus-opensource/pyxid/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
%{summary}.

XID (eXperiment Interface Device) devices are used in software such as
SuperLab, Presentation, and ePrime for receiving input as part of
stimulus/response testing experiments.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
Requires:       python3-pyserial

%description -n python3-%{modname}
%{summary}.

XID (eXperiment Interface Device) devices are used in software such as
SuperLab, Presentation, and ePrime for receiving input as part of
stimulus/response testing experiments.

Python 3 version.

%prep
%autosetup -n %{modname}-%{commit}

%build
%py3_build

%install
%py3_install


%files -n python3-%{modname}
%license COPYING
%doc README.txt
%{python3_sitelib}/%{modname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-0.16.gitc84afe9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.15.gitc84afe9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-0.14.gitc84afe9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-0.13.gitc84afe9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.12.gitc84afe9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.11.gitc84afe9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-0.10.gitc84afe9
- Remove Python 2 subpackage (#1627358)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.9.gitc84afe9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-0.8.gitc84afe9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.7.gitc84afe9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.6.gitc84afe9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.5.gitc84afe9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1-0.4.gitc84afe9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.3.gitc84afe9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.2.gitc84afe9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1-0.1.gitc84afe9
- Initial package
