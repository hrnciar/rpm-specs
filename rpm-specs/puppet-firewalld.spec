Name:		puppet-firewalld
Version:	0.2.2
Release:	11%{?dist}
Summary:	A Puppet module for FirewallD
License:	GPLv2+
URL:		https://github.com/jpopelka/puppet-firewalld

Source0:	https://github.com/jpopelka/puppet-firewalld/archive/v%{version}.tar.gz

BuildArch:	noarch

Requires:	puppet


%description
A Puppet module used for installing, configuring and managing FirewallD.

%prep
%setup -qn puppet-firewalld-%{version}

%install
mkdir -p %{buildroot}%{_datadir}/puppet/modules/firewalld/
cp -rp manifests/ %{buildroot}%{_datadir}/puppet/modules/firewalld/manifests/
cp -rp templates/ %{buildroot}%{_datadir}/puppet/modules/firewalld/templates/
cp -p metadata.json %{buildroot}%{_datadir}/puppet/modules/firewalld/metadata.json

%files
%doc LICENSE README examples
%{_datadir}/puppet/modules/firewalld

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 03 2014 Jiri Popelka <jpopelka@redhat.com> - 0.2.2-1
- 0.2.2

* Wed Sep 03 2014 Jiri Popelka <jpopelka@redhat.com> - 0.2.1-1
- 0.2.1

* Fri Aug 29 2014 Jiri Popelka <jpopelka@redhat.com> - 0.2.0-1
- 0.2.0

* Wed Aug 20 2014 Jiri Popelka <jpopelka@redhat.com> - 0.1.3-1
- 0.1.3

* Mon Aug 04 2014 Jiri Popelka <jpopelka@redhat.com> - 0.1.2-1
- 0.1.2

* Wed Jul 16 2014 Jiri Popelka <jpopelka@redhat.com> - 0.1.1-2
- fixed source URL

* Mon Jul 14 2014 Jiri Popelka <jpopelka@redhat.com> - 0.1.1-1
- improved metadata

* Fri Jul 11 2014 Jiri Popelka <jpopelka@redhat.com> - 0.1-1
- initial version
