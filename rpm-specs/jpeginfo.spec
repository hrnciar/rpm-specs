
Name:		jpeginfo
Version:	1.6.1
Release:	14%{?dist}
Summary:	Error-check and generate informative listings from JPEG files

License:	GPLv2+
URL:		http://www.kokkonen.net/tjko/projects.html
Source0:	http://www.kokkonen.net/tjko/src/%{name}-%{version}.tar.gz

Provides:	bundled(md5-plumb)

BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	libjpeg-devel
BuildRequires:	make


%description
Jpeginfo prints information and tests integrity of JPEG/JFIF files. It can
generate informative listings of .jpg files, and can also be used to test
them for errors (and optionally delete broken files).


%prep
%setup -q
rm getopt*.*


%build
%configure
make %{?_smp_mflags}


%install
install -Dpm 0755 jpeginfo %{buildroot}/%{_bindir}/jpeginfo
install -Dpm 0644 jpeginfo.1 %{buildroot}/%{_mandir}/man1/jpeginfo.1


%files
%license COPYRIGHT COPYING
%doc README
%{_bindir}/jpeginfo
%{_mandir}/man1/*.1*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Denis Fateyev <denis@fateyev.com> - 1.6.1-11
- Spec cleanup, added BR

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Denis Fateyev <denis@fateyev.com> - 1.6.1-1
- Initial Fedora RPM package
