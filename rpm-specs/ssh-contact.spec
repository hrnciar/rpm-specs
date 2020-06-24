Name:           ssh-contact
Version:        0.7
Release:        16%{?dist}
Summary:        Establish SSH connections to your IM contacts using Telepathy

License:        GPLv2+
URL:            http://telepathy.freedesktop.org/wiki/SSH-Contact
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  telepathy-glib-devel >= 0.15.5
BuildRequires:  glib2-devel
BuildRequires:  intltool
## BR for vinagre plugin. Enable once it becomes stable.
#BuildRequires:  vinagre-devel
#BuildRequires:  vte-devel

Requires:       openssh-server
Requires:       openssh-clients


%description
%{name} is a client/service tool that makes it easy to connect to
your telepathy IM contacts via SSH. No need to care about dynamic
IP, NAT, port forwarding, or firewalls anymore; if you can chat with
a friend, you can also SSH to their machine. 


#%package vinagre
#Summary:	Vinagre plugin for %{name}
#Group:		Applications/Internet
#Requires:	%{name} = %{version}-%{release}


#%description vinagre
#Vinagre plugin for %{name}.


%prep
%setup -q


%build
%configure --enable-static=no --enable-vinagre=no
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc COPYING NEWS AUTHORS
%{_bindir}/%{name}
%{_libexecdir}/%{name}-service
%{_datadir}/telepathy/clients/SSHContact.client
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.SSHContact.service


#%files vinagre
#%defattr(-,root,root,-)
#%{_libdir}/vinagre-1/plugins

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 12 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.7-1
- Update to 0.7.
- Bump minimum version of tp-glib-devel.

* Mon Jan 09 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.6-2
- Rebuild for new gcc.

* Mon May 16 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.6-1
- Update to 0.6.

* Thu Dec 16 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.4-1
- Initial Fedora spec.
