Name:           unpaper
Version:        0.3
Release:        24%{?dist}
Summary:        Post-processing of scanned and photocopied book pages
# Licensed under any GPL version since none is specified
License:        GPL+
URL:            http://unpaper.berlios.de/
Source0:        http://download.berlios.de/%{name}/%{name}-%{version}.tar.gz
Patch0:         unpaper-0.3-format-security.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  sed

%description
unpaper is a post-processing tool for scanned sheets of paper, especially for
book pages that have been scanned from previously created photocopies. The
main purpose is to make scanned book pages better readable on screen after
conversion to PDF. Additionally, unpaper might be useful to enhance the
quality of scanned pages before performing optical character recognition (OCR).
unpaper tries to clean scanned images by removing dark edges that appeared
through scanning or copying on areas outside the actual page content (e.g. dark
areas between the left-hand-side and the right-hand-side of a double- sided
book-page scan). The program also tries to detect misaligned centering and
rotation of pages and will automatically straighten each page by rotating it to
the correct angle. This process is called "deskewing".

%prep
%setup -q
%patch0 -p1
# fix eol encoding in LICENSE
sed -i -e 's/\r//' LICENSE

%build
cd src
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -o unpaper unpaper.c -lm

%install
install -d $RPM_BUILD_ROOT/%{_bindir}
install -p -m 0755 src/unpaper $RPM_BUILD_ROOT/%{_bindir}

%files
%license LICENSE
%{_bindir}/*
%doc doc CHANGELOG README

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 07 2016 Petr Pisar <ppisar@redhat.com> - 0.3-15
- Modernize spec file

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3-11
- Fix FTBFS with -Werror=format-security (#1037369, #1107039)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3-2
- Autorebuild for GCC 4.3

* Mon Jan 21 2008 Bernard Johnson <bjohnson@symetrix.com> - 0.3-1
- 0.3
- license clarification

* Mon Mar 19 2007 Bernard Johnson <bjohnson@symetrix.com> - 0_2-2
- repackage tgz file without included ELF binary

* Thu Mar 15 2007 Bernard Johnson <bjohnson@symetrix.com> - 0_2-1
- initial release
