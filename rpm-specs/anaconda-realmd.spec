Name:		anaconda-realmd
Version:	0.2
Release:	14%{?dist}
Summary:	Anaconda addon which interacts with realmd to join domains
License:	GPLv2+
URL:		http://git.fedorahosted.org/cgit/anaconda-realmd.git/
Source0:	https://fedorahosted.org/releases/a/n/anaconda-realmd/anaconda-realmd-%{version}.tgz

BuildArch:	noarch
BuildRequires:	python3-devel
Requires:	anaconda >= 19
Requires:	realmd >= 0.12

%description
This is a addon for Anaconda which allows use of 'realm' commands in the
kickstart file to join domains.

%define _hardened_build 1

%prep
%setup -q

%build

%install
make install DESTDIR=%{buildroot}

%files
%dir %{_datadir}/anaconda/addons/org_fedora_realm/
%dir %{_datadir}/anaconda/addons/org_fedora_realm/ks
%{_datadir}/anaconda/addons/org_fedora_realm/ks/realm.py*
%doc COPYING ChangeLog NEWS README

%changelog
* Wed Sep 09 2020 Petr Viktorin <pviktori@redhat.com> - 0.2-14
- Switch to Python 3 for build

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Stef Walter <stefw@redhat.com> - 0.2-1
- Initial RPM for anaconda-realmd

