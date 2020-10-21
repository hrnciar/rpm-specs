Name:           cups-x2go
Version:        3.0.1.3
Release:        10%{?dist}
Summary:        CUPS backend for printing from X2Go

License:        GPLv2+
URL:            http://www.x2go.org/
Source0:        http://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       cups
Requires:       ghostscript
Requires:       openssh-clients

%description
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - audio support
    - authentication by smartcard and USB stick

CUPS backend for printing from X2Go.


%prep
%setup -q


%install
mkdir -p %{buildroot}%{_prefix}/lib/cups/backend/
# The cups-x2go backends wants root permissions. So give it to them.
# http://www.cups.org/documentation.php/doc-1.4/man-backend.html says:
# “Backends without world execute permissions are run as the root user.
# Otherwise, the backend is run using the unprivileged user account,
# typically "lp".”
install -pm700 cups-x2go %{buildroot}%{_prefix}/lib/cups/backend/
mkdir -p %{buildroot}%{_sysconfdir}/cups/
cp -p cups-x2go.conf %{buildroot}%{_sysconfdir}/cups/
mkdir -p %{buildroot}%{_datadir}/ppd/cups-x2go/
cp -p CUPS-X2GO.ppd %{buildroot}%{_datadir}/ppd/cups-x2go/
mkdir -p %{buildroot}%{_datadir}/x2go/versions
cp -p VERSION.cups-x2go %{buildroot}%{_datadir}/x2go/versions/


%files
%doc ChangeLog COPYING README.txt
%{_prefix}/lib/cups/backend/cups-x2go
%config(noreplace) %{_sysconfdir}/cups/cups-x2go.conf
%{_datadir}/ppd/cups-x2go/
%{_datadir}/x2go/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Orion Poplawski <orion@cora.nwra.com> - 3.0.1.3-1
- Update to 3.0.1.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Orion Poplawski <orion@cora.nwra.com> - 3.0.1.1-1
- Update to 3.0.1.1
- Require openssh-clients

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 9 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.1.0-1
- Update to 3.0.1.0

* Wed Sep 4 2013 Orion Poplawski <orion@cora.nwra.com> 3.0.0.4-2
- Use install to set permissions on cups-x2go
- Drop %%doc for now
- Mark config file as %%config(noreplace)
- Fix Group
- Drop tabs

* Fri Dec 14 2012 Orion Poplawski <orion@cora.nwra.com> 3.0.0.4-1
- Initial Fedora package
