Name:		cowpatty
Version:	4.6
Release:	20%{?dist}
Summary:	WPA password cracker

License:	GPLv2 and BSD 
URL:		http://wirelessdefence.org/Contents/coWPAttyMain.htm
Source0:	http://wirelessdefence.org/Contents/Files/%{name}-%{version}.tgz

BuildRequires:  gcc
BuildRequires:	libpcap-devel
BuildRequires:	openssl-devel	
		
%description
Cowpatty is designed to audit the pre-shared key (PSK) selection for WPA 
networks based on the TKIP protocol. It can perform both dictionary and 
computed rainbow table attacks.


%prep
%setup -q


%build
make CFLAGS="%{optflags} -DOPENSSL"

%install
rm -rf %{buildroot}
install -D -pm 755 cowpatty %{buildroot}%{_bindir}/%{name}
install -D -pm 755 genpmk %{buildroot}%{_bindir}/genpmk



%files
%doc AUTHORS COPYING README FAQ TODO CHANGELOG
%{_bindir}/%{name}
%{_bindir}/genpmk


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 29 2010 Arun SAG <sagarun [AT] gmail dot com> - 4.6-3
- Fixing koji build failure.
- License fixed.

* Sun Apr 11 2010 Arun SAG <sagarun [AT] gmail dot com> - 4.6-2
- Source url adjusted with macros.
- INSTALL file removed from package.
- Minor cosmetic fixes.

* Sat Apr 10 2010 Arun SAG <sagarun [AT] gmail dot com> -  4.6-1
- Initial build.
