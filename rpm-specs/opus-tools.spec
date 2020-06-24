Name:          opus-tools
Version:       0.2
Release:       4%{?dist}
Summary:       A set of tools for the opus audio codec
License:       BSD and GPLv2
URL:           http://www.opus-codec.org/
Source0:       http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: flac-devel
BuildRequires: libogg-devel
BuildRequires: opus-devel
BuildRequires: opusfile-devel
BuildRequires: libopusenc-devel

%description
The Opus codec is designed for interactive speech and audio transmission over 
the Internet. It is designed by the IETF Codec Working Group and incorporates 
technology from Skype's SILK codec and Xiph.Org's CELT codec.

This is a set of tools for the opus codec.

%prep
%setup -q

%build
%configure

%make_build

%install
%make_install

%check
make check %{?_smp_mflags} V=1

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS
%{_bindir}/opus*
%{_datadir}/man/man1/opus*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.2-1
- update to 0.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.10-3
- Add gcc BR

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 13 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.10-1
- update to 0.1.10

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.9-1
- update to 0.1.9

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep  9 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.7-1
- update to 0.1.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.6-1
- update to 0.1.6

* Tue Sep  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.5-1
- update to 0.1.5

* Thu Aug  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.4-1
- update to 0.1.4

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.3-1
- update to 0.1.3

* Thu Jun 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.2-1
- Initial packaging
