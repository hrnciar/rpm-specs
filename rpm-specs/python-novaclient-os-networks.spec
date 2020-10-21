%global srcname novaclient-os-networks
%global upstreamname os_networksv2_python_novaclient_ext

Name:		python-%{srcname}
Version:	0.26
Release:	16%{?dist}
Summary:	Adds network extension support to python-novaclient

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{upstreamname}
Source0:	https://files.pythonhosted.org/packages/source/o/%{upstreamname}/%{upstreamname}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel

%description
%{summary}

%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:	python3-novaclient
Requires:	python3-novaclient
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{upstreamname}-%{version}


%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.26-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.26-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.26-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.26-9
- Subpackage python2-novaclient-os-networks has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.26-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.26-3
- Rebuild for Python 3.6

* Sun Aug 07 2016 Ricardo Cordeiro <gryfrev8-redhat.com-rjmco@tux.com.pt> - 0.26-2
- Added python3 subpackage
- Removed the check section as no checks are defined by upstream

* Fri Aug 05 2016 Ricardo Cordeiro <gryfrev8-redhat.com-rjmco@tux.com.pt> - 0.26-1
- Version bump to 0.26
- Update Source0 to use files.pythonhosted.org

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 03 2016 Ricardo Cordeiro <gryfrev8-redhat.com-rjmco@tux.com.pt> - 0.25-2
- Replaced the use of sum with summary

* Sat Feb 20 2016 Ricardo Cordeiro <gryfrev8-redhat.com-rjmco@tux.com.pt> - 0.25-1
- Initial package
