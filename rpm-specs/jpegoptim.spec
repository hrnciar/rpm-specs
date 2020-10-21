
Name:		jpegoptim
Version:	1.4.6
Release:	6%{?dist}
Summary:	Utility to optimize JPEG files

License:	GPLv2+
URL:		http://www.kokkonen.net/tjko/projects.html

Source0:	http://www.kokkonen.net/tjko/src/%{name}-%{version}.tar.gz

BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	libjpeg-devel
BuildRequires:	make

%description
Jpegoptim is an utility to optimize JPEG files. Provides lossless optimization
(based on optimizing the Huffman tables) and "lossy" optimization based on
setting maximum quality factor.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
install -Dpm 0755 jpegoptim %{buildroot}/%{_bindir}/jpegoptim
install -Dpm 0644 jpegoptim.1 %{buildroot}/%{_mandir}/man1/jpegoptim.1


%files
%{!?_licensedir:%global license %doc}
%license COPYRIGHT COPYING
%doc README
%{_bindir}/jpegoptim
%{_mandir}/man1/*.1*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 28 2018 Denis Fateyev <denis@fateyev.com> - 1.4.6-1
- Update to version 1.4.6

* Sat Apr 07 2018 Denis Fateyev <denis@fateyev.com> - 1.4.5-1
- Update to version 1.4.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 03 2016 Denis Fateyev <denis@fateyev.com> - 1.4.4-1
- Update to version 1.4.4
- Remove unneeded error handling patch

* Sat Feb 20 2016 Denis Fateyev <denis@fateyev.com> - 1.4.3-4
- Added detailed error handling patch
- Modernized the package spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Denis Fateyev <denis@fateyev.com> - 1.4.3-1
- Update to version 1.4.3

* Tue Dec 23 2014 Denis Fateyev <denis@fateyev.com> - 1.4.2-1
- Update to version 1.4.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Denis Fateyev <denis@fateyev.com> - 1.4.1-1
- Update to version 1.4.1

* Sat May 03 2014 Denis Fateyev <denis@fateyev.com> - 1.3.1-1
- Update to version 1.3.1

* Tue Jan 07 2014 Denis Fateyev <denis@fateyev.com> - 1.3.0-1
- Initial Fedora RPM package
